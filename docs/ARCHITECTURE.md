# Architecture

The project separates analytical logic from the Streamlit presentation layer.

## Pipeline

1. Ingestion — read the supplied customer CSV.
2. Validation — check the 19-column schema.
3. Cleaning — normalize text and numeric fields.
4. EDA — category, location, season, frequency and demographic analysis.
5. Customer engagement — purchase interval, previous purchases and purchase value.
6. Risk heuristic — classify purchase-interval-based engagement risk.
7. Presentation — Streamlit dashboard.
8. Quality — pytest and Ruff through GitHub Actions.

## Modeling boundary

The supplied dataset has no purchase dates or repeated transactions per customer. Classical date-based RFM and leakage-safe 180-day churn are therefore not claimed for this dataset.

The generic Logistic Regression implementation remains reusable for a future longitudinal dataset.
