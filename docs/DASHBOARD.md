# Dashboard

Run streamlit run app.py.

## Controls

- CSV upload.
- Category filter.
- Location filter.
- Gender filter.

## KPIs

- Total Revenue.
- Customer Count.
- Average Purchase Value.
- Average Rating.
- Subscription Rate.

## Visuals

- Revenue by Category.
- Revenue by Location.
- Revenue by Season.
- Revenue by Purchase Frequency.
- Revenue by Gender.
- Previous Purchases vs Purchase Value.

## Customer analysis

The dashboard displays a customer engagement-risk table using purchase_frequency_days:

- Low: under 30 days.
- Medium: 30–179 days.
- High: 180 days or more.

This is a heuristic engagement indicator and not a supervised churn probability.

## Export

The customer metrics table can be downloaded as CSV.

Uploaded data always passes through the same cleaning function before analysis.
