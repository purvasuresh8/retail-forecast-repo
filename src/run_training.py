import pandas as pd

from src.train import compare_models
from src.features import create_date_features

df = pd.read_csv("Retail_Data_Set.csv")

df = create_date_features(df)

target = "Sales"

X = df.drop(columns=[target])
y = df[target]

results = compare_models(X, y)

print(results)
