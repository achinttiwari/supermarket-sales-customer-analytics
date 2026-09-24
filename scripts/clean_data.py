"""Clean the supplied supermarket CSV into data/processed/."""
from pathlib import Path
from src.data_cleaning import load_and_clean_csv

source = Path("data/raw/supermarket_sales.csv")
target = Path("data/processed/cleaned_supermarket_sales.csv")

if not source.exists():
    raise SystemExit("Missing data/raw/supermarket_sales.csv")

target.parent.mkdir(parents=True, exist_ok=True)
load_and_clean_csv(str(source)).to_csv(target, index=False)
print(f"Wrote {target}")
