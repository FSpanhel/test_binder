""" Companion module for 2_structure_notebook_with_imports.ipynb.
"""
from __future__ import annotations

import sqlite3
from typing import List, Optional

import matplotlib.pyplot as plt
import pandas as pd


# %% data
def query_data_from_db(query: str, path: str) -> pd.DataFrame:
    """
    Return the result of the query 'query' from  the database 'path' as
    pd.DataFrame.
    """
    connection = sqlite3.connect(path)
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df


def transform_data(
    df: pd.DataFrame,
    columns2lower: bool = True,
    freq_col: str = "month",
    query: Optional[str] = None,
) -> pd.DataFrame:
    """
    Transforms the data.

    Args:
    - column2lower: If True, convert all columns of 'df' to lower case.
    - freq_col: Must be a string that is a valid attribute of pandas.Series.dt,
      e.g, ['month', 'day_of_week', 'hour', 'quarter', ...].
      Adds the resulting pd.Series as column to 'df'.
    - filter_row: If provided, must be a string that is consistent with
      pd.DataFrame.query.
    """
    df = df.copy()
    if columns2lower:
        df.columns = df.columns.str.lower()
    df[freq_col] = getattr(pd.to_datetime(df["start_time_agf"]).dt, freq_col)
    if query:
        df = df.query(query).copy()
    return df


def mean_target_per_group(
    df: pd.DataFrame,
    group_cols: List[str],
    target: str,
) -> pd.DataFrame:
    """
    Aggregate column 'target' of 'df' by taking the mean over 'group_cols'.
    """
    df_agg = df.groupby(group_cols)[target].mean().reset_index()
    return df_agg


# %% model
class SimpleLinearRegression:
    """Perform a simple linear regression of y on X using ordinary least-squares."""

    def fit(self, X: pd.Series, y: pd.Series) -> SimpleLinearRegression:
        nom = (X * y).mean() - X.mean() * y.mean()
        denom = (X**2).mean() - X.mean() ** 2
        self.b = nom / denom
        self.a = y.mean() - self.b * X.mean()
        return self

    def predict(self, X: pd.Series) -> pd.Series:
        return self.a + self.b * X


# %% plots
def plot(x: pd.Series, y: pd.Series):
    plt.figure()
    plt.plot(x, y, "bx")


def plot_x_vs_yy(x: pd.Series, y1: pd.Series, y2: pd.Series):
    plt.figure()
    plt.plot(x, y1, "bx")
    plt.plot(x, y2, "r-")


"""
    def plot_prediction(
        model: SimpleLinearRegression,
        x: pd.Series,
        y: Optional[pd.Series] = None
    ) -> None:
        plt.figure()
        if y is not None:
            plt.plot(x, y, "bx")
        plt.plot(x, model.predict(x), "r-")
"""
