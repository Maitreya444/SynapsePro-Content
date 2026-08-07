from pathlib import Path
from typing import Dict, List
import re

FIELDS = [
    "Question",
    "Answer",
    "Explanation",
    "Diagram",
    "Mnemonic",
    "Formula",
    "Reference",
    "Related",
    "AI Notes",
]


class MarkdownParser:
    """
    Parses SynapsePro cards.md files into Python dictionaries.
    """

    def __init__(self, markdown_file: Path):
        self.markdown_file = markdown_file

    def parse(self) -> List[Dict[str, str]]:
        text = self.markdown_file.read_text(encoding="utf-8")

        # Split only on level-1 headings
        sections = re.split(r"^#\s+", text, flags=re.MULTILINE)

        cards = []

        for section in sections:

            section = section.strip()

            if not section:
                continue

            lines = section.splitlines()

            title = lines[0].strip()

            body = "\n".join(lines[1:])

            # Skip anything that isn't actually a card
            if "Question" not in body or "Answer" not in body:
                continue

            card = self._extract_fields(body)

            card["Title"] = title

            cards.append(card)

        return cards

    def _extract_fields(self, body: str) -> Dict[str, str]:
        result = {}

        for i, field in enumerate(FIELDS):
            start = body.find(field)

            if start == -1:
                result[field] = ""
                continue

            start += len(field)

            end = len(body)

            for next_field in FIELDS[i + 1:]:
                idx = body.find(next_field, start)

                if idx != -1:
                    end = idx
                    break

            value = body[start:end].strip()

            result[field] = value

        return result


def main():

    project_root = Path(__file__).resolve().parent.parent

    markdown_file = (
        project_root
        / "DGCA"
        / "Technical Specific"
        / "01-General"
        / "cards.md"
    )

    parser = MarkdownParser(markdown_file)

    cards = parser.parse()

    print(f"\n✓ Parsed {len(cards)} cards successfully.")

    for i, card in enumerate(cards, start=1):
        print("=" * 80)
        print(f"Card {i}: {card['Title']}")
        print("=" * 80)

        for key, value in card.items():
            if key != "Title":
                print(f"\n{key}")
                print("-" * len(key))
                print(value)

    print("\nCards found:")

    for i, card in enumerate(cards, start=1):
        print(f"{i:02}. {card['Title']}")

if __name__ == "__main__":
    main()
