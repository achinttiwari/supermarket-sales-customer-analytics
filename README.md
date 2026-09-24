# Supermarket Sales & Customer Analytics

A reproducible customer-shopping analytics project built from the supplied CSV, with a Python cleaning/analysis pipeline and Streamlit dashboard.

## Dataset

The raw file supplied for this project contains **500 customer records and 17 columns**. Two fields are derived by the cleaning pipeline:

- `age_group`
- `purchase_frequency_days`

The snapshot has one unique `customer_id` per row. It contains no purchase date and no repeated transaction history.

### Data quality

- 500 rows
- 500 unique customers
- 26 missing `review_rating` values; the pipeline fills these with the median
- No missing values remain after cleaning
- Purchase value total: **₹83,676.81**
- Average purchase value: **₹167.35**
- Average rating: **2.93**
- Subscription rate: **49.0%**
- Discount-applied rate: **47.4%**

## Key findings

- Accessories generated ₹21,765.50 in purchase value.
- California generated ₹18,194.14 in purchase value.
- Spring generated ₹22,704.40 in purchase value.
- Weekly and annual purchasing each contain 139 customers.
- The snapshot contains 263 customers in the <30-day engagement bucket, 98 in 30–179 days, and 139 at ≥180 days.

These are descriptive observations from this dataset, not causal conclusions.

## Modeling boundary

The internship guide calls for date-based RFM and a leakage-safe 180-day churn model. This dataset cannot support either honestly because it has no transaction dates or future activity labels.

The project therefore implements a transparent engagement-risk proxy:

- **Low:** purchase interval <30 days
- **Medium:** 30–179 days
- **High:** ≥180 days

The reusable Logistic Regression implementation remains in `src/churn_model.py` for a future longitudinal dataset.

## Project structure

```
.
├── app.py
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── scripts/
├── src/
└── tests/
```

## Run locally

```bash
python -m pip install -r requirements.txt
python -m scripts.clean_data
pytest
ruff check .
streamlit run app.py
```

The dashboard loads `data/raw/customer_shopping_behavior.csv` by default and also supports CSV upload.

## Dashboard

The dashboard provides:

- KPI cards
- Category, location and gender filters
- Revenue by category, location, season, purchase frequency and gender
- Previous-purchases vs purchase-value visualization
- Customer engagement-risk table
- CSV export

## Deliverables

- Reproducible cleaning pipeline
- EDA modules
- Streamlit dashboard
- Automated tests and CI configuration
- Dataset documentation and analysis report
- Executive presentation deck

See `docs/EXECUTIVE_PRESENTATION.md` for the presentation outline and download the generated PPTX from the project workspace.

## Status

**Complete for the supplied cross-sectional dataset.** True RFM and supervised 180-day churn remain future extensions that require longitudinal transaction data.
