# Analysis Results — Supplied Customer Shopping Dataset

## Dataset profile

- Rows: 500
- Unique customers: 500
- Columns: 19
- Missing values: 0
- Total purchase value: ₹83,676.81
- Average purchase value: ₹167.35
- Average review rating: 2.93
- Subscription rate: 49.0%
- Discount-applied rate: 47.4%

## Category distribution

| Category | Customers |
|---|---:|
| Clothing | 129 |
| Accessories | 128 |
| Footwear | 126 |
| Outerwear | 117 |

## Purchase-frequency distribution

| Frequency | Customers |
|---|---:|
| Weekly | 139 |
| Annually | 139 |
| Fortnightly | 124 |
| Monthly | 98 |

The supplied frequency labels correspond to purchase_frequency_days values of 7, 365, 14, and 30 respectively.

## Analytical interpretation

This is a cross-sectional customer snapshot, not a time-series transaction table. The repository therefore focuses on purchase-value differences, category/location/season patterns, demographic segmentation, subscription and discount behavior, purchase-frequency behavior, and the relationship between previous purchases and current purchase value.

It does not claim causal effects or supervised churn performance from this file alone.

## Reproducibility

Run scripts/clean_data.py and then streamlit run app.py. The dashboard recalculates all metrics from the supplied CSV and accepts compatible uploads.
