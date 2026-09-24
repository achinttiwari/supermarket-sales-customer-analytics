# RFM & Churn

## Why classical RFM is not computed

Classical RFM needs transaction dates and repeated customer activity to calculate:

- Recency: time since last transaction
- Frequency: transaction count over a defined period
- Monetary: monetary value over a defined period

The supplied dataset has one row per customer and no transaction date, so these quantities cannot be reconstructed without inventing information.

## Implemented alternative

The dashboard uses:

- Purchase interval from `frequency_of_purchases`
- Previous purchases
- Current purchase value
- Subscription status
- Review rating

A transparent engagement-risk heuristic is applied:

| Purchase interval | Risk |
|---:|---|
| <30 days | Low |
| 30–179 days | Medium |
| ≥180 days | High |

This is **not** a churn probability and should not be presented as a trained classifier.

## Reusable model

`src/churn_model.py` contains a leakage-safe Logistic Regression pipeline for a future longitudinal dataset with `Recency`, `Frequency`, `Monetary`, and a valid future `Churn_Status` label.

## Required future data

To implement the guide's 180-day churn model, collect transaction-level records containing at least:

- Customer ID
- Transaction date
- Transaction value

Then define a historical cutoff and generate the future inactivity label without leakage.
