# Supermarket Sales & Customer Analytics

[![CI](https://github.com/achinttiwari/supermarket-sales-customer-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/achinttiwari/supermarket-sales-customer-analytics/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/App-Streamlit-red)](https://streamlit.io/)

End-to-end supermarket analytics: cleaning, EDA, RFM customer analysis, leakage-safe churn prediction, and an interactive Streamlit dashboard.

> The project specification describes a 500-row supermarket dataset, but the CSV itself was not supplied. Place the real `supermarket_sales.csv` in `data/raw/` before running the full pipeline.

## Goals

- Reproducible transaction-data cleaning.
- Business-oriented EDA and insight generation.
- RFM customer aggregation.
- Leakage-safe 180-day churn labeling.
- Logistic Regression churn prediction.
- High / Medium / Low risk tiers.
- Interactive Streamlit dashboard.
- Automated tests and GitHub Actions CI.

## Architecture

```
CSV → Validation → Cleaning → EDA
                         ↓
                  Customer RFM
                         ↓
             Historical cutoff + future label
                         ↓
                Logistic Regression
                         ↓
                   Risk tiers
                         ↓
                 Streamlit dashboard
```

## Quick start

```bash
git clone https://github.com/achinttiwari/supermarket-sales-customer-analytics.git
cd supermarket-sales-customer-analytics
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

Put the supplied CSV at:

```
data/raw/supermarket_sales.csv
```

Run:

```bash
streamlit run app.py
```

Test:

```bash
pytest
ruff check .
```

## Data contract

Required columns:

- Invoice_ID
- Order_Date
- Customer_ID
- Customer_Type
- Gender
- Product_Category
- Unit_Price
- Quantity
- Total_Sales

The dashboard also supports Branch and Rating when present. Product_Line is accepted as an alias for Product_Category.

## Churn methodology

Churn is inactivity for at least 180 days. Features are calculated only from records on or before a historical cutoff; the subsequent observation window creates the label. This prevents future transactions from leaking into model features.

The supplied specification reports reference metrics of approximately 70.89% accuracy, 65% precision, and 84.21% recall. Those values are not assumed to reproduce without the original dataset.

## Documentation

- [Project specification](docs/PROJECT_SPECIFICATION.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Data dictionary](docs/DATA_DICTIONARY.md)
- [Data pipeline](docs/DATA_PIPELINE.md)
- [EDA](docs/EDA.md)
- [RFM & churn](docs/RFM_CHURN.md)
- [Dashboard](docs/DASHBOARD.md)
- [Development](docs/DEVELOPMENT.md)
- [Deployment](docs/DEPLOYMENT.md)

## Status

| Component | Status |
|---|---|
| Repository foundation | Complete |
| Cleaning | Complete |
| EDA | Complete |
| RFM | Complete |
| Churn model | Complete |
| Streamlit dashboard | Complete |
| Tests | Complete |
| CI | Complete |
| Real-dataset validation | Pending CSV |
