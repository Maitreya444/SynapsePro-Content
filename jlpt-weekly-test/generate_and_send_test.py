"""
generate_and_send_test.py
--------------------------
Runs in GitHub Actions every Saturday. No Anki / AnkiConnect dependency —
reads whatever weekly_coverage_*.json file Friday's local script pushed
to the repo, generates a mixed-difficulty MCQ test grounded in that
content via the Gemini API (free tier via Google AI Studio — separate
from any Gemini/Google Pro subscription, no billing required), renders
it as HTML, and emails it via Gmail SMTP.

The test is generated in several smaller batched API calls rather than
one big call — this keeps each individual response small and reliable
to parse, and keeps well within Gemini's free-tier rate limits (a short
delay is inserted between batches). If a batch fails after retries, it's
skipped rather than failing the whole run — you still get a (slightly
shorter) test rather than no email at all.

Required environment variables (set as GitHub Secrets):
    GEMINI_API_KEY        - free API key from https://aistudio.google.com/apikey
                             (this is NOT the same thing as a Gemini/Google
                             Pro subscription — the free API tier is open to
                             any Google account regardless of subscription)
    GMAIL_ADDRESS          - the Gmail account sending the mail
    GMAIL_APP_PASSWORD     - a Google App Password (NOT your normal password;
                             requires 2-Step Verification enabled on the account:
                             https://myaccount.google.com/apppasswords)
    RECIPIENT_EMAIL        - where the test should be sent (can be the same
                             Gmail address, i.e. send-to-self)
"""

import glob
import json
import os
import smtplib
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from google import genai
from google.genai import types

# ---------------- CONFIG ----------------
COVERAGE_DIR = "weekly-tests"
MODEL = "gemini-2.5-flash"

# Weekly question count scales with how much you actually reviewed,
# clamped to a sane range rather than a fixed number.
QUESTIONS_PER_TOPIC = 2.5
MIN_QUESTIONS = 60
MAX_QUESTIONS = 80

# Split into batched API calls instead of one giant request.
BATCH_SIZE = 15
BATCH_DELAY_SECONDS = int(os.environ.get("BATCH_DELAY_SECONDS", "6"))
MAX_BATCH_RETRIES = 2

DIFFICULTY_MIX = {"easy": 0.4, "medium": 0.4, "hard": 0.2}
# -----------------------------------------


def find_latest_coverage_file():
    files = sorted(glob.glob(os.path.join(COVERAGE_DIR, "weekly_coverage_*.json")))
    if not files:
        sys.exit(f"No weekly_coverage_*.json files found in {COVERAGE_DIR}/. "
                  f"Did Friday's export run and push successfully?")
    return files[-1]  # latest by filename (date-sorted)


def build_topic_block(topics):
    topic_lines = []
    for t in topics:
        f = t["fields"]
        tag = next((tg for tg in t["tags"] if tg.startswith("n5-")), "untagged")
        # Pull whichever fields exist across your different note types
        summary_bits = []
        for key in ("Question", "Answer", "Japanese", "English", "Marathi", "Example"):
            if key in f and f[key].strip():
                summary_bits.append(f"{key}: {f[key]}")
        topic_lines.append(f"- [{tag}] " + " | ".join(summary_bits))
    return "\n".join(topic_lines)


def compute_target_count(topic_count):
    target = round(topic_count * QUESTIONS_PER_TOPIC)
    return max(MIN_QUESTIONS, min(MAX_QUESTIONS, target))


def compute_batch_sizes(total):
    sizes = []
    remaining = total
    while remaining > 0:
        size = min(BATCH_SIZE, remaining)
        sizes.append(size)
        remaining -= size
    return sizes


