from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np


def train_model(df):

    features = [
        "lag_1",
        "lag_7",
        "rolling_mean_7",
        "rolling_mean_30"
    ]

    X = df[features]
    y = df["TransactionAmount"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = XGBRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=4,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_test,
            predictions
        )
    )

    print(f"MAE : {mae:,.2f}")
    print(f"RMSE: {rmse:,.2f}")

    return model
    