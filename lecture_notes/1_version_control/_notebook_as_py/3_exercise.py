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

# %% [markdown] slideshow={"slide_type": "slide"} solution="hidden"
# # Questions regarding next week's topic (Python project setup)

# %% [markdown] slideshow={"slide_type": "-"}
# Click [here](https://partici.fi/26194946), or scan the QR code below, to answer the questions about setting up your Python project.
# <div align="center">
# <img src="./figures/p_2.png" alt="drawing" width="1200"/>
# </div>
#
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# # Git
# - Before you start with one exercise, verify that your **working directory is clean**, i.e., you have no uncommitted changes.
# - For the first three exercise you can run ```python3 -m dsc.version_control.exercise_git [<arg>]``` where arg can be first, second, or third, to set up the necessary commits in Git.
# - You can try to run ```python3 -m dsc.version_control.exercise_git reset``` to undo these commits. If this doesn't work you have to undo the commits manually.
# - Don't be afraid to use ```git status``` frequently to see on which branch you are and what changes Git is tracking.

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
# 1. Create two new branches called _source and _target. Checkout _source.
# 1. Add a **text.md** with the following commits:
#     - Add "abc" as first line and commit "Add abc to the first line".
#     - Add "def" as second line and commit "Add def to the second line".
#     - Add "ghi" as third line and commit "Add ghi to the third line".    
#     - Add "jkl" as fourth line and commit "Add jkl to the fourth line".
#     
#    Alternatively, you can run ```python3 -m dsc.version_control.exercise_git third``` to execute the commits but I recommend to do the commits manually at least once. 
# <br><br>
# 1. Do the following changes
#     1. Combine the first and second commit and adjust the commit message accordingly to "Add abc to the first line and def to the second line".   
#     1. Add "jkl" and not "ghi" as third line in the third commit.  
#     1. Drop the fourth commit.
# <br><br>
# 1. Merge _source into _target and delete _source.
# 1. Checkout to main and delete _target.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Exercise
# 1. Create a new branch named by your name. 
# 1. Commit a text file name 'animal.txt' that contains the name of your favorite animal.
# 1. Undo the previous commit using an interactive rebase so that 'animal.txt' contains your second favorite animal.
# 1. Push 'animal.txt' to a remote with the same name.
# 1. Assuming that the remote might be investigate by somebody else, undo the previous commit on the remote so that 'animal.txt' contains your favorite animal.
# 1. Checkout to main and delete the local and remote branch named by your name.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Versioning Jupyter notebooks
# 1. Checkout the (new) branch _jupytext. 
# 1. Create a .py script (with the same name) of this notebook .ipynb file using Jupytext.
# 1. Commit the the .py script to Git.
# 1. Execute the following code cell and save the notebook.
# 1. Run git status. Does it make sense to commit the change?
# 1. Delete the following code cell below.
# 1. Convert the modified notebook .ipynb file again to a .py script (with the same name) using Jupytext.
# 1. What does ```git status``` tell you? What changes should you commit?
# 1. Delete the branch _temp.

# %%
# code cell
1

# %% [markdown] slideshow={"slide_type": "slide"}
# # DVC
# 1. Set up your own Gdrive account. You can share files of this Gdrive with spanhel@hm.edu.
# 1. Create a new git branch _dvc_exercise
# 1. Using the broadcast table of data/dsc.db, put all distinct movie titles that were broadcasted in 2018 into movies_2018.csv which you save in data/.
# 1. Track movies_2018.csv with DVC and Git.
# 1. Push movies_2018.csv to your Gdrive account. 
# 1. Overwrite movies_2018.csv with all distinct movie titles from the broadcast table of data/dsc.db that were broadcasted in 2018 and 2019.
# 1. Rename movies_2018.csv to movies_2018_2019.csv.
# 1. Push movies_2018_2019.csv to your Gdrive account.
# 1. Locate movies_2018.csv and movies_2018_2019.csv on your Gdrive account.
# 1. Roll back to 4.
# 1. Checkout to main and tidy up.
