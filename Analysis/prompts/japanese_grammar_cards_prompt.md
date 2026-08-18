# Japanese N5 Grammar Cards — Generation Prompts

Reusable prompts for turning `Japanese/N5/Topics.md`'s 127 grammar patterns (`G001`-`G127`,
deduplicated — see that file's changelog) into recall cards appended to
`Japanese/N5/Grammar/cards.md`, parsed by `scripts/japanese_markdown_parser.py` ->
`scripts/build_japanese_anki.py`.

Run in batches of ~15-20 patterns — Topics.md's "Part 1 — Checklist" is organized into 18
categories, which is a natural set of batch boundaries; each row there also has a `Done` checkbox
for tracking which batches are finished. Review each batch before moving to the next.

## Card format

7 fields now (added `Mnemonic` and `AI Notes` — matching the same two fields the DGCA note type
already uses, see `scripts/markdown_parser.py`). No parser changes needed either time; they're just
plain-text fields captured between labels.

| Field | Content |
|---|---|
| Question | Plain recall prompt: `What does 「<pattern>」mean?` |
| Answer | Short English meaning (1 line) |
| Marathi | One Marathi example sentence (Devanagari script) that carries the same meaning/function as the pattern, plus its English meaning — not a literal word-for-word gloss. Japanese and Marathi are both SOV languages with particle/postposition-driven grammar, so note the parallel in one short clause where it's genuinely there; don't force it where it isn't. |
| Example | 3 Japanese example sentences for the pattern, graded **easy / medium / hard**. Each gets: the sentence, furigana for any non-obvious kanji, an English translation, and a one-line note on why it illustrates the rule. |
| Mnemonic | A short memory hook for the pattern itself — wordplay, a sound association, or a visual. Only include one where it's genuinely useful; don't force a weak one. |
| AI Notes | The most common mistake learners make with this specific pattern, and/or a key point worth remembering (e.g. an irregular form, a contrast with a similar-looking pattern). 1-3 sentences. |
| Reference | `Topics.md G0xx` |

Card shape (fields must appear on their own line, in this exact order, for every card — a
downstream parser splits on lines starting with `# ` and finds fields by plain substring search):

```
# G0xx - <short romaji pattern name>

Question
What does 「<pattern>」mean?

Answer
<English meaning>

Marathi
<Marathi example sentence in Devanagari> — <its English meaning>

Example
Easy: <Japanese sentence> (<furigana>) — <English translation> (Why: <one-line note>)
Medium: <Japanese sentence> (<furigana>) — <English translation> (Why: <one-line note>)
Hard: <Japanese sentence> (<furigana>) — <English translation> (Why: <one-line note>)

Mnemonic
<short memory hook, or omit the line's content if none fits naturally>

AI Notes
<common mistake and/or key point to remember for this pattern>

Reference
Topics.md G0xx

---
```

## Copilot version

Run inside this repo (VS Code), one batch (category) at a time, appending to the same file.

