from pathlib import Path
from typing import Dict, List
import re

# Maps the raw markdown header text to clean CSV column names.
HEADER_MAP = {
    "#": "No",
    "Kanji / Word": "Kanji",
    "Hiragana": "Hiragana",
    "English Meaning": "Meaning",
    "🟢 Easy": "Easy",
    "🟡 Medium": "Medium",
    "🔴 Hard": "Hard",
}


class KanjiTableParser:
    """
    Parses a markdown pipe-table (like Japanese/N5/Kanji/Kanji_Reading_N5_Table.md)
    into a list of row dictionaries, one per kanji/word entry.

    Separate from JapaneseMarkdownParser (which parses "# heading + labeled field"
    cards.md files) because this source is a plain markdown table, not a card file.
    """

    def __init__(self, markdown_file: Path):
        self.markdown_file = markdown_file

    def parse(self) -> List[Dict[str, str]]:
        text = self.markdown_file.read_text(encoding="utf-8")

        table_lines = [
            line for line in text.splitlines()
            if line.strip().startswith("|")
        ]

        if not table_lines:
            return []

        header_cells = self._split_row(table_lines[0])
        columns = [HEADER_MAP.get(cell, cell) for cell in header_cells]

        rows = []

        # table_lines[0] is the header, table_lines[1] is the "|---|---|" separator
        for line in table_lines[2:]:

            cells = self._split_row(line)

            if len(cells) != len(columns):
                continue

            row = dict(zip(columns, cells))

            # Skip placeholder rows for missing source entries, e.g. "*(no entry)*"
            if "no entry" in row.get("Kanji", "").lower():
                continue

            rows.append(row)

        return rows

    @staticmethod
    def _split_row(line: str) -> List[str]:
        line = line.strip()

        if line.startswith("|"):
            line = line[1:]

        if line.endswith("|"):
            line = line[:-1]

        return [cell.strip() for cell in line.split("|")]


def main():

    project_root = Path(__file__).resolve().parent.parent

    markdown_file = (
        project_root
        / "Japanese"
        / "N5"
        / "Kanji"
        / "Kanji_Reading_N5_Table.md"
    )

    parser = KanjiTableParser(markdown_file)

    rows = parser.parse()

    print(f"\n✓ Parsed {len(rows)} kanji entries successfully.")

    for i, row in enumerate(rows[:3], start=1):
        print("=" * 80)
        print(f"Row {i}")
        print("=" * 80)

        for key, value in row.items():
            print(f"\n{key}")
            print("-" * len(key))
            print(value)


if __name__ == "__main__":
    main()
