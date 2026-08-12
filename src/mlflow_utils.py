import mlflow


def log_experiment(
        model_name,
        rmse,
        mae
):

    with mlflow.start_run():

        mlflow.log_param(
            "model",
            model_name
        )

        mlflow.log_metric(
            "rmse",
            rmse
        )

        mlflow.log_metric(
            "mae",
            mae
        )
