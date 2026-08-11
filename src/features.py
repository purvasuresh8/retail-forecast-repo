# src/features.py

import pandas as pd


def create_date_features(
        df,
        date_col="Date"
):

    df[date_col] = pd.to_datetime(
        df[date_col]
    )

    df["year"] = (
        df[date_col].dt.year
    )

    df["month"] = (
        df[date_col].dt.month
    )

    df["week"] = (
        df[date_col].dt.isocalendar().week
    )

    df["day_of_week"] = (
        df[date_col].dt.dayofweek
    )

    return df


def create_lag_features(
        df,
        target_col="Sales"
):

    df["sales_lag_1"] = (
        df[target_col].shift(1)
    )

    df["sales_lag_7"] = (
        df[target_col].shift(7)
    )

    return df


def create_rolling_features(
        df,
        target_col="Sales"
):

    df["rolling_mean_7"] = (
        df[target_col]
        .rolling(7)
        .mean()
    )

    df["rolling_mean_30"] = (
        df[target_col]
        .rolling(30)
        .mean()
    )

    return df
    