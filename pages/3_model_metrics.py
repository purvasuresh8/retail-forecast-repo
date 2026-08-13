import streamlit as st
import pandas as pd
import plotly.express as px

from xgboost import XGBRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import numpy as np

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Model Metrics",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Model Performance")

# ----------------------------------
# LOAD DATA
# ----------------------------------

df = pd.read_csv(
    "daily_sales_features.csv"
)

# ----------------------------------
# FEATURES
# ----------------------------------

features = [
    "lag_1",
    "lag_7",
    "rolling_mean_7",
    "rolling_mean_30"
]

X = df[features]

y = df["TransactionAmount"]

# ----------------------------------
# TRAIN MODEL
# ----------------------------------

model = XGBRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=4,
    random_state=42
)

model.fit(X, y)

predictions = model.predict(X)

# ----------------------------------
# METRICS
# ----------------------------------

mae = mean_absolute_error(
    y,
    predictions
)

rmse = np.sqrt(
    mean_squared_error(
        y,
        predictions
    )
)

r2 = r2_score(
    y,
    predictions
)

# ----------------------------------
# KPI CARDS
# ----------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "MAE",
        f"{mae:,.0f}"
    )

with col2:
    st.metric(
        "RMSE",
        f"{rmse:,.0f}"
    )

with col3:
    st.metric(
        "R² Score",
        f"{r2:.4f}"
    )

st.divider()

# ----------------------------------
# FEATURE IMPORTANCE
# ----------------------------------

st.subheader("📊 Feature Importance")

importance_df = pd.DataFrame(
    {
        "Feature": features,
        "Importance": model.feature_importances_
    }
)

importance_df = importance_df.sort_values(
    "Importance",
    ascending=True
)

fig = px.bar(
    importance_df,
    x="Importance",
    y="Feature",
    orientation="h",
    title="XGBoost Feature Importance",
    color="Importance",
    color_continuous_scale="Blues"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------------
# FEATURE TABLE
# ----------------------------------

st.subheader("📋 Importance Values")

st.dataframe(
    importance_df.sort_values(
        "Importance",
        ascending=False
    ),
    use_container_width=True
)

# ----------------------------------
# PREDICTION COMPARISON
# ----------------------------------

st.subheader("🔍 Actual vs Predicted")

comparison_df = pd.DataFrame(
    {
        "Actual": y,
        "Predicted": predictions
    }
)

st.line_chart(
    comparison_df.head(100)
)
