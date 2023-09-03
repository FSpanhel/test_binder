"""
Model classes and instance loading and storage.

- Provides SimpleLinearRegression that can be fitted to data and predict data.
- Moreover, stores and loads SimpleLinearRegression using pickle.
"""
from __future__ import annotations

import os
import pickle

import numpy as np
import numpy.typing as npt
import pandas as pd


class SimpleLinearRegression:
    """
    Simple linear regression using ordinary least-squares.

    - Note that a simple linear regression uses only one feature.
    - Its methods .fit and .predict use the Scikit-Learn API.

    Attributes:
        a: Intercept. Updated during .fit().
        b: Slope. Updated during .fit().
    """

    def __init__(self):
        self.a: float = np.nan
        self.b: float = np.nan

    def fit(self, X: pd.Series[float], y: pd.Series[float]) -> SimpleLinearRegression:
        """
        Regresses y on X using ordinary least-squares.

        Updates the attributes a and b.

        Args:
            y: Target values.
            X: Feature values.

        Returns:
            The class instance.
        """
        nom = (X * y).mean() - X.mean() * y.mean()
        denom = (X**2).mean() - X.mean() ** 2  # type: ignore  # (X ** object) raises an error because, according to the type annotation, object must be a pd.Series. However, a scalar also works so I rather ignore this type warning instead of writing X ** pd.Series([2] *  X.shape[0]) # noqa # fmt: skip
        self.b = nom / denom
        self.a = y.mean() - self.b * X.mean()
        return self

    def predict(self, X: pd.Series[float]) -> npt.NDArray[np.float64]:
        """
        Predicts the target using the fitted model and X.

        Args:
            X: Feature values.

        Returns:
            Predicted target values.
        """
        prediction: pd.Series[float] = self.a + self.b * X  # type: ignore  # see previous ignore  # noqa
        # prediction.name = 'prediction'
        prediction_np = prediction.to_numpy(dtype=float).squeeze()
        return prediction_np


def store_model(model: SimpleLinearRegression, path: str) -> None:
    """
    Pickles 'model' as 'path'.
    """
    folder = os.path.dirname(path)
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(path, "wb") as model_storage:
        pickle.dump(model, model_storage)
    print(f"> Stored model in {os.path.abspath(path)}")


def load_model(path: str) -> SimpleLinearRegression:
    """
    Loads 'model' from 'path'.
    """
    with open(path, "rb") as model_storage:
        model = pickle.load(model_storage)
    print(f"> Loaded model from {path}")
    return model


def store_prediction(prediction: npt.NDArray[np.float64], path: str) -> None:
    pd.Series(prediction).rename("prediction").to_csv(path, index=False)  # type: ignore  # false positive which is raised because pandas uses internally pd._typing.FilePath as type for path but this is not recognized by the public pandas-stubs # noqa # fmt: skip
    print(f"> Predictions are stored in {path}")
