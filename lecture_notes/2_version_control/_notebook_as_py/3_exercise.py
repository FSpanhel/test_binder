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

# %% [markdown] slideshow={"slide_type": "slide"} solution="hidden"
# # Questions regarding the next topic (Python project setup)

# %% [markdown] slideshow={"slide_type": "-"}
# Click [here](https://partici.fi/26194946), or scan the QR code below, to answer the questions about setting up your Python project.
# <div align="center">
# <img src="./figures/p_2.png" alt="drawing" width="1200"/>
# </div>
#
# <div align="left">
# <div/>

# %% [markdown]
# # Git
# - **Cd into your folder of the playground repo** that you have created in the issue with the title `[name]: First task`, where [name] is your full name, e.g., "Fabian Spanhel".
# - For some exercises you can run ```python3 -m dsc.version_control.exercise_git [<arg>]``` where arg can be first, second, or third, to set up the necessary commits in Git.
#     - Note that the `dsc` environment must be activated for these commands.
#     - You can activate the `dsc` environment using `mamba activate dsc`.
# - In these cases, you can try to run ```python3 -m dsc.version_control.exercise_git reset``` to undo these commits. If this doesn't work you have to undo the commits manually.
# - Don't be afraid to use ```git status``` frequently to see on which branch you are and what changes Git is tracking.
# - Before you start with one exercise, verify that your **working directory is clean**, i.e., you have no uncommitted changes.
#

# %% [markdown]
# ## Exercise
# - Create an issue in the [playground repo](https://gitlab.lrz.de/dsc/2023/playground) with the title "[name]: Exercise 3.2.1", where [name] is your full name, and create a corresponding branch and MR.
# - You can use "Tackle Exercise 3.2.1" as issue description.
# - Add the file `AUTHOR.md`.  to your folder that contains your name in the first line.
# - Rename this file into `AUTHORS.md` and add your HM email address after your name.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Exercise
# Run ```python3 -m dsc.version_control.exercise_git first``` or the following commands in the terminal:
# ```bash
# git checkout -b _target && echo '123' > a.py && git add a.py && git commit -m 'Add a.py' &&
# git checkout main &&
# git checkout -b _source && echo '123' > b.py && git add b.py && git commit -m 'Add b.py'
# ```
# Have a look at the commit history/log (using ```git log``` or GitGraph in VSCode).  
#
# 1) Perform operations so that the commit history looks as follows (note that the order of the last two commits is arbitary here and might be reversed in your GitGraph):  
# ![commit history](./figures/0_exercise.png)
# <br>
# 2) Run ```python3 -m dsc.version_control.exercise_git reset``` or checkout to main and delete all branches manually.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Exercise
# Run ```python3 -m dsc.version_control.exercise_git second``` or the following commands in the terminal:
# ```bash
# git checkout -b _target && echo '123' > a.py && git add a.py && git commit -m 'Add a.py' &&
# git checkout main &&
# git checkout -b _source && echo '123' > b.py && git add b.py && git commit -m 'Add b.py'
# ```
# Have a look at the commit history/log (using ```git log``` or GitGraph in VSCode). 
#
# 1) Perform operations so that the log looks as follows:  
# ![commit history](./figures/1_exercise.png)
# <br>
# 2) Run ```python3 -m dsc.version_control.exercise_git reset``` or checkout to main and delete all branches manually.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Exercise
# 1. Create two new branches called `_source` and `_target`. Checkout the branch `_source`.
# 1. Add a `text.md` with the following commits:
#     - Add "abc" as first line and commit "Add abc to the first line".
#     - Add "def" as second line and commit "Add def to the second line".
#     - Add "ghi" as third line and commit "Add ghi to the third line".    
#     - Add "jkl" as fourth line and commit "Add jkl to the fourth line".
#     
#    Alternatively, you can run ```python3 -m dsc.version_control.exercise_git third``` to execute the commits but I recommend to do the commits manually at least once. 
# 1. Do the following changes
#     1. Combine the first and second commit and adjust the commit message accordingly to "Add abc to the first line and def to the second line".   
#     1. Add "jkl" and not "ghi" as third line in the third commit.  
#     1. Drop the fourth commit.
# 1. Merge `_source` into `_target` and delete `_source`.
# 1. Checkout to `main` and delete `_target`.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Exercise
# 1. Create a new branch named by your name. 
# 1. Commit a text file name `animal.md` that contains the name of your favorite animal.
# 1. Undo the previous commit using an interactive rebase so that `animal.md` contains your second favorite animal.
# 1. Push `animal.md` to a remote with the same name.
# 1. Assuming that the remote might be investigate by somebody else, undo the previous commit on the remote so that `animal.md` contains your favorite animal again.
# 1. Checkout to main and delete the local and remote branch named by your name.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Versioning Jupyter notebooks
# 1. Checkout the (new) branch `_jupytext`. 
# 1. Copy this notebook to the root of your local playground repo and commit it to the (local) `_jupytext` branch.
# 1. Create a .py script (with the same name) of this notebook .ipynb file using Jupytext.
# 1. Commit the the .py script to Git.
# 1. Execute the following code cell and save the notebook.
# 1. Run git status. Does it make sense to commit the change?
# 1. Delete the following code cell below.
# 1. Convert the modified notebook .ipynb file again to a .py script (with the same name) using Jupytext.
# 1. What does ```git status``` tell you? What changes should you commit?
# 1. Delete the branch `_jupytext` and checkout to `main`.

# %% [markdown] slideshow={"slide_type": "slide"}
# # DVC
# 1. Create a new branch `_dvc_exercise`.
# 1. Using the broadcast table of `data/dsc.db`, put all distinct movie titles that were broadcasted in 2018 into `movies_2018.csv` which you save in `data/`.
# 1. Track movies_2018.csv with DVC and Git.
# 1. Push movies_2018.csv to your Gdrive account. 
# 1. Overwrite movies_2018.csv with all distinct movie titles from the broadcast table of data/dsc.db that were broadcasted in 2018 and 2019.
# 1. Rename movies_2018.csv to movies_2018_2019.csv.
# 1. Push movies_2018_2019.csv to your Gdrive account.
# 1. Locate movies_2018.csv and movies_2018_2019.csv on your Gdrive account.
# 1. Roll back to step 4.
# 1. Checkout to main and tidy up.
