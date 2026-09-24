# Dashboard

Run:

```bash
streamlit run app.py
```

## Controls

- CSV upload.
- Branch filter when Branch exists.
- Customer Type filter.
- Date range filter.

## KPIs

- Total Revenue.
- Total Orders.
- Average Order Value.
- Average Rating when Rating exists.

## Visuals

- Monthly revenue trend.
- Revenue by Product Category.
- Customer segment revenue mix.
- Branch revenue or Rating vs Sales depending on available fields.

## Export

The dashboard provides an RFM CSV download.

## Data flow

The dashboard always passes uploaded/default data through the same cleaning function before calculating KPIs or charts. This keeps interactive analysis consistent with the documented cleaning rules.
