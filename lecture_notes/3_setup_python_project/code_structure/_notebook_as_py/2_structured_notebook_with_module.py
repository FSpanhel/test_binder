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

# %% [markdown]
# # Setup

# %% [markdown]
# ## Imports

# %%
import pandas as pd

from companion_module import (
    query_data_from_db,
    transform_data,
    mean_target_per_group,
    SimpleLinearRegression,
    plot,
    plot_x_vs_yy)

# %% [markdown]
# # Parameters

# %% [markdown]
# ## Data

# %% [markdown]
# ### Database connection

# %%
path2db = "../../../data/dsc.db"

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
pd_query = "channel in 'RTL'"

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
df = query_data_from_db(sql_query, path2db)

# %%
df

# %% [markdown]
# ## Transform

# %%
df = transform_data(
    df,
    columns2lower=True,
    freq_col=feature,
    query=pd_query)

# %% [markdown]
# ## Aggregate

# %%
mean_duration_per_month = mean_target_per_group(
    df,
    group_cols=feature,
    target=target)

# %%
mean_duration_per_month

# %% [markdown]
# ## Visualize

# %%
plot(mean_duration_per_month[feature], mean_duration_per_month[target])

# %% [markdown]
# # Model

# %% [markdown]
# ## Fit

# %%
y = mean_duration_per_month[feature]
X = mean_duration_per_month[target]

# %%
model = Model().fit(X, y)

# %% [markdown]
# ## Predict in-sample

# %%
in_sample_pred = model.predict(X)

# %% [markdown]
# ## Visualize

# %%
plot_x_vs_yy(X, y, in_sample_pred)

# %% [markdown]
# ## Predict out-of-sample

# %%
y_13 = model.predict(pd.Series([3]))
print(f"Mean {target} for the 13th month is {round(y_13.squeeze()/ (60))} minutes.")

# %% [markdown]
# # Export in-sample predictions

# %%
in_sample_pred.to_csv(output, index=False)
