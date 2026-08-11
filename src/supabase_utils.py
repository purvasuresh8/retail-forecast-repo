# src/supabase_utils.py

from supabase import create_client
from src.config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


def get_supabase():
    return supabase


def insert_rows(table_name, records):
    response = (
        supabase
        .table(table_name)
        .insert(records)
        .execute()
    )

    return response


def fetch_all(table_name):
    response = (
        supabase
        .table(table_name)
        .select("*")
        .execute()
    )

    return response.data
    