def build_batch_prompt(topic_block, batch_size, n_easy, n_medium, n_hard,
                        avoid_list, batch_num, total_batches):
    avoid_block = ""
    if avoid_list:
        avoid_lines = "\n".join(f"- {item}" for item in avoid_list)
        avoid_block = f"""
Questions already generated in earlier batches of this same test — do NOT
repeat these, or ask near-identical questions about the same narrow point:
{avoid_lines}
"""

    return f"""You are generating batch {batch_num} of {total_batches} of a JLPT N5-level
Japanese practice test for a Marathi-speaking learner.

Below is the exact list of grammar points, kanji, and vocabulary the learner
reviewed this week (Anki export). Base EVERY question strictly on this list —
do not introduce grammar or vocabulary beyond N5 level, and do not test
anything not in this list.

WEEK'S COVERAGE:
{topic_block}
{avoid_block}
Generate exactly {batch_size} multiple-choice questions for THIS batch:
- {n_easy} easy (direct recall/recognition)
- {n_medium} medium (requires applying the grammar/vocab in a new short sentence)
- {n_hard} hard (requires combining 2+ concepts from the list, or distinguishing it from a close distractor)

For each question include:
- "difficulty": "easy" | "medium" | "hard"
- "topic_tag": the source tag this question tests
- "question": the question text (Japanese where relevant, with English/Marathi context as needed)
- "options": exactly 4 answer choices
- "correct_index": 0-based index of the correct option
- "explanation": one or two sentences explaining the correct answer, written so a Marathi-speaking N5 learner understands the grammar logic (Marathi phrases welcome where helpful)

Respond with ONLY a JSON object of this exact shape, no markdown fences, no preamble:
{{
  "questions": [
    {{
      "difficulty": "easy",
      "topic_tag": "n5-particle-14",
      "question": "...",
      "options": ["...", "...", "...", "..."],
      "correct_index": 0,
      "explanation": "..."
    }}
  ]
}}
"""


def call_gemini(prompt):
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(response_mime_type="application/json"),
    )
    text = (response.text or "").strip()
    text = text.replace("```json", "").replace("```", "").strip()
    return json.loads(text)  # raises json.JSONDecodeError on bad output


def generate_batch(topic_block, batch_size, n_easy, n_medium, n_hard,
                    avoid_list, batch_num, total_batches):
    prompt = build_batch_prompt(
        topic_block, batch_size, n_easy, n_medium, n_hard,
        avoid_list, batch_num, total_batches,
    )

    last_error = None
    for attempt in range(1, MAX_BATCH_RETRIES + 2):  # initial try + retries
        try:
            data = call_gemini(prompt)
            questions = data["questions"]
            if not questions:
                raise ValueError("Gemini returned an empty questions list")
            return questions
        except Exception as e:
            last_error = e
            print(f"  Batch {batch_num}/{total_batches} attempt {attempt} failed: {e}")
            if attempt <= MAX_BATCH_RETRIES:
                time.sleep(BATCH_DELAY_SECONDS)

    print(f"  WARNING: batch {batch_num}/{total_batches} failed after "
          f"{MAX_BATCH_RETRIES} retries — skipping it ({batch_size} questions "
          f"lost). Last error: {last_error}")
    return []


def generate_all_questions(coverage):
    topics = coverage["topics"]
    topic_block = build_topic_block(topics)

    total_target = compute_target_count(len(topics))
    batch_sizes = compute_batch_sizes(total_target)
    print(f"Topics this week: {len(topics)} -> target {total_target} questions "
          f"across {len(batch_sizes)} batches")

    all_questions = []
    avoid_list = []

    for i, size in enumerate(batch_sizes, start=1):
        n_easy = round(size * DIFFICULTY_MIX["easy"])
        n_medium = round(size * DIFFICULTY_MIX["medium"])
        n_hard = size - n_easy - n_medium

        print(f"Requesting batch {i}/{len(batch_sizes)}: {size} questions "
              f"({n_easy} easy / {n_medium} medium / {n_hard} hard)...")

        batch_questions = generate_batch(
            topic_block, size, n_easy, n_medium, n_hard,
            avoid_list, i, len(batch_sizes),
        )
        all_questions.extend(batch_questions)
        avoid_list.extend(
            f"[{q.get('topic_tag', '?')}] {q.get('question', '')[:70]}"
            for q in batch_questions
        )

        if i < len(batch_sizes):
            time.sleep(BATCH_DELAY_SECONDS)

    if len(all_questions) < total_target * 0.5:
        sys.exit(
            f"Only generated {len(all_questions)}/{total_target} questions — "
            f"too many batches failed. Aborting rather than sending a broken "
            f"test. Check the batch warnings above for the underlying error."
        )

    print(f"Generated {len(all_questions)}/{total_target} questions total.")
    return all_questions


