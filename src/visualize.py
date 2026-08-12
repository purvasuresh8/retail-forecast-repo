import matplotlib.pyplot as plt


def plot_forecast(
        y_true,
        y_pred
):

    plt.figure(
        figsize=(12,6)
    )

    plt.plot(
        y_true.values,
        label="Actual"
    )

    plt.plot(
        y_pred,
        label="Predicted"
    )

    plt.legend()

    plt.title(
        "Actual vs Forecast"
    )

    plt.show()
    