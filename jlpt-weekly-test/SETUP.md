# Weekly N5 Test — Setup Guide

## Overview

- **Friday (local, your PC):** `friday_export.py` reads what you reviewed
  this week from Anki (via AnkiConnect) and pushes a coverage JSON to this repo.
- **Saturday (cloud, GitHub Actions):** `generate_and_send_test.py` reads
  that JSON, asks the Gemini API (free tier) to build a mixed-difficulty
  60-80 question MCQ test — generated in several smaller batches to stay
  comfortably within free-tier rate limits — and emails it to you via
  Gmail SMTP. Runs on GitHub's servers — your PC does not need to be on.

## One-time setup

### 1. AnkiConnect (for Friday's local script)

1. Anki → Tools → Add-ons → Get Add-ons → paste code `2116944090` → OK.
2. Restart Anki.
3. Leave Anki open when you run `friday_export.py`.

### 2. Python environment (local, for Friday's script)

No extra packages needed — `friday_export.py` only uses the standard
library plus `git` on your PATH.

### 3. This repo

The `.github/workflows/weekly-test.yml` must live at the **true repo
root** (GitHub only discovers workflows there, never in a subfolder) —
everything else (`friday_export.py`, `generate_and_send_test.py`,
`weekly-tests/`) stays together under `jlpt-weekly-test/`:

```
your-repo/
├── .github/workflows/weekly-test.yml
└── jlpt-weekly-test/
    ├── friday_export.py
    ├── generate_and_send_test.py
    └── weekly-tests/        (created automatically)
```

The workflow's job sets `working-directory: jlpt-weekly-test` for every
step, so both scripts' relative paths (e.g. `weekly-tests/...`) work
unchanged from that layout.

### 4. Gemini API key (for Saturday's test generation — free)

This is a **free API key from Google AI Studio**, not the same thing as
a Gemini/Google Pro subscription — those are separate, and a Pro chat
subscription does not grant free API quota. The AI Studio free tier is
open to any Google account, subscription or not:

1. Go to https://aistudio.google.com/apikey.
2. Create an API key (a new or existing Google Cloud project is fine —
   no billing needs to be enabled to use the free tier).
3. Copy the key — you'll paste it into GitHub Secrets below.
4. Free-tier rate limits can change — check current numbers at
   https://ai.google.dev/pricing if you ever see rate-limit errors in
   the Actions log. `generate_and_send_test.py` already batches its
   requests with a delay between them (`BATCH_DELAY_SECONDS`, default 6s)
   to stay safely under typical limits.

### 5. Gmail App Password (for Saturday's email send)

Regular Gmail passwords don't work with SMTP anymore — you need an App
Password:

1. Enable 2-Step Verification on the Gmail account, if not already on:
   https://myaccount.google.com/security
2. Go to https://myaccount.google.com/apppasswords
3. Create an app password (name it e.g. "N5 weekly test").
4. Copy the 16-character password — you'll paste it into GitHub Secrets
   next, and you won't be able to view it again.

### 6. GitHub Secrets

In your repo: Settings → Secrets and variables → Actions → New repository secret.
Add these four:

| Secret name | Value |
|---|---|
| `GEMINI_API_KEY` | Your free API key from step 4 (aistudio.google.com/apikey) |
| `GMAIL_ADDRESS` | The Gmail address sending the mail |
| `GMAIL_APP_PASSWORD` | The 16-character app password from step 5 |
| `RECIPIENT_EMAIL` | Where the test should land (can equal `GMAIL_ADDRESS`) |

## Weekly routine

**Friday**, after your study session:
```bash
cd your-repo/jlpt-weekly-test
python friday_export.py
```
This writes `weekly-tests/weekly_coverage_YYYY-MM-DD.json` and pushes it
to GitHub automatically (edit `GIT_AUTO_PUSH = False` in the script if
you'd rather review the file before pushing manually).

**Saturday, ~8:30 AM IST:** the GitHub Action fires automatically and the
test lands in your inbox. No action needed on your end.

## Testing before you trust it

- To test Friday's script without waiting for a real study week, you can
  temporarily set `RATED_DAYS` higher (e.g. `30`) as an env var so it
  picks up older reviews too.
- To test Saturday's job without waiting for Saturday: go to the repo's
  **Actions** tab → "Weekly N5 Test Email" → **Run workflow** (this is
  what `workflow_dispatch` in the YAML enables).

## Tuning

- `QUESTIONS_PER_TOPIC`, `MIN_QUESTIONS`, `MAX_QUESTIONS` in
  `generate_and_send_test.py` control weekly test size — it scales with
  how many topics you reviewed (roughly 2.5 questions/topic), clamped to
  60–80 by default.
- `BATCH_SIZE` (default 15) and `BATCH_DELAY_SECONDS` (default 6) control
  how the test is split into API calls — smaller batches / longer delays
  if you ever hit Gemini free-tier rate limits; check the Actions log for
  batch warnings if some questions go missing.
- `DIFFICULTY_MIX` controls the easy/medium/hard ratio.
- `RATED_DAYS` in `friday_export.py` controls how far back AnkiConnect
  looks. Default `6` assumes you study Sun–Fri; adjust to match your
  actual weekday pattern.
- `DECK_PREFIX` defaults to `JLPT N5` (matching decks like `JLPT N5::Grammer
  Patterns`, `JLPT N5::Kanji Study`). Change via `ANKI_DECK_PREFIX` if your
  naming differs — and if it contains a space, note the query is quoted
  (`deck:"PREFIX*"`) precisely because Anki's search syntax splits on
  whitespace otherwise.

## Known limitations

- If you study Fri night *after* running the export, that session won't
  be captured until next week — run the script as your last step of the day.
- The dedupe logic keeps one entry per `n5-*` tag. Untagged notes (if any
  slip through) are included individually rather than deduped.
- Coverage JSON files accumulate in `weekly-tests/` over time — this is
  intentional (gives you a study history), but you can prune old ones
  periodically if the repo grows large.
