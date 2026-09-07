# Weekly N5 Test — Setup Guide

## Overview

- **Friday (local, your PC):** `friday_export.py` reads what you reviewed
  this week from Anki (via AnkiConnect) and pushes a coverage JSON to this repo.
- **Saturday (cloud, GitHub Actions):** `generate_and_send_test.py` reads
  that JSON, asks Claude to build a mixed-difficulty MCQ test, and emails
  it to you via Gmail SMTP. Runs on GitHub's servers — your PC does not
  need to be on.

## One-time setup

### 1. AnkiConnect (for Friday's local script)

1. Anki → Tools → Add-ons → Get Add-ons → paste code `2116944090` → OK.
2. Restart Anki.
3. Leave Anki open when you run `friday_export.py`.

### 2. Python environment (local, for Friday's script)

No extra packages needed — `friday_export.py` only uses the standard
library plus `git` on your PATH.

### 3. This repo

Push this folder structure to the GitHub repo your pipeline already
lives in (or a new one):

```
your-repo/
├── friday_export.py
├── generate_and_send_test.py
├── .github/workflows/weekly-test.yml
└── weekly-tests/        (created automatically)
```

### 4. Gmail App Password (for Saturday's email send)

Regular Gmail passwords don't work with SMTP anymore — you need an App
Password:

1. Enable 2-Step Verification on the Gmail account, if not already on:
   https://myaccount.google.com/security
2. Go to https://myaccount.google.com/apppasswords
3. Create an app password (name it e.g. "N5 weekly test").
4. Copy the 16-character password — you'll paste it into GitHub Secrets
   next, and you won't be able to view it again.

### 5. GitHub Secrets

In your repo: Settings → Secrets and variables → Actions → New repository secret.
Add these four:

| Secret name | Value |
|---|---|
| `ANTHROPIC_API_KEY` | Your Claude API key from console.anthropic.com |
| `GMAIL_ADDRESS` | The Gmail address sending the mail |
| `GMAIL_APP_PASSWORD` | The 16-character app password from step 4 |
| `RECIPIENT_EMAIL` | Where the test should land (can equal `GMAIL_ADDRESS`) |

## Weekly routine

**Friday**, after your study session:
```bash
cd your-repo
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

- `QUESTIONS_PER_TEST` and `DIFFICULTY_MIX` in `generate_and_send_test.py`
  control test length and easy/medium/hard ratio.
- `RATED_DAYS` in `friday_export.py` controls how far back AnkiConnect
  looks. Default `6` assumes you study Sun–Fri; adjust to match your
  actual weekday pattern.
- `DECK_PREFIX` assumes your decks are named starting with `N5` (e.g.
  `N5::Grammar`, `N5::Kanji`). Change if your naming differs.

## Known limitations

- If you study Fri night *after* running the export, that session won't
  be captured until next week — run the script as your last step of the day.
- The dedupe logic keeps one entry per `n5-*` tag. Untagged notes (if any
  slip through) are included individually rather than deduped.
- Coverage JSON files accumulate in `weekly-tests/` over time — this is
  intentional (gives you a study history), but you can prune old ones
  periodically if the repo grows large.
