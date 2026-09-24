"""Reusable EDA transformations for customer shopping behavior."""

from __future__ import annotations

import pandas as pd


def revenue_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("category", as_index=False)["purchase_amount"]
        .sum()
        .rename(columns={"purchase_amount": "Revenue"})
        .sort_values("Revenue", ascending=False)
    )


def revenue_by_location(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("location", as_index=False)["purchase_amount"]
        .sum()
        .rename(columns={"purchase_amount": "Revenue"})
        .sort_values("Revenue", ascending=False)
    )


def revenue_by_season(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("season", as_index=False)["purchase_amount"]
        .sum()
        .rename(columns={"purchase_amount": "Revenue"})
        .sort_values("Revenue", ascending=False)
    )


def revenue_by_gender(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("gender", as_index=False)["purchase_amount"]
        .sum()
        .rename(columns={"purchase_amount": "Revenue"})
        .sort_values("Revenue", ascending=False)
    )


def purchase_frequency_summary(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["frequency_of_purchases", "purchase_frequency_days"], as_index=False)
        .agg(Customers=("customer_id", "nunique"), Revenue=("purchase_amount", "sum"))
        .sort_values("purchase_frequency_days")
    )


def kpis(df: pd.DataFrame) -> dict[str, float]:
    return {
        "total_revenue": float(df["purchase_amount"].sum()),
        "total_customers": float(df["customer_id"].nunique()),
        "average_purchase_value": float(df["purchase_amount"].mean()) if not df.empty else 0.0,
        "average_rating": float(df["review_rating"].mean()) if not df.empty else float("nan"),
        "subscription_rate": float(df["subscription_status"].mean()) if not df.empty else 0.0,
        "discount_rate": float(df["discount_applied"].mean()) if not df.empty else 0.0,
    }
