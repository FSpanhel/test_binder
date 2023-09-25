# ---
# jupyter:
#   jupytext:
#     comment_magics: false
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python [conda env:dsc] *
#     language: python
#     name: conda-env-dsc-py
# ---

# %% [markdown]
# - In order to use the table of contents, you have to install the Jupyter contributed extensions into your pyscaffold_test environment by running  
# ```conda install -n pyscaffold_test jupyter_contrib_nbextensions```.
# - If your notebook server is running, shut down the notebook server and start a new one so that the extension can be activated.
# - On the starting page of Jupyter notebook, have a look at the menu at the top and click on <a style="background-color:yellow;">Nbextensions</a>.

# %% [markdown]
# <div align="left">
# <img src="../figures/0_toc.png" alt="VC" width=700/>
# <div/>

# %% [markdown]
# - Deactivate the first box.
# - Activate the extension <a style="background-color:yellow;">Table Of Contents (2)</a>.

# %% [markdown]
# <div align="left">
# <img src="../figures/1_toc.png" alt="VC" width=700/>
# <div/>

# %% [markdown]
# # Setup

# %% [markdown]
# ## Imports

# %%
from __future__ import annotations
import sys
import os
import sqlite3
from typing import Tuple, List

import pandas as pd
import matplotlib.pyplot as plt


# %% [markdown]
# ## Functions

# %% [markdown]
# ### execute_query

# %%
def execute_query(query: str):
    return pd.read_sql_query(query, connection)


# %% [markdown]
# ### SimpleLinearRegression

# %%
class SimpleLinearRegression:
    """ Perform a simple linear regression of y on X using ordinary least-squares.
    """
    def fit(self, X: pd.Series, y: pd.Series) -> SimpleLinearRegression:
        nom = (X * y).mean() - X.mean() * y.mean()   # \bar{xy} - \bar{x}\bar{y}
        denom = (X ** 2).mean() - X.mean() ** 2   # \bar{xx} - \bar{x}^2
        self.b = nom / denom
        self.a = y.mean() - self.b * X.mean()  # \bar{y} - b \bar{x}
        return self
        
    def predict(self, X: pd.Series):
        return self.a + self.b * X


# %% [markdown]
# # Parameters

# %% [markdown]
# ## Data

# %% [markdown]
# ### Database connection

# %%
connection = sqlite3.connect("../../../data/dsc.db")
cursor = connection.cursor()

# %% [markdown]
# ### Sql query

# %%
sql_query = """
SELECT *
FROM broadcast
WHERE genre = 'Spielfilm'
    AND start_time_agf >= '2018-01-01'
    AND end_time_agf <= '2018-12-31'
"""

# %% [markdown]
# ### Pd query

# %%
pd_query = "channel == 'RTL'"

# %% [markdown]
# ### Target

# %%
target = 'duration'

# %% [markdown]
# ### Feature

# %%
feature = 'month'

# %% [markdown]
# ### Output

# %%
output = "prediction.csv"

# %% [markdown]
# ## Model

# %% [markdown]
# ### Model class

# %%
Model = SimpleLinearRegression

# %% [markdown]
# # Data

# %% [markdown]
# ## Load

# %%
movies = execute_query(sql_query)

# %%
movies

# %% [markdown]
# ## Mutate

# %%
movies.columns = movies.columns.str.lower()

# %%
movies[feature] = pd.to_datetime(movies['start_time_agf']).dt.month

# %% [markdown]
# ## Filter

# %%
movies = movies.query(pd_query)

# %% [markdown]
# ## Aggregate

# %%
mean_duration_per_month = (
    movies
    .groupby([feature])
    [target]
    .mean()
    .reset_index())

# %%
mean_duration_per_month

# %% [markdown]
# ## Visualize

# %%
plt.figure();
plt.plot(mean_duration_per_month[feature], mean_duration_per_month[target], "bx");

# %% [markdown]
# # Model

# %% [markdown]
# ## Fit

# %%
y = mean_duration_per_month[target]
X = mean_duration_per_month[feature]

# %%
model = Model().fit(X, y)

# %% [markdown]
# ## Predict in-sample

# %%
in_sample_pred = model.predict(X)

# %% [markdown]
# ## Visualize

# %%
plt.figure();
plt.plot(mean_duration_per_month[feature], mean_duration_per_month[target], "bx");
plt.plot(mean_duration_per_month[feature], in_sample_pred, "r-");

# %% [markdown]
# ## Predict out-of-sample

# %%
y_13 = model.predict(pd.Series([3]))
print(f"Mean {target} for the 13th month is {round(y_13.squeeze()/ (60))} minutes.")

# %% [markdown]
# # Export in-sample predictions

# %%
in_sample_pred.to_csv(output, index=False)
