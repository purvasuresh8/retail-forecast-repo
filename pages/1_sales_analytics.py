import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Sales Analytics")

df = pd.read_csv(
    "daily_sales_features.csv"
)

df["TransactionDate"] = pd.to_datetime(
    df["TransactionDate"]
)

# KPIs

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Revenue",
        f"${df['TransactionAmount'].sum():,.0f}"
    )

with col2:
    st.metric(
        "Average Revenue",
        f"${df['TransactionAmount'].mean():,.0f}"
    )

with col3:
    st.metric(
        "Peak Revenue",
        f"${df['TransactionAmount'].max():,.0f}"
    )

st.divider()

# Revenue Trend

fig = px.line(
    df,
    x="TransactionDate",
    y="TransactionAmount",
    title="Daily Revenue Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Monthly Revenue

monthly = (
    df
    .set_index("TransactionDate")
    .resample("M")
    .sum(numeric_only=True)
    .reset_index()
)

fig2 = px.bar(
    monthly,
    x="TransactionDate",
    y="TransactionAmount",
    title="Monthly Revenue"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
