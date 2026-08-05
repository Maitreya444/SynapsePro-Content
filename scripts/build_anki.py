from pathlib import Path

from markdown_parser import MarkdownParser
from csv_exporter import CsvExporter


ROOT = Path(__file__).resolve().parent.parent

MARKDOWN_FILE = (
    ROOT
    / "DGCA"
    / "Technical Specific"
    / "01-General"
    / "cards.md"
)

OUTPUT_FILE = (
    ROOT
    / "output"
    / "chapter01.csv"
)


def main():

    print("=" * 60)
    print("SynapsePro Anki Builder")
    print("=" * 60)

    parser = MarkdownParser(MARKDOWN_FILE)

    cards = parser.parse()

    print(f"\nParsed {len(cards)} cards")

    exporter = CsvExporter(OUTPUT_FILE)

    exporter.export(cards)

    print("\nDone!")


if __name__ == "__main__":
    main()
