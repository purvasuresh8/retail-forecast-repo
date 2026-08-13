import pandas as pd

from src.train_xgb import train_model
from src.model_registry import save_model

# Load engineered dataset

df = pd.read_csv(
    "daily_sales_features.csv"
)

# Train model

model = train_model(df)

# Save model

save_model(
    model,
    "models/xgb_forecast.pkl"
)

print("\n✅ Model saved successfully.")
print("📁 models/xgb_forecast.pkl")
