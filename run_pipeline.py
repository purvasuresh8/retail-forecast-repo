from src.ingest import load_csv
from src.quality import remove_duplicates
from src.features import create_date_features

df = load_csv("data/raw/Retail_Data_Set.csv")
print(df.columns.tolist())
6
df = remove_duplicates(df)

df = create_date_features(df)

print(df.head())
