# Data Pipeline

## Input

The supplied customer shopping behavior CSV is a 500-row, 19-column customer-level snapshot.

## Cleaning

The implementation:

1. Normalizes column names.
2. Strips whitespace from text fields.
3. Converts numeric fields to numeric types.
4. Removes rows missing customer_id or purchase_amount.
5. Fills missing binary flags with zero.
6. Fills missing purchase-frequency intervals with the column median.
7. Removes duplicate customer_id records.

The supplied file currently has no missing values, so the imputation paths are defensive rather than observed corrections.

## Output

scripts/clean_data.py writes a cleaned copy to data/processed/cleaned_customer_shopping_behavior.csv.

The raw CSV is treated as a local input and is not fabricated into the repository.
