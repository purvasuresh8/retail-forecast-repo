# src/quality.py

import pandas as pd


def remove_duplicates(df):

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print(
        f"Removed {before-after} duplicates"
    )

    return df


def handle_missing_values(df):

    numeric_cols = (
        df.select_dtypes(include="number")
        .columns
    )

    df[numeric_cols] = (
        df[numeric_cols]
        .fillna(
            df[numeric_cols].median()
        )
    )

    return df


def validate_sales(df):

    if "Sales" in df.columns:

        negatives = (
            df["Sales"] < 0
        ).sum()

        print(
            f"Negative sales rows: {negatives}"
        )

    return df
    