DIFFICULTY_COLORS = {"easy": "#2e7d32", "medium": "#e6a700", "hard": "#c62828"}
DIFFICULTY_LABELS_MR = {"easy": "सोपे", "medium": "मध्यम", "hard": "कठीण"}


def render_html(questions, coverage_date):
    q_html_parts = []

    for i, q in enumerate(questions, start=1):
        color = DIFFICULTY_COLORS.get(q["difficulty"], "#555")
        mr_label = DIFFICULTY_LABELS_MR.get(q["difficulty"], q["difficulty"])
        options_html = "".join(
            f'<li style="margin:4px 0;">{chr(65+j)}. {opt}</li>'
            for j, opt in enumerate(q["options"])
        )
        correct_letter = chr(65 + q["correct_index"])

        q_html_parts.append(f"""
        <div style="border:1px solid #ddd; border-radius:8px; padding:16px; margin-bottom:16px; background:#fafafa;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <strong>Q{i}.</strong>
            <span style="background:{color}; color:white; padding:2px 10px; border-radius:12px; font-size:12px;">
              {q['difficulty'].upper()} / {mr_label}
            </span>
          </div>
          <p style="margin:10px 0; font-size:16px;">{q['question']}</p>
          <ol type="A" style="list-style:none; padding-left:0;">{options_html}</ol>
          <details style="margin-top:8px;">
            <summary style="cursor:pointer; color:#555;">Show answer / उत्तर पहा</summary>
            <p><strong>Correct: {correct_letter}</strong></p>
            <p style="color:#444;">{q['explanation']}</p>
          </details>
          <p style="font-size:11px; color:#999; margin-top:6px;">Tag: {q['topic_tag']}</p>
        </div>
        """)

    html = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="font-family: -apple-system, Segoe UI, sans-serif; max-width:640px; margin:0 auto; padding:16px; color:#222;">
  <h1 style="font-size:22px;">📝 Weekly N5 Test — {coverage_date}</h1>
  <p style="color:#555;">Based on your Anki reviews this week. {len(questions)} questions, mixed difficulty. Answers are collapsed — tap "Show answer" after you've committed to a choice.</p>
  {''.join(q_html_parts)}
  <p style="color:#999; font-size:12px; margin-top:24px;">Generated automatically from your JLPT N5 Anki pipeline.</p>
</body>
</html>"""
    return html


def send_email(html_body, coverage_date):
    gmail_address = os.environ["GMAIL_ADDRESS"]
    # Google displays app passwords with spaces for readability, but the real
    # credential is the 16 characters without them -- strip defensively in
    # case the secret was stored with spaces intact.
    gmail_app_password = os.environ["GMAIL_APP_PASSWORD"].replace(" ", "")
    recipient = os.environ.get("RECIPIENT_EMAIL", gmail_address)

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"N5 Weekly Test — {coverage_date}"
    msg["From"] = gmail_address
    msg["To"] = recipient
    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(gmail_address, gmail_app_password)
        server.sendmail(gmail_address, recipient, msg.as_string())

    print(f"Email sent to {recipient}")


def main():
    coverage_path = find_latest_coverage_file()
    print(f"Using coverage file: {coverage_path}")

    with open(coverage_path, "r", encoding="utf-8") as f:
        coverage = json.load(f)

    questions = generate_all_questions(coverage)

    html_body = render_html(questions, coverage["generated_on"])
    send_email(html_body, coverage["generated_on"])


if __name__ == "__main__":
    main()
