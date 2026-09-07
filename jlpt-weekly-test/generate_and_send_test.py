"""
generate_and_send_test.py
--------------------------
Runs in GitHub Actions every Saturday. No Anki / AnkiConnect dependency —
reads whatever weekly_coverage_*.json file Friday's local script pushed
to the repo, generates a mixed-difficulty MCQ test grounded in that
content via the Claude API, renders it as HTML, and emails it via Gmail
SMTP.

Required environment variables (set as GitHub Secrets):
    ANTHROPIC_API_KEY
    GMAIL_ADDRESS        - the Gmail account sending the mail
    GMAIL_APP_PASSWORD    - a Google App Password (NOT your normal password;
                            requires 2-Step Verification enabled on the account:
                            https://myaccount.google.com/apppasswords)
    RECIPIENT_EMAIL       - where the test should be sent (can be the same
                            Gmail address, i.e. send-to-self)
"""

import glob
import json
import os
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import anthropic

# ---------------- CONFIG ----------------
COVERAGE_DIR = "weekly-tests"
MODEL = "claude-sonnet-4-6"
QUESTIONS_PER_TEST = 15
DIFFICULTY_MIX = {"easy": 0.4, "medium": 0.4, "hard": 0.2}
# -----------------------------------------


def find_latest_coverage_file():
    files = sorted(glob.glob(os.path.join(COVERAGE_DIR, "weekly_coverage_*.json")))
    if not files:
        sys.exit(f"No weekly_coverage_*.json files found in {COVERAGE_DIR}/. "
                  f"Did Friday's export run and push successfully?")
    return files[-1]  # latest by filename (date-sorted)


def build_prompt(coverage):
    topics = coverage["topics"]

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

    topic_block = "\n".join(topic_lines)

    n_easy = round(QUESTIONS_PER_TEST * DIFFICULTY_MIX["easy"])
    n_medium = round(QUESTIONS_PER_TEST * DIFFICULTY_MIX["medium"])
    n_hard = QUESTIONS_PER_TEST - n_easy - n_medium

    prompt = f"""You are generating a JLPT N5-level Japanese practice test for a Marathi-speaking learner.

Below is the exact list of grammar points, kanji, and vocabulary the learner reviewed this week (Anki export). Base EVERY question strictly on this list — do not introduce grammar or vocabulary beyond N5 level, and do not test anything not in this list.

WEEK'S COVERAGE:
{topic_block}

Generate exactly {QUESTIONS_PER_TEST} multiple-choice questions:
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
    return prompt


def call_claude(prompt):
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env
    response = client.messages.create(
        model=MODEL,
        max_tokens=8000,
        messages=[{"role": "user", "content": prompt}],
    )
    text = response.content[0].text.strip()
    text = text.replace("```json", "").replace("```", "").strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        sys.exit(f"Failed to parse Claude's response as JSON: {e}\n\nRaw response:\n{text}")


DIFFICULTY_COLORS = {"easy": "#2e7d32", "medium": "#e6a700", "hard": "#c62828"}
DIFFICULTY_LABELS_MR = {"easy": "सोपे", "medium": "मध्यम", "hard": "कठीण"}


def render_html(test_data, coverage_date):
    questions = test_data["questions"]
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
    gmail_app_password = os.environ["GMAIL_APP_PASSWORD"]
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

    prompt = build_prompt(coverage)
    print("Calling Claude API...")
    test_data = call_claude(prompt)

    html_body = render_html(test_data, coverage["generated_on"])
    send_email(html_body, coverage["generated_on"])


if __name__ == "__main__":
    main()
