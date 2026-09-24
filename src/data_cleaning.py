"""Schema validation and deterministic transaction-data cleaning."""

from __future__ import annotations

from typing import Iterable

import pandas as pd

CORE_COLUMNS = [
    "Invoice_ID", "Order_Date", "Customer_ID", "Customer_Type", "Gender",
    "Product_Category", "Unit_Price", "Quantity", "Total_Sales",
]

ALIASES = {
    "Product_Line": "Product_Category",
    "Invoice ID": "Invoice_ID",
    "Customer ID": "Customer_ID",
    "Order Date": "Order_Date",
    "Customer Type": "Customer_Type",
    "Unit Price": "Unit_Price",
    "Total Sales": "Total_Sales",
}


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out.columns = [str(c).strip() for c in out.columns]
    return out.rename(columns={k: v for k, v in ALIASES.items() if k in out.columns})


def validate_schema(df: pd.DataFrame, required: Iterable[str] = CORE_COLUMNS) -> None:
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")


def _clean_numeric(series: pd.Series) -> pd.Series:
    cleaned = (
        series.astype("string")
        .str.replace(r"[^0-9.\-]", "", regex=True)
        .replace("", pd.NA)
    )
    return pd.to_numeric(cleaned, errors="coerce")


def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    out = normalize_columns(df)
    validate_schema(out)

    for column in out.select_dtypes(include=["object", "string"]).columns:
        out[column] = out[column].astype("string").str.strip()

    out["Order_Date"] = pd.to_datetime(out["Order_Date"], errors="coerce")
    out["Customer_ID"] = out["Customer_ID"].fillna("C000").replace("", "C000")

    for column in ["Unit_Price", "Quantity", "Total_Sales"]:
        out[column] = _clean_numeric(out[column])
        if out[column].isna().any():
            out[column] = out[column].fillna(out[column].mean())

    return out.dropna(subset=["Order_Date"]).reset_index(drop=True)


def load_and_clean_csv(path: str) -> pd.DataFrame:
    return clean_transactions(pd.read_csv(path))
