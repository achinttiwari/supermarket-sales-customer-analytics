# Architecture

The project separates analytical logic from the Streamlit presentation layer.

## Pipeline

1. **Ingestion** — read CSV.
2. **Validation** — check required fields and normalize aliases.
3. **Cleaning** — text, dates, IDs, and numeric values.
4. **EDA** — monthly revenue, category revenue, segment revenue, branch summaries.
5. **RFM** — customer Recency, Frequency, Monetary features.
6. **Churn labeling** — historical cutoff plus future 180-day observation window.
7. **Modeling** — StandardScaler + Logistic Regression.
8. **Presentation** — Streamlit dashboard.
9. **Quality** — pytest and Ruff through GitHub Actions.

The separation allows the same analytical functions to be tested and reused outside the dashboard.
