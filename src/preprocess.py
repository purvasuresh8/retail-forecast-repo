import pandas as pd


def aggregate_daily_sales(df):

    daily_sales = (
        df.groupby("TransactionDate")
        .agg(
            {
                "TransactionAmount": "sum"
            }
        )
        .reset_index()
        .sort_values("TransactionDate")
    )
    

    return daily_sales
    
def create_forecast_features(df):

    df["day_of_week"] = (
        df["TransactionDate"]
        .dt.dayofweek
    )

    df["month"] = (
        df["TransactionDate"]
        .dt.month
    )

    df["quarter"] = (
        df["TransactionDate"]
        .dt.quarter
    )

    df["lag_1"] = df["TransactionAmount"].shift(1)
    df["lag_7"] = df["TransactionAmount"].shift(7)
    df["lag_30"] = df["TransactionAmount"].shift(30)

    df["rolling_mean_7"] = (
        df["TransactionAmount"]
        .rolling(7)
        .mean()
    )

    df["rolling_mean_30"] = (
        df["TransactionAmount"]
        .rolling(30)
        .mean()
    )

    return df.dropna()