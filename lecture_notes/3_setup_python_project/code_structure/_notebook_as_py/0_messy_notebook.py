# ---
# jupyter:
#   jupytext:
#     comment_magics: false
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python [conda env:improcast]
#     language: python
#     name: conda-env-improcast-py
# ---

# %%
import sys
import os
import sqlite3

import pandas as pd

connection = sqlite3.connect("../../../data/dsc.db")
cursor = connection.cursor()

def execute_query(query: str):
    return pd.read_sql_query(query, connection)

movies = execute_query(f"""
SELECT *
FROM broadcast
WHERE genre = 'Spielfilm'
    AND start_time_agf >= '2018-01-01'
    AND end_time_agf <= '2018-12-31'
""")

# %%
movies

# %%
movies.columns = movies.columns.str.lower()

# %%
movies['month'] = pd.to_datetime(movies['start_time_agf']).dt.month

# %%
movies = movies.query("channel == 'RTL'")

# %%
mean_duration_per_month = (
    movies
    .groupby(['month'])
    ['duration']
    .mean()
    .reset_index())

# %%
mean_duration_per_month

# %%
import matplotlib.pyplot as plt
plt.figure();
plt.plot(mean_duration_per_month['month'], mean_duration_per_month['duration'], "bx");

# %%
y = mean_duration_per_month['duration']
X = mean_duration_per_month['month']

# %%
from __future__ import annotations

class SimpleLinearRegression:
    """ Perform a simple linear regression of y on X using ordinary least-squares.
    """
    def fit(self, X: pd.Series, y: pd.Series) -> SimpleLinearRegression:
        nom = (X * y).mean() - X.mean() * y.mean()
        denom = (X ** 2).mean() - X.mean() ** 2
        self.b = nom / denom
        self.a = y.mean() - self.b * X.mean()
        return self
        
    def predict(self, X: pd.Series) -> pd.Series:
        return self.a + self.b * X


# %%
slr = SimpleLinearRegression().fit(X, y)

# %%
in_sample_pred = slr.predict(X)

# %%
import matplotlib.pyplot as plt
plt.figure();
plt.plot(mean_duration_per_month['month'], mean_duration_per_month['duration'], "bx");
plt.plot(mean_duration_per_month['month'], in_sample_pred, "r-");

# %%
y_13 = slr.predict(pd.Series([3]))
print(f"Mean duration for the 13th month is {round(y_13.squeeze()/ (60))} minutes.")

# %%
in_sample_pred.to_csv("prediction.csv", index=False)
