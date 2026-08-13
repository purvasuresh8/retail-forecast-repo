import joblib


def save_model(model, path):
    """
    Save a trained model to disk.
    """

    joblib.dump(model, path)


def load_model(path):
    """
    Load a saved model from disk.
    """

    return joblib.load(path)
    
    