from src.model_registry import load_model

model = load_model(
    "models/xgb_forecast.pkl"
)

print("\n✅ Model loaded successfully.\n")

print(model)
