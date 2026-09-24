"""Explain why supervised churn training is not run for the supplied snapshot."""

raise SystemExit(
    "The supplied customer shopping CSV is a single customer-level snapshot with no "
    "purchase dates or repeated transaction history. A leakage-safe 180-day churn label "
    "cannot be created without inventing future observations. Use src/churn_model.py "
    "with a longitudinal transaction dataset when one is available."
)
