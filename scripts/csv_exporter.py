from pathlib import Path

import pandas as pd


class CsvExporter:

    def __init__(self, output_file: Path):
        self.output_file = output_file

    def export(self, cards):

        df = pd.DataFrame(cards)

        if "Title" in df.columns:
            df = df.drop(columns=["Title"])

        self.output_file.parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(
            self.output_file,
            index=False,
            encoding="utf-8-sig",
        )

        print(f"\nCSV exported successfully")

        print(self.output_file)


def main():

    sample_cards = [
        {
            "Question": "Sample Question",
            "Answer": "Sample Answer",
            "Explanation": "Explanation",
            "Diagram": "",
            "Mnemonic": "",
            "Formula": "",
            "Reference": "",
            "Related": "",
            "AI Notes": "",
        }
    ]

    output = Path("sample.csv")

    exporter = CsvExporter(output)

    exporter.export(sample_cards)


if __name__ == "__main__":
    main()
