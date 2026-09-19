from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_ROOT / "data" / "raw_original"


def profile_csv(file_path: Path) -> None:
    df = pd.read_csv(file_path)

    print("=" * 80)
    print(f"FILE: {file_path.name}")
    print(f"ROWS: {len(df):,}")
    print(f"COLUMNS: {len(df.columns)}")
    print()
    print("COLUMN NAMES:")
    print(df.columns.tolist())
    print()
    print("NULL VALUES:")
    print(df.isna().sum().sort_values(ascending=False).head(10))
    print()


def main() -> None:
    csv_files = sorted(RAW_DIR.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {RAW_DIR}")

    for file_path in csv_files:
        profile_csv(file_path)


if __name__ == "__main__":
    main()
