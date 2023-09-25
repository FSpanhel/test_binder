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
#     display_name: Python [conda env:dsc] *
#     language: python
#     name: conda-env-dsc-py
# ---

# %% [markdown]
# ## getting data from remote storage: dvc get

# %% [markdown]
# We download the latest version of the data.xml file from the dataset registry repo as the data source.

# %%
!dvc get https://github.com/iterative/dataset-registry get-started/data.xml -o dvc/data.xml  # ./dvc/data.xml can also be used

# %%
Note that get-started/data.xml does not exist in the remote repo 
https://github.com/iterative/example-get-started/tree/main/data
but just meta data https://github.com/iterative/example-get-started/blob/main/data/data.xml.dvc 
that points to the actual file.

# %% [markdown]
# How to avoid data duplication between cache and workspace

# %%
https://discuss.dvc.org/t/how-to-avoid-data-duplication-between-cache-and-workspace/1340
