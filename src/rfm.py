"""Snapshot customer value and engagement-risk features."""
from __future__ import annotations
import pandas as pd

def build_snapshot_customer_metrics(df: pd.DataFrame) -> pd.DataFrame:
    out=df[["customer_id","purchase_frequency_days","previous_purchases","purchase_amount","subscription_status","review_rating"]].copy()
    out=out.rename(columns={"purchase_frequency_days":"Purchase_Interval_Days","previous_purchases":"Previous_Purchases","purchase_amount":"Purchase_Value"})
    def risk(days: float) -> str:
        if days>=180: return "High"
        if days>=30: return "Medium"
        return "Low"
    out["Engagement_Risk"]=out["Purchase_Interval_Days"].apply(risk)
    return out.sort_values(["Engagement_Risk","Purchase_Value"],ascending=[True,False]).reset_index(drop=True)

def add_risk_tier(probability: pd.Series) -> pd.Series:
    return pd.cut(probability,bins=[-float("inf"),0.33,0.66,float("inf")],labels=["Low","Medium","High"],include_lowest=True).astype("string")
