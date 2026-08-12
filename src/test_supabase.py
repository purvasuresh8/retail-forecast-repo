from src.supabase_utils import fetch_all

data = fetch_all("retail_sales")

print(data[:5])
