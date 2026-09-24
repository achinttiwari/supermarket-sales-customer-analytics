"""Streamlit dashboard for supermarket sales analytics."""

from __future__ import annotations

import io
import pandas as pd
import plotly.express as px
import streamlit as st

from src.data_cleaning import clean_transactions
from src.eda import branch_summary, kpis, monthly_revenue, revenue_by_category, revenue_by_customer_type
from src.rfm import build_rfm

st.set_page_config(page_title="Supermarket Analytics", page_icon="📊", layout="wide")
st.title("Supermarket Sales & Customer Analytics")
st.caption("Cleaning → EDA → RFM → churn-ready customer intelligence")

uploaded = st.sidebar.file_uploader("Upload supermarket CSV", type=["csv"])
try:
    raw = pd.read_csv(uploaded) if uploaded is not None else pd.read_csv("data/raw/supermarket_sales.csv")
except FileNotFoundError:
    st.info("Add data/raw/supermarket_sales.csv or upload a compatible CSV to begin.")
    st.stop()

try:
    df = clean_transactions(raw)
except ValueError as exc:
    st.error(str(exc))
    st.stop()

st.sidebar.header("Filters")
if "Branch" in df.columns:
    options = sorted(df["Branch"].dropna().unique().tolist())
    selected = st.sidebar.multiselect("Branch", options, default=options)
    df = df[df["Branch"].isin(selected)]

customer_options = sorted(df["Customer_Type"].dropna().unique().tolist())
selected_customers = st.sidebar.multiselect("Customer Type", customer_options, default=customer_options)
df = df[df["Customer_Type"].isin(selected_customers)]

min_date, max_date = df["Order_Date"].min().date(), df["Order_Date"].max().date()
date_range = st.sidebar.date_input("Date Range", (min_date, max_date), min_value=min_date, max_value=max_date)
if isinstance(date_range, tuple) and len(date_range) == 2:
    df = df[df["Order_Date"].dt.date.between(date_range[0], date_range[1])]

if df.empty:
    st.warning("No records match the selected filters.")
    st.stop()

summary = kpis(df)
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Revenue", f"₹{summary['total_revenue']:,.2f}")
c2.metric("Total Orders", f"{int(summary['total_orders']):,}")
c3.metric("Average Order Value", f"₹{summary['average_order_value']:,.2f}")
c4.metric("Average Rating", "N/A" if pd.isna(summary["average_rating"]) else f"{summary['average_rating']:.2f}")

left, right = st.columns(2)
with left:
    monthly = monthly_revenue(df)
    st.plotly_chart(px.line(monthly, x="Month", y="Revenue", markers=True, title="Monthly Revenue Trend"), use_container_width=True)
with right:
    category = revenue_by_category(df)
    st.plotly_chart(px.bar(category, x="Product_Category", y="Total_Sales", title="Revenue by Product Category"), use_container_width=True)

left, right = st.columns(2)
with left:
    customer_mix = revenue_by_customer_type(df)
    st.plotly_chart(px.pie(customer_mix, names="Customer_Type", values="Total_Sales", title="Revenue by Customer Type"), use_container_width=True)
with right:
    if "Branch" in df.columns:
        branches = branch_summary(df)
        st.plotly_chart(px.bar(branches, x="Branch", y="Total_Sales", title="Revenue by Branch"), use_container_width=True)
    elif "Rating" in df.columns:
        st.plotly_chart(px.scatter(df, x="Rating", y="Total_Sales", title="Rating vs Sales"), use_container_width=True)
    else:
        st.info("Add Branch or Rating to enable the fourth analysis chart.")

st.subheader("Customer RFM")
rfm = build_rfm(df)
st.dataframe(rfm, use_container_width=True, hide_index=True)
buffer = io.StringIO()
rfm.to_csv(buffer, index=False)
st.download_button("Download RFM CSV", data=buffer.getvalue(), file_name="rfm_customers.csv", mime="text/csv")
