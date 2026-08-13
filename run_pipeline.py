from src.ingest import load_csv
from src.quality import remove_duplicates
from src.features import create_date_features
from src.preprocess import (
    aggregate_daily_sales,
    create_forecast_features
)

df = load_csv("data/raw/Retail_Data_Set.csv")
print(df.columns.tolist())
6
df = remove_duplicates(df)

df = create_date_features(df)

daily_sales = aggregate_daily_sales(df)

daily_sales = create_forecast_features(
    daily_sales
)

print(daily_sales.head())
print(df.head())


daily_sales.to_csv(
    "daily_sales_features.csv",
    index=False
)