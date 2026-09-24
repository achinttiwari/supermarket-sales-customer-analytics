"""Cleaning and validation for the supplied customer shopping dataset."""

from __future__ import annotations

import pandas as pd

CORE_COLUMNS = [
    "customer_id", "age", "gender", "item_purchased", "category",
    "purchase_amount", "location", "size", "color", "season",
    "review_rating", "subscription_status", "shipping_type",
    "discount_applied", "previous_purchases", "payment_method",
    "frequency_of_purchases", "age_group", "purchase_frequency_days",
]


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out.columns = [str(c).strip().lower() for c in out.columns]
    return out


def validate_schema(df: pd.DataFrame, required: list[str] = CORE_COLUMNS) -> None:
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")


def clean_customer_shopping_data(df: pd.DataFrame) -> pd.DataFrame:
    out = normalize_columns(df)
    validate_schema(out)

    text_columns = out.select_dtypes(include=["object", "string"]).columns
    for column in text_columns:
        out[column] = out[column].astype("string").str.strip()

    numeric_columns = [
        "customer_id", "age", "purchase_amount", "review_rating",
        "subscription_status", "discount_applied", "previous_purchases",
        "purchase_frequency_days",
    ]
    for column in numeric_columns:
        out[column] = pd.to_numeric(out[column], errors="coerce")

    out = out.dropna(subset=["customer_id", "purchase_amount"]).copy()
    out["customer_id"] = out["customer_id"].astype(int)
    out["subscription_status"] = out["subscription_status"].fillna(0).astype(int)
    out["discount_applied"] = out["discount_applied"].fillna(0).astype(int)
    out["purchase_frequency_days"] = out["purchase_frequency_days"].fillna(
        out["purchase_frequency_days"].median()
    )

    return out.drop_duplicates(subset=["customer_id"]).reset_index(drop=True)


def load_and_clean_csv(path: str) -> pd.DataFrame:
    return clean_customer_shopping_data(pd.read_csv(path))
