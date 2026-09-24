# Project Specification

## Objective

Implement the supplied IBM Bob IDE & AI Data Analytics Internship Guide against the actual customer shopping CSV provided for this project.

## Scope

1. Load and validate the supplied customer shopping dataset.
2. Clean and standardize the data.
3. Perform descriptive EDA and business segmentation.
4. Build a Streamlit dashboard.
5. Provide customer engagement analysis.
6. Preserve a reusable architecture for future RFM/churn modeling.
7. Produce reproducible documentation and an executive presentation.

## Dataset-specific adaptation

The supplied raw CSV contains 17 fields. The pipeline derives `age_group` from age and `purchase_frequency_days` from the categorical frequency field.

The source guide's date-based RFM and 180-day churn specification cannot be reproduced from this snapshot without inventing transaction dates or future observations. The implementation explicitly documents that boundary rather than fabricating model performance.

## Deliverables

- Raw supplied CSV as project input
- Reproducible cleaned CSV
- Data dictionary
- EDA documentation
- Streamlit dashboard
- Engagement-risk customer table
- Reusable leakage-safe Logistic Regression module
- Automated tests and CI
- Executive presentation
