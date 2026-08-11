# src/ingest.py

import pandas as pd
from src.supabase_utils import insert_rows


def load_csv(filepath):
    return pd.read_csv(filepath)


def validate_columns(df, expected_columns):

    missing = [
        col
        for col in expected_columns
        if col not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing columns: {missing}"
        )

    return True


def upload_to_supabase(
        df,
        table_name,
        batch_size=500
):
    records = df.to_dict("records")

    for i in range(
        0,
        len(records),
        batch_size
    ):
        batch = records[i:i + batch_size]

        insert_rows(
            table_name,
            batch
        )

    print(
        f"Uploaded {len(records)} rows"
    )
    