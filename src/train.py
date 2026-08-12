import pandas as pd

from src.models import (
    random_forest_model,
    xgboost_model
)

from src.evaluate import (
    evaluate_model
)

from sklearn.model_selection import (
    train_test_split
)


def compare_models(X, y):

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )
    )

    models = {
        "RandomForest":
            random_forest_model(),

        "XGBoost":
            xgboost_model()
    }

    results = []

    for name, model in models.items():

        model.fit(
            X_train,
            y_train
        )

        preds = model.predict(
            X_test
        )

        metrics = evaluate_model(
            y_test,
            preds
        )

        metrics["Model"] = name

        results.append(metrics)

    return pd.DataFrame(results)
    