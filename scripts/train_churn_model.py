"""Train the leakage-safe churn model from the cleaned transaction CSV."""
from pathlib import Path
import pandas as pd

from src.data_cleaning import clean_transactions
from src.rfm import build_leakage_safe_dataset
from src.churn_model import train_churn_model

source = Path("data/processed/cleaned_supermarket_sales.csv")
if not source.exists():
    raise SystemExit("Run scripts/clean_data.py first.")

df = clean_transactions(pd.read_csv(source))
max_date = df["Order_Date"].max()
cutoff = max_date - pd.Timedelta(days=180)
labeled = build_leakage_safe_dataset(df, cutoff)
result = train_churn_model(labeled)

print("Cutoff:", cutoff.date())
for name, value in result.metrics.items():
    print(f"{name}: {value:.4f}")

Path("data/processed").mkdir(exist_ok=True)
result.predictions.to_csv("data/processed/churn_predictions.csv", index=False)
print("Wrote data/processed/churn_predictions.csv")
