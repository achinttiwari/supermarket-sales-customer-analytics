# Supermarket Sales & Customer Analytics

End-to-end customer shopping analytics using the supplied 500-row customer shopping behavior CSV, Python, Plotly, and Streamlit.

## Dataset used

The supplied file contains 500 customers and 19 fields. It is a customer-level snapshot: each customer_id is unique and there is no transaction date or multi-period transaction history.

Core fields include customer demographics, product behavior, purchase value, location, season, ratings, subscriptions, discounts, payment method and purchase-frequency behavior.

### Dataset snapshot

| Metric | Value |
|---|---:|
| Customers | 500 |
| Total purchase value | ₹83,676.81 |
| Average purchase value | ₹167.35 |
| Average review rating | 2.93 |
| Subscription rate | 49.0% |
| Discount-applied rate | 47.4% |

## Modeling decision

The original project guide describes date-based RFM and a leakage-safe 180-day churn model. This supplied CSV does not contain purchase dates or repeated transactions per customer, so classical Recency and supervised 180-day churn cannot be calculated without inventing information.

The repository therefore uses a transparent Customer Engagement Risk heuristic:

- Low: purchase interval < 30 days
- Medium: 30–179 days
- High: ≥ 180 days

This is a behavioral risk indicator, not a trained churn prediction model.

The generic Logistic Regression module remains available for a future longitudinal transaction dataset.

## Quick start

Clone the repository, place customer_shopping_behavior_cleaned.csv in data/raw/, install requirements, run scripts/clean_data.py, then run streamlit run app.py.

Tests: pytest
Lint: ruff check .

## Dashboard

The Streamlit app provides total revenue, customer count, average purchase value, average rating, subscription rate, revenue by category/location/season/frequency/gender, previous-purchases vs purchase-value analysis, customer engagement risk, CSV export, and upload support.

## Status

| Component | Status |
|---|---|
| Supplied CSV schema integration | Complete |
| Cleaning | Complete |
| EDA | Complete |
| Customer engagement analysis | Complete |
| Streamlit dashboard | Complete |
| Tests | Complete |
| CI | Configured |
| Classical time-based RFM | Not applicable to snapshot |
| 180-day supervised churn | Requires longitudinal transaction data |
| Executive presentation | Pending |
