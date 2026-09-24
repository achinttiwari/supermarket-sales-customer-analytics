# RFM & Churn

## RFM

For each Customer_ID:

- **Recency** — days since the latest historical order.
- **Frequency** — number of distinct invoices.
- **Monetary** — total historical revenue.

## Churn

The source specification defines churn as inactivity for 180+ days.

The implementation creates a leakage-safe supervised dataset:

1. Choose a historical cutoff.
2. Compute RFM features using transactions on or before that cutoff.
3. Look only at the following 180 days to create the churn label.
4. Split the labeled customer table 80/20 with stratification.
5. Train Logistic Regression using scaled RFM features.

## Risk tiers

- Low: probability < 40%
- Medium: 40% to < 70%
- High: >= 70%

The supplied guide reports reference metrics around 70.89% accuracy, 65% precision, and 84.21% recall. Those are treated as reference values rather than guaranteed results.
