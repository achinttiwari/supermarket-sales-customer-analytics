"""Streamlit dashboard for the supplied customer shopping behavior dataset."""

from __future__ import annotations

import io

import pandas as pd
import plotly.express as px
import streamlit as st

from src.data_cleaning import clean_customer_shopping_data
from src.eda import (
    kpis,
    purchase_frequency_summary,
    revenue_by_category,
    revenue_by_gender,
    revenue_by_location,
    revenue_by_season,
)
from src.rfm import build_snapshot_customer_metrics

st.set_page_config(page_title="Customer Shopping Analytics", page_icon="📊", layout="wide")
st.title("Supermarket Sales & Customer Analytics")
st.caption(
    "Customer behavior, product performance, purchasing frequency, "
    "subscription and discount analysis"
)

uploaded = st.sidebar.file_uploader("Upload customer shopping CSV", type=["csv"])
default_path = "data/raw/customer_shopping_behavior.csv"

try:
    raw = pd.read_csv(uploaded) if uploaded is not None else pd.read_csv(default_path)
except FileNotFoundError:
    st.info("Place customer_shopping_behavior.csv in data/raw/ or upload it from the sidebar.")
    st.stop()

try:
    df = clean_customer_shopping_data(raw)
except ValueError as exc:
    st.error(str(exc))
    st.stop()

st.sidebar.header("Filters")
for column, label in [("category", "Category"), ("location", "Location"), ("gender", "Gender")]:
    options = sorted(df[column].dropna().unique())
    selected = st.sidebar.multiselect(label, options, default=options)
    df = df[df[column].isin(selected)]

if df.empty:
    st.warning("No records match the selected filters.")
    st.stop()

summary = kpis(df)
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total Revenue", f"₹{summary['total_revenue']:,.2f}")
c2.metric("Customers", f"{int(summary['total_customers']):,}")
c3.metric("Avg Purchase", f"₹{summary['average_purchase_value']:,.2f}")
c4.metric("Avg Rating", f"{summary['average_rating']:.2f}")
c5.metric("Subscription Rate", f"{summary['subscription_rate']:.1%}")

left, right = st.columns(2)
with left:
    st.plotly_chart(
        px.bar(
            revenue_by_category(df),
            x="category",
            y="Revenue",
            title="Revenue by Category",
        ),
        use_container_width=True,
    )
with right:
    st.plotly_chart(
        px.bar(
            revenue_by_location(df),
            x="location",
            y="Revenue",
            title="Revenue by Location",
        ),
        use_container_width=True,
    )

left, right = st.columns(2)
with left:
    st.plotly_chart(
        px.bar(
            revenue_by_season(df),
            x="season",
            y="Revenue",
            title="Revenue by Season",
        ),
        use_container_width=True,
    )
with right:
    st.plotly_chart(
        px.bar(
            purchase_frequency_summary(df),
            x="frequency_of_purchases",
            y="Revenue",
            title="Revenue by Purchase Frequency",
        ),
        use_container_width=True,
    )

left, right = st.columns(2)
with left:
    st.plotly_chart(
        px.pie(
            revenue_by_gender(df),
            names="gender",
            values="Revenue",
            title="Revenue by Gender",
        ),
        use_container_width=True,
    )
with right:
    st.plotly_chart(
        px.scatter(
            df,
            x="previous_purchases",
            y="purchase_amount",
            size="review_rating",
            color="subscription_status",
            hover_data=["customer_id", "category", "frequency_of_purchases"],
            title="Previous Purchases vs Purchase Value",
        ),
        use_container_width=True,
    )

st.subheader("Customer Engagement Risk")
st.caption(
    "Transparent heuristic: <30 days = Low, 30–179 days = Medium, ≥180 days = High. "
    "This is not a supervised churn prediction."
)
metrics = build_snapshot_customer_metrics(df)
st.dataframe(metrics, use_container_width=True, hide_index=True)

buffer = io.StringIO()
metrics.to_csv(buffer, index=False)
st.download_button(
    "Download Customer Metrics CSV",
    data=buffer.getvalue(),
    file_name="customer_engagement_metrics.csv",
    mime="text/csv",
)
