import pandas as pd

from src.rfm import build_snapshot_customer_metrics


def test_snapshot_engagement_risk():
    df = pd.DataFrame(
        {
            "customer_id": [1, 2, 3],
            "purchase_frequency_days": [7, 30, 365],
            "previous_purchases": [10, 5, 2],
            "purchase_amount": [100, 200, 300],
            "subscription_status": [1, 0, 0],
            "review_rating": [4.0, 3.0, 2.0],
        }
    )
    result = build_snapshot_customer_metrics(df)
    risks = dict(zip(result.customer_id, result.Engagement_Risk.astype(str)))
    assert risks == {3: "High", 2: "Medium", 1: "Low"}
