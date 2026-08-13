import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from xgboost import XGBRegressor

st.title("🔮 Forecasting")

df = pd.read_csv(
    "daily_sales_features.csv"
)

features = [
    "lag_1",
    "lag_7",
    "rolling_mean_7",
    "rolling_mean_30"
]

X = df[features]
y = df["TransactionAmount"]

model = XGBRegressor()

model.fit(X, y)

predictions = model.predict(X)

forecast_df = pd.DataFrame(
    {
        "Actual": y,
        "Prediction": predictions
    }
)

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        y=forecast_df["Actual"],
        mode="lines",
        name="Actual"
    )
)

fig.add_trace(
    go.Scatter(
        y=forecast_df["Prediction"],
        mode="lines",
        name="Predicted"
    )
)

fig.update_layout(
    title="Actual vs Predicted Sales"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.success(
    "Forecasting model successfully generated predictions."
)
