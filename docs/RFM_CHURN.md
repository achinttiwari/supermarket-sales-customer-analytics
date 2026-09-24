# RFM & Churn

## Dataset limitation

The supplied CSV is a customer-level snapshot with one row per customer and no purchase date.

A valid classical RFM/churn implementation cannot manufacture last transaction date, repeated invoice history, historical monetary aggregation, or future 180-day activity labels.

## Implemented alternative

The project exposes snapshot customer metrics:

- Purchase_Interval_Days from purchase_frequency_days
- Previous_Purchases from previous_purchases
- Purchase_Value from purchase_amount
- subscription_status
- review_rating

Engagement risk is assigned as:

| Purchase interval | Risk |
|---:|---|
| < 30 days | Low |
| 30–179 days | Medium |
| ≥ 180 days | High |

This is engagement risk, not churn probability.

## Future extension

A longitudinal transaction dataset with dates can restore historical cutoff logic, true RFM features, 180-day churn labels, Logistic Regression, and probability-based risk tiers. The reusable model remains in src/churn_model.py.
