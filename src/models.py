# src/models.py

from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor


def random_forest_model():
    return RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )


def xgboost_model():
    return XGBRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=6,
        random_state=42
    )