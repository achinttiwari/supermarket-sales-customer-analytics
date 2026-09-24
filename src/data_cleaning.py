"""Cleaning and validation for the supplied customer shopping dataset."""
from __future__ import annotations
import pandas as pd

BASE_COLUMNS = ["customer_id","age","gender","item_purchased","category","purchase_amount","location","size","color","season","review_rating","subscription_status","shipping_type","discount_applied","previous_purchases","payment_method","frequency_of_purchases"]
DERIVED_COLUMNS = ["age_group","purchase_frequency_days"]
CORE_COLUMNS = BASE_COLUMNS + DERIVED_COLUMNS

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    out=df.copy(); out.columns=[str(c).strip().lower() for c in out.columns]; return out

def validate_schema(df: pd.DataFrame, required: list[str] = BASE_COLUMNS) -> None:
    missing=[c for c in required if c not in df.columns]
    if missing: raise ValueError(f"Missing required columns: {', '.join(missing)}")

def _age_group(age: pd.Series) -> pd.Series:
    bins=[0,17,25,35,45,55,65,float("inf")]; labels=["Under 18","18-25","26-35","36-45","46-55","56-65","66+"]
    return pd.cut(age,bins=bins,labels=labels,include_lowest=True).astype("string")

def clean_customer_shopping_data(df: pd.DataFrame) -> pd.DataFrame:
    out=normalize_columns(df); validate_schema(out)
    for column in out.select_dtypes(include=["object","string"]).columns:
        out[column]=out[column].astype("string").str.strip()
    numeric_columns=["customer_id","age","purchase_amount","review_rating","subscription_status","discount_applied","previous_purchases","purchase_frequency_days"]
    for column in numeric_columns:
        if column in out.columns:
            out[column]=pd.to_numeric(out[column].astype("string").str.replace(r"[^0-9.\-]","",regex=True),errors="coerce")
    out=out.dropna(subset=["customer_id","purchase_amount"]).copy()
    out["customer_id"]=out["customer_id"].astype(int)
    out["subscription_status"]=out["subscription_status"].fillna(0).astype(int)
    out["discount_applied"]=out["discount_applied"].fillna(0).astype(int)
    out["previous_purchases"]=out["previous_purchases"].fillna(0).astype(int)
    out["review_rating"]=out["review_rating"].fillna(out["review_rating"].median())
    frequency_days={"Weekly":7,"Fortnightly":14,"Monthly":30,"Annually":365}
    if "purchase_frequency_days" not in out.columns:
        out["purchase_frequency_days"]=out["frequency_of_purchases"].map(frequency_days)
    else:
        out["purchase_frequency_days"]=out["purchase_frequency_days"].fillna(out["frequency_of_purchases"].map(frequency_days))
    out["purchase_frequency_days"]=out["purchase_frequency_days"].fillna(out["purchase_frequency_days"].median())
    if "age_group" not in out.columns:
        out["age_group"]=_age_group(out["age"])
    else:
        out["age_group"]=out["age_group"].fillna(_age_group(out["age"]))
    return out.drop_duplicates(subset=["customer_id"]).reset_index(drop=True)

def load_and_clean_csv(path: str) -> pd.DataFrame:
    return clean_customer_shopping_data(pd.read_csv(path))
