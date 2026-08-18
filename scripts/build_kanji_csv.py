from pathlib import Path

from kanji_table_parser import KanjiTableParser
from csv_exporter import CsvExporter


ROOT = Path(__file__).resolve().parent.parent

MARKDOWN_FILE = (
    ROOT
    / "Japanese"
    / "N5"
    / "Kanji"
    / "Kanji_Reading_N5_Table.md"
)

OUTPUT_FILE = (
    ROOT
    / "Output"
    / "kanji_n5_reading.csv"
)


def main():

    print("=" * 60)
    print("SynapsePro N5 Kanji Reading CSV Builder")
    print("=" * 60)

    parser = KanjiTableParser(MARKDOWN_FILE)

    rows = parser.parse()

    print(f"\nParsed {len(rows)} kanji entries")

    exporter = CsvExporter(OUTPUT_FILE)

    exporter.export(rows)

    print("\nDone!")


if __name__ == "__main__":
    main()
