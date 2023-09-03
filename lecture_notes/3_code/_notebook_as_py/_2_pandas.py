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
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# Resources
https://www.amazon.com/Effective-Pandas-Patterns-Manipulation-Treading/dp/B09MYXXSFM


# %%
Note that pandas is build upon numpy but not 100% compatible with numpy, i.e., treatment of missings

numpy: 

# %%
# Alternatives
polars
static frames

# %%
# Pandas functions that are not well-known but may be helpful

# %%
- pd.cut
- .squeeze
- .assign
. .query

# %%
# there's not only one thing how to do things
df.columns = [...]
df.rename(columns = {})

# %%
import pandas as pd

# %%
dir(pd.DataFrame)  # drop_duplicates, dropna (why not drop_na, droplevel)

# %%
dir(pd.MultiIndex) #  'sort_values', 'sortlevel',
