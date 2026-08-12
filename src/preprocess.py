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
    