```text
You are helping build the Japanese N5 grammar flashcard source file for the SynapsePro repo.

Read first: Japanese/N5/Topics.md — Part 1 (Checklist) for the pattern list and category batches,
Part 2 (Full Catalogue) for each pattern's canonical example sentence.

Task: for grammar patterns G0xx-G0xx (category: <category name>, from Part 1), append to
Japanese/N5/Grammar/cards.md one card per pattern in this exact structure (field labels verbatim,
one per line, in this order — a dedicated parser splits on lines starting with "# " and finds
fields by plain substring search in order):

# G0xx - <short romaji pattern name>

Question
What does 「<pattern>」mean?

Answer
<short English meaning, 1 line>

Marathi
<one Marathi example sentence in Devanagari script that carries the same meaning/function as the
pattern> — <its English meaning>. Japanese and Marathi are both SOV languages with
particle/postposition-driven grammar, so note the structural parallel in one short clause if it's
genuinely there; don't force a parallel that isn't natural for this particular pattern.

Example
Find 2-3 real example sentences for this pattern (Topics.md Part 2 has one canonical example per
pattern — use it as your "medium" example if it fits), then give exactly 3, graded by difficulty,
each on its own line in this format:
Easy: <simple sentence> (<furigana for any non-obvious kanji, in parentheses>) — <English
translation> (Why: <one-line note on how this sentence shows the grammar rule>)
Medium: <a bit more complex, e.g. one added modifier or clause> — same format
Hard: <more complex, e.g. multiple clauses or less common vocabulary — but still N5-level grammar
only, don't reach for N4+ constructions> — same format

Mnemonic
A short memory hook for the pattern itself (wordplay, sound association, or a visual). Only include
one if it's genuinely useful — don't force a weak one just to fill the field.

AI Notes
The single most common mistake learners make with this specific pattern (e.g. wrong verb form
before it, confusing it with a similar-looking pattern, an irregular exception), plus any other key
point worth remembering. 1-3 sentences.

Reference
Topics.md G0xx

---

Rules:
1. Every card starts with a line beginning with "# ".
2. All 7 labels (Question, Answer, Marathi, Example, Mnemonic, AI Notes, Reference) appear on their
   own line, in that exact order, for every card.
3. Never use these 7 label words inside another field's body text.
4. Preserve G-codes exactly as in Topics.md.
5. All Japanese must stay at N5 grammar level, even the "hard" example — vary vocabulary and
   sentence length, not grammar complexity.
6. Do this range only; stop and wait so each batch can be reviewed before continuing.
```

## NotebookLM version

Upload `Japanese/N5/Topics.md` as a source first. Paste the prompt below per batch (one category
at a time), then manually copy the response into `Japanese/N5/Grammar/cards.md`.

```text
Using the uploaded Topics.md as the source for the pattern list and each pattern's canonical
example (Part 2), generate flashcard text for grammar patterns G0xx-G0xx (category: <category
name>, from Part 1). For the Marathi field, use your general knowledge of Marathi (it is not in
the uploaded source) — Japanese and Marathi are both SOV, particle-driven languages, so give one
natural Marathi example sentence that carries the same meaning, not a literal translation. Output
ONLY blocks in exactly this format, one per pattern, no extra commentary, don't skip or renumber
any pattern:

# G0xx - <short romaji pattern name>

Question
What does 「<pattern>」mean?

Answer
<short English meaning>

Marathi
<one Marathi example sentence, Devanagari script, with the same meaning as the pattern> — <its
English meaning, with a short explanation of the structural parallel to Japanese if there is one>

Example
From the source (and general N5-level knowledge if the source only has one example), give 3
Japanese example sentences graded easy / medium / hard. For each: the sentence, furigana for any
non-obvious kanji, an English translation, and a one-line note on why it illustrates the rule.
Keep all 3 within N5 grammar — vary vocabulary/length, not grammar complexity:
Easy: ...
Medium: ...
Hard: ...

Mnemonic
A short memory hook for the pattern (wordplay, sound association, or visual) — only if one
genuinely fits, don't force it.

AI Notes
The most common mistake learners make with this pattern, plus any other key point worth
remembering. 1-3 sentences.

Reference
Topics.md G0xx

---
```

Note: NotebookLM normally answers strictly from uploaded sources — the prompt above explicitly
permits general knowledge for the Marathi field, and for the medium/hard examples if the source
only supplies one example sentence per pattern.

## After each batch

```
python scripts/build_japanese_anki.py
```

`build_japanese_anki.py` scans every `*.md` file directly under `Japanese/N5/Grammar/` (not just
`cards.md`) and combines all their cards into one CSV — so a new topical file dropped into that
folder (e.g. `n5_adjectives.md`) is picked up automatically on the next run. Confirms the total
row count matches the number of `# G0xx` headings across all files, with
`Question, Answer, Marathi, Example, Mnemonic, AI Notes, Reference` columns all populated. Output
goes to `Output/japanese_n5_grammar.csv`.

**Reference field:** always cite the pattern's code from `Japanese/N5/Topics.md` specifically
(e.g. `Topics.md G047`) — not a row number from `Analysis/jlpt_n5_flashcard_checklist.md`. The two
files use different numbering; if content is sourced from the checklist instead, write
`Analysis checklist #N (jlpt_n5_flashcard_checklist.md)` so it's not mistaken for a Topics.md code.
