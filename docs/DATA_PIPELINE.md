# Data Pipeline

## Input

`data/raw/customer_shopping_behavior.csv` is the supplied 500-row, 17-column customer-level snapshot.

## Transformations

1. Normalize column names.
2. Strip whitespace from text values.
3. Parse numeric fields, including currency-formatted purchase values.
4. Remove rows missing `customer_id` or `purchase_amount`.
5. Fill missing binary flags with zero.
6. Fill missing previous-purchase counts with zero.
7. Fill missing review ratings with the median.
8. Derive `purchase_frequency_days` using Weekly=7, Fortnightly=14, Monthly=30, Annually=365.
9. Derive `age_group` from age.
10. Remove duplicate customer IDs.

The supplied file has 26 missing review ratings; no other missing values are present.

## Output

`python -m scripts.clean_data` writes:

`data/processed/cleaned_customer_shopping_behavior.csv`

The cleaned artifact contains 19 columns and 500 rows.
