"""Reusable EDA transformations."""

from __future__ import annotations

import pandas as pd


def monthly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.assign(Month=df["Order_Date"].dt.to_period("M").astype(str))
        .groupby("Month", as_index=False)["Total_Sales"].sum()
        .rename(columns={"Total_Sales": "Revenue"})
    )


def revenue_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Product_Category", as_index=False)["Total_Sales"].sum().sort_values(
        "Total_Sales", ascending=False
    )


def revenue_by_customer_type(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Customer_Type", as_index=False)["Total_Sales"].sum().sort_values(
        "Total_Sales", ascending=False
    )


def branch_summary(df: pd.DataFrame) -> pd.DataFrame:
    if "Branch" not in df.columns:
        return pd.DataFrame(columns=["Branch", "Total_Sales"])
    return df.groupby("Branch", as_index=False)["Total_Sales"].sum().sort_values(
        "Total_Sales", ascending=False
    )


def kpis(df: pd.DataFrame) -> dict[str, float]:
    orders = df["Invoice_ID"].nunique()
    return {
        "total_revenue": float(df["Total_Sales"].sum()),
        "total_orders": float(orders),
        "average_order_value": float(df["Total_Sales"].sum() / orders) if orders else 0.0,
        "average_rating": float(df["Rating"].mean()) if "Rating" in df.columns else float("nan"),
    }
