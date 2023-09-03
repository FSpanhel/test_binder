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
#     display_name: Python [conda env:dsc]
#     language: python
#     name: conda-env-dsc-py
# ---

# %%
# jupyter notebook --generate-config
# > generates config in /home/spa0001f/.jupyter/jupyter_notebook_config.py


# %% [markdown]
# # Formatting

# %% [markdown]
# ## display all outputs

# %%
from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all" # ‘all’, ‘last’, ‘last_expr’ or ‘none’, ‘last_expr_or_assign’

# %% [markdown]
# ## footnotes

# %% [markdown]
# Just a footnote[<sup id="fn2-back">2</sup>](#fn2).
#
# [<sup id="fn2">2</sup>](#fn2-back) footnote 2

# %%
Just a footnote[<sup id="fn2-back">2</sup>](#fn2).

[<sup id="fn2">2</sup>](#fn2-back) footnote 2

# %% [markdown]
# ## details

# %% [markdown]
# <details>
#
#
# Let's say we obtained more data from some external source. We can pretend this
# is the case by doubling the dataset:
#
#
# </details>

# %% [markdown]
# # Trust notebook

# %%
# https://stackoverflow.com/questions/66509195/how-to-mark-jupyter-notebook-trusted-when-generating-the-notebook-with-papermill
# jupyter trust mynotebook.ipynb

# %%
!pwd

# %% [markdown]
# # set notebook starting dir -> has no effect, starting working directory is still the directory of the notebook, maybe an IPython thin?

# %%
jupyter notebook --notebook-dir="."

# %% [markdown]
# # embed html

# %%
from IPython.display import display, HTML
display(HTML('<h1>Hello, world!</h1>'))
HTML?

# %% [markdown]
# # embed website

# %%
from IPython.display import IFrame
IFrame("https://www.openasapp.com/embedding-an-iframe-step-by-step/", 900,500)

# %% [markdown]
# # embed image in md
# ![alt text](Isolated.png "Title")

# %% [markdown]
# ## center and title

# %% [markdown]
# <div align="center">
#
# <h2>The Data Science Hierarchy of Needs</h2>
#
# <img src="./figures/0_1_hierarchy.png" alt="drawing" width="1200"/>
#
# </div>
#
# Source: https://www.reddit.com/r/datascience/comments/wi2gil/the_data_science_hierarchy_of_needs
#
# [Source](https://www.reddit.com/r/datascience/comments/wi2gil/the_data_science_hierarchy_of_needs)

# %% [markdown]
# # Links
#
