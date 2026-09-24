import pandas as pd
from src.rfm import build_leakage_safe_dataset

def test_leakage_safe_churn_label():
    df = pd.DataFrame({
        "Invoice_ID": ["1", "2", "3"],
        "Order_Date": pd.to_datetime(["2025-01-01", "2025-01-10", "2025-07-01"]),
        "Customer_ID": ["A", "B", "B"], "Total_Sales": [100, 50, 75],
    })
    result = build_leakage_safe_dataset(df, pd.Timestamp("2025-01-10"), churn_days=180)
    labels = dict(zip(result["Customer_ID"], result["Churn_Status"]))
    assert labels["A"] == 1
    assert labels["B"] == 0
