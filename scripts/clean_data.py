"""Create the reproducible cleaned dataset artifact."""
from pathlib import Path
from src.data_cleaning import load_and_clean_csv
source=Path("data/raw/customer_shopping_behavior.csv")
target=Path("data/processed/cleaned_customer_shopping_behavior.csv")
if not source.exists(): raise SystemExit(f"Missing {source}")
target.parent.mkdir(parents=True,exist_ok=True)
load_and_clean_csv(str(source)).to_csv(target,index=False)
print(f"Wrote {target}")
