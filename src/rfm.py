"""Customer RFM feature engineering."""

from __future__ import annotations

import pandas as pd


def build_rfm(df: pd.DataFrame, reference_date: pd.Timestamp | None = None) -> pd.DataFrame:
    if reference_date is None:
        reference_date = df["Order_Date"].max() + pd.Timedelta(days=1)

    grouped = (
        df.groupby("Customer_ID")
        .agg(
            Last_Order=("Order_Date", "max"),
            Frequency=("Invoice_ID", "nunique"),
            Monetary=("Total_Sales", "sum"),
        )
        .reset_index()
    )
    grouped["Recency"] = (reference_date - grouped["Last_Order"]).dt.days
    return grouped[["Customer_ID", "Recency", "Frequency", "Monetary", "Last_Order"]]


def build_leakage_safe_dataset(
    df: pd.DataFrame, cutoff_date: pd.Timestamp, churn_days: int = 180
) -> pd.DataFrame:
    cutoff_date = pd.Timestamp(cutoff_date)
    feature_df = df[df["Order_Date"] <= cutoff_date].copy()
    future_df = df[
        (df["Order_Date"] > cutoff_date)
        & (df["Order_Date"] <= cutoff_date + pd.Timedelta(days=churn_days))
    ].copy()

    if feature_df.empty:
        raise ValueError("No transactions exist on or before the cutoff date.")

    rfm = build_rfm(feature_df, reference_date=cutoff_date + pd.Timedelta(days=1))
    active_future = set(future_df["Customer_ID"].dropna().astype(str))
    rfm["Churn_Status"] = (~rfm["Customer_ID"].astype(str).isin(active_future)).astype(int)
    return rfm


def add_risk_tier(probability: pd.Series) -> pd.Series:
    return pd.cut(
        probability,
        bins=[-float("inf"), 0.40, 0.70, float("inf")],
        labels=["Low", "Medium", "High"],
        right=False,
    )
