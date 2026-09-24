# Data Pipeline

## Cleaning rules

The source specification calls for:

- TRIM/CLEAN-style text normalization.
- Date validation.
- Missing Customer_ID → C000.
- Removal of currency symbols, spaces, and separators before numeric conversion.
- Mean-based filling for missing numerical values.

The implementation performs deterministic versions of these transformations.

## Schema handling

The source material uses both Product_Line and Product_Category in different sections. The implementation canonicalizes Product_Line to Product_Category.

The raw CSV should remain outside version control. Generated cleaned data belongs in data/processed/.
