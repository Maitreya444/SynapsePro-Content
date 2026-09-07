"""
friday_export.py
-----------------
Run this locally on Friday, after your study session, with Anki open
(AnkiConnect add-on must be installed and running).

What it does:
1. Queries AnkiConnect for every card reviewed since Sunday (rated:6)
   across your N5 decks.
2. Pulls the note fields + tags for each card.
3. Dedupes by grammar/kanji/vocab tag, so 15 reviews of the same
   grammar point collapse into one topic entry.
4. Writes weekly-tests/weekly_coverage_YYYY-MM-DD.json
5. Commits and pushes that file to the repo, so Saturday's cloud job
   can pick it up.

Usage:
    python friday_export.py

Config (edit the CONFIG block below, or set as env vars):
    ANKI_DECK_PREFIX   - deck name prefix to scope the query (default "N5")
    RATED_DAYS         - how many days back to check reviews (default 6,
                          i.e. "since Sunday" if you run this Friday night)
"""

import json
import os
import subprocess
import sys
import urllib.request
from collections import defaultdict
from datetime import date

# ---------------- CONFIG ----------------
ANKICONNECT_URL = "http://localhost:8765"
DECK_PREFIX = os.environ.get("ANKI_DECK_PREFIX", "JLPT N5")
RATED_DAYS = int(os.environ.get("RATED_DAYS", "6"))
OUTPUT_DIR = "weekly-tests"
GIT_AUTO_PUSH = True  # set False if you want to review the file before pushing
# -----------------------------------------


def anki_request(action, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    req = urllib.request.Request(ANKICONNECT_URL, payload)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.load(resp)
    except Exception as e:
        sys.exit(
            f"ERROR: Could not reach AnkiConnect at {ANKICONNECT_URL}.\n"
            f"Make sure Anki is open and the AnkiConnect add-on is installed.\n"
            f"Details: {e}"
        )
    if result.get("error") is not None:
        sys.exit(f"AnkiConnect error: {result['error']}")
    return result["result"]


def get_reviewed_cards():
    # Quote the deck name -- Anki's search syntax splits on whitespace, so an
    # unquoted deck prefix containing a space (e.g. "JLPT N5") silently breaks.
    query = f'deck:"{DECK_PREFIX}*" rated:{RATED_DAYS}'
    card_ids = anki_request("findCards", query=query)
    if not card_ids:
        sys.exit(f"No cards found for query '{query}'. Nothing to export.")
    return card_ids


def get_notes_for_cards(card_ids):
    cards_info = anki_request("cardsInfo", cards=card_ids)
    note_ids = list({c["note"] for c in cards_info})
    notes_info = anki_request("notesInfo", notes=note_ids)
    return notes_info


def pick_topic_tag(tags):
    """Pick the most specific n5-* tag to use as the dedupe key."""
    n5_tags = [t for t in tags if t.startswith("n5-")]
    if n5_tags:
        return n5_tags[0]
    return None


def dedupe_by_topic(notes_info):
    """Collapse repeated reviews of the same tagged topic into one entry."""
    topics = {}
    untagged = []

    for note in notes_info:
        tags = note.get("tags", [])
        fields = {k: v["value"] for k, v in note.get("fields", {}).items()}
        topic_tag = pick_topic_tag(tags)

        entry = {
            "tags": tags,
            "fields": fields,
            "modelName": note.get("modelName"),
        }

        if topic_tag:
            # Keep the first occurrence; later dupes are just extra reviews
            if topic_tag not in topics:
                topics[topic_tag] = entry
        else:
            untagged.append(entry)

    return list(topics.values()) + untagged


def write_coverage_file(items):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    today = date.today().isoformat()
    out_path = os.path.join(OUTPUT_DIR, f"weekly_coverage_{today}.json")

    payload = {
        "generated_on": today,
        "deck_prefix": DECK_PREFIX,
        "rated_days": RATED_DAYS,
        "topic_count": len(items),
        "topics": items,
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"Wrote {out_path} ({len(items)} unique topics)")
    return out_path


def git_commit_and_push(file_path):
    try:
        subprocess.run(["git", "add", file_path], check=True)
        subprocess.run(
            ["git", "commit", "-m", f"Weekly coverage export: {os.path.basename(file_path)}"],
            check=True,
        )
        subprocess.run(["git", "push"], check=True)
        print("Committed and pushed to repo.")
    except subprocess.CalledProcessError as e:
        print(f"WARNING: git commit/push failed — push manually. Details: {e}")


def main():
    print(f"Querying AnkiConnect: deck:{DECK_PREFIX}* rated:{RATED_DAYS} ...")
    card_ids = get_reviewed_cards()
    print(f"Found {len(card_ids)} reviewed cards.")

    notes_info = get_notes_for_cards(card_ids)
    print(f"Resolved to {len(notes_info)} unique notes.")

    deduped = dedupe_by_topic(notes_info)
    out_path = write_coverage_file(deduped)

    if GIT_AUTO_PUSH:
        git_commit_and_push(out_path)
    else:
        print("GIT_AUTO_PUSH is False — commit and push manually when ready.")


if __name__ == "__main__":
    main()
