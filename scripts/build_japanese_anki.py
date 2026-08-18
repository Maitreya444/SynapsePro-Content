from pathlib import Path

from japanese_markdown_parser import JapaneseMarkdownParser
from csv_exporter import CsvExporter


ROOT = Path(__file__).resolve().parent.parent

GRAMMAR_DIR = (
    ROOT
    / "Japanese"
    / "N5"
    / "Grammar"
)

OUTPUT_FILE = (
    ROOT
    / "Output"
    / "japanese_n5_grammar.csv"
)


def main():

    print("=" * 60)
    print("SynapsePro Japanese N5 Anki Builder")
    print("=" * 60)

    markdown_files = sorted(GRAMMAR_DIR.glob("*.md"))

    print(f"\nFound {len(markdown_files)} markdown files in {GRAMMAR_DIR}")

    cards = []

    for markdown_file in markdown_files:

        parser = JapaneseMarkdownParser(markdown_file)

        file_cards = parser.parse()

        print(f"  {markdown_file.name}: {len(file_cards)} cards")

        cards.extend(file_cards)

    print(f"\nParsed {len(cards)} cards total")

    exporter = CsvExporter(OUTPUT_FILE)

    exporter.export(cards)

    print("\nDone!")


if __name__ == "__main__":
    main()
