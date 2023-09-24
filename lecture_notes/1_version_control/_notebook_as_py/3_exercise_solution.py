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

# %% [markdown]
# [//]: <> (s)
# ### Solution
# 1. We first fetch and checkout the feature-branch
#     ```bash
#     git fetch &&
#     git checkout feature-branch
#     ```
# 1. We then add `AUTHOR.md`, assuming your working directory is your folder of the playground repo.
#     ```bash
#     echo 'Fabian Spanhel' > AUTHOR.md &&
#     git add AUTHOR.md
#     git commit -m "Add AUTHOR.md"
#     ```
# 2. Although it might be tempted to put the renaming of a file and editing its content into one commit, it is more atomic to use the following two separate commits
#     ```bash
#     git mv AUTHOR.md AUTHORS.md &&
#     git add AUTHOR.md AUTHORS.md &&
#     git commit -m "Rename AUTHOR.md to AUTHORS.md"
#     ```
#     and
#     ```bash
#     echo 'Fabian Spanhel (fabian.spanhel@hm.edu)' > AUTHORS.md &&
#     git add AUTHORS.md &&
#     git commit -m "Update AUTHORS.md"
#     ```

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

# %% [markdown] slideshow={"slide_type": "slide"} tags=["solution"]
# [//]: <> (s)
# ### Solution
# This exercise demonstrates ```git merge```.
# 1. Integrating `_source` into `_target` by (3-way) merging `_source` into `_target`:
#     ```bash
#     git checkout _target && 
#     git merge _source --no-edit  # the flag --no-edit is used so that we don't have to change the merge commit message
#     ```
# 1. Tidy up:
#     ```bash
#     git checkout main &&
#     git branch -D _source _target
#     ```

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

# %% [markdown] slideshow={"slide_type": "slide"} tags=["solution"]
# [//]: <> (s)
# ### Solution
# This exercise demonstrates ```git rebase```.
# 1. Integrating `_source` into `_target` by rebasing `_target` on `_source`:
#     ```bash
#     git checkout _target && 
#     git rebase _source
#     ```
# 1. Tidy up:
#     ```bash
#     git checkout main &&
#     git branch -D _source _target
#     ```

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

# %% [markdown] slideshow={"slide_type": "slide"} tags=["solution"]
# [//]: <> (s)
# ### Solution
# In this exercise, the use of an interactive rebase is practiced.
# Run the following commands in the terminal.  
# 1. Let's create the branches and checkout `_source`:
#     ```bash
#     git branch _target &&
#     git checkout -b _source
#     ```
# 1. Do the commits manually or run ```python3 -m dsc.version_control.exercise_git third```.
# 1. Start an interactive rebase on the commit which has been done 4 commits ago.
#     ```bash
#     git rebase -i HEAD~4  # HEAD~4 refers to the commit 4 commits ago
#     ```
#     and edit the git-rebase-todo file as follows
#
#     ```bash
#     pick   193caaf Add abc to the first line
#     squash 49bdf42 Add def to the second line
#     edit   02ea624 Add ghi to the third line
#     drop   1da20a1 Add jkl to the fourth line
#     ```
#     and conduct the rebase by 
#     - Performing the squash of 49bdf42 into 193caaf by changing the commit message to
#         "Add abc to the first line and def to the second line."
#     - During the edit of the third commit change `text.md` into
#         ```sh
#         abc
#         def
#         jkl
#         ``` 
#     and then run ```git add``` and ```git commit --amend```. Change the commit message to "Add jkl to the third line" when your text editor is opened, and finally execute ```git rebase --continue```.
#
# 4. Merge `_source` into `_target` and delete `_source`:
# ```bash
# git checkout _target &&
# git merge _source &&
# git branch -d _source
# ```
# 5. Tidy up:
# ```bash
# git checkout main &&
# git branch -D _target
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Exercise
# 1. Create a new branch named by your name. 
# 1. Commit a text file name `animal.md` that contains the name of your favorite animal.
# 1. Undo the previous commit using an interactive rebase so that `animal.md` contains your second favorite animal.
# 1. Push `animal.md` to a remote with the same name.
# 1. Assuming that the remote might be investigate by somebody else, undo the previous commit on the remote so that `animal.md` contains your favorite animal again.
# 1. Checkout to main and delete the local and remote branch named by your name.

# %% [markdown] slideshow={"slide_type": "slide"} tags=["solution"]
# [//]: <> (s)
# ### Solution
# 1. Let's create the branch with the name:
#     ```bash
#     git checkout -b my_name
#     ```
# 1. Let's create `animal.md`:
#     ```bash
#     echo "The cat is my favorite animal, MEOW!!!" > animal.md &&
#     git add animal.md &&
#     git commit -m "Add animal.md which mentions my favorite animal"
#     ```
# 1. We start an interactive rebase using
#     ```bash
#     git rebase -i HEAD~1
#     ```
#     and edit the git-rebase-todo file as follows
#     ```bash
#     edit 193caaf Add animal.txt which mentions my favorite animal
#     ```
#     and change `animal.md` into
#     ```
#     The dog is my second favorite animal, WOOF!!!
#     ``` 
#     and then run ```git add```, ```git commit --amend```, change the commit message to "Add animal.md which mentions my second favorite animal" when your text editor is opened, and finally execute ```git rebase --continue```.
# 1. We now push to the remote:
#     ```bash
#     git fetch && git status  # It is always good to get the current status before interacting with a remote
#     git push -u origin my_name
#     ```
# 1. Since the remote branch is not private you should not rebase your local branch and then push to the remote. Instead you should add a new commit to your local branch and then push the changes as follows:
#     ```bash
#     rm animal.md &&
#     echo "The cat is my favorite animal, MEOW!!!" > animal.md &&
#     git add animal.md && 
#     git commit -m "Add animal.txt which mentions my favorite animal" &&
#     git push
#     ```
# 1. Tidy up:
# ```bash
# git checkout main &&
# git push -d origin my_name &&
# git branch -D my_name
# ```

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

# %%
# code cell
1

# %% [markdown] slideshow={"slide_type": "slide"} tags=["solution"]
# [//]: <> (s)
# ## Solution
# 1. Let's checkout the branch
#     ```bash
#     git checkout -b _jupytext
#     ```
# 1. Assuming the location of this notebook is given by `../dsc/lecture_notes/2_version_control/3_exercise.ipynb`, we copy this notebook to the root of your local playground repo using
#     ```bash
#     cp ../dsc/lecture_notes/2_version_control/3_exercise.ipynb .
#     ```
#     and commit it to the `_jupytext` branch using
#     ```bash
#     git add 3_exercise.ipynb &&
#     git commit -m "Add 3_exercise.ipynb"
#     ```
# 1. From the root directory of this project run
#     ```bash
#     jupytext --to py:percent --out 3_exercise.py 3_exercise.ipynb
#     ```
# 1. Let's commit the .py script:
#     ```bash
#     git add 3_exercise.py &&
#     git commit -m "Add .py script of 3_exercise.ipynb"
#     ```
# 1. Executing the code cell above should change the cell counter.
# 1. After saving the notebook, ```git status``` shows that this notebook has been changed, but the .py script is unchanged.
#     - The notebook has been changed because the cell counter has increased, but this is no meanigful change.
#     - The .py script has not changed because it only contains the input of the notebook cells (and the notebook meta data).
#     - Thus, we should not commit the change.<br><br>
# 1. Select the cell in command mode and press dd to delete the code cell or use the context menu.
# 1. Run 
#     ```bash
#     jupytext --to py:percent --out 3_exercise.py 3_exercise.ipynb
#     ```
# to convert the notebook once again to a .py script.
# 1. Running ```git status```now shows that the .ipynb and .py file of the notebook have been changed. Since the .py file has been changed, the input of the notebook has been changed. Thus, we commit both the modified .iypnb and .py file.
# 1. Tidy up:
#     ```bash
#     git checkout main &&
#     git branch -D _jupytext
#     ```

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

# %% [markdown] slideshow={"slide_type": "slide"} tags=["solution"]
# [//]: <> (s)
# ## Solution 
# For this exercise it is helpful to create the following Python program which should be saved as src/dsc/version_control/exercise_dvc.py into the root of the course repo.
# ```python
# """ Helper for the DVC exercise in
#     lecture_notes/1_version_control/3_exercise.ipynb.
#
#     Creates the file 'movies_2018.csv' which contains
#     all distinct movies titles from 2018-01-01 until
#     {arg}-12-31, where arg is the first argument that
#     is provided to this program when it is run.
#
#     Program should be run from the root directory of
#     the project using python3 -m dsc.version_control.exercise_dvc YYYY
# """
# if __name__ == '__main__':
#     import sys
#     import sqlite3
#
#     import pandas as pd
#
#     until = sys.argv[1]
#     connection = sqlite3.connect("data/dsc.db")
#     cursor = connection.cursor()
#     output = "data/movies_2018.csv"
#
#     def execute_query(query: str):
#         return pd.read_sql_query(query, connection)
#
#     movies = execute_query(f"""
#     SELECT DISTINCT(title)
#     FROM broadcast
#     WHERE genre = 'Spielfilm'
#         AND start_time_agf >= '2018-01-01'
#         AND end_time_agf <= '{until}-12-31'
#     """)
#
#     movies.to_csv(output, index=False)
#     print(f"> created {output}, with data until {until}-12-31")
#
#
# ```

# %% [markdown] slideshow={"slide_type": "slide"} tags=["solution"]
# [//]: <> (s)
# <!--
# 1. Go to https://www.google.com/intl/de/drive/ and open Gdrive. If you don't have a Google account create one. Don't forget to to share the corresponding Google Drive folder to at least one other person or group. For instance, you can share it with spanhel@hm.edu.
# -->
# 1. In the terminal, run 
#     ```bash
#     git checkout -b _dvc_exercise
#     ```
# 1. To create movies_2018.csv you can either export the corresponding query result from DBeaver (using the sql editor to query the database and then exporting the result as csv by right-clicking on the resulting table in DBeaver) or run ```python3 -m dsc.version_control.exercise_dvc 2018```
# 1. If DVC has not been initialized in your project, run the following command from the root of your Git repo
#     ```bash
#     dvc init
#     ```
#    Run
#     ```bash
#     dvc add data/movies_2018.csv &&
#     git add data/movies_2018.csv.dvc data/.gitignore &&
#     git commit -m "Add movies_2018.csv.dvc" 
#     ```
# 1. Run
#     ```bash
#     dvc remote add -d -f dvc_gdrive path2gdrive_folder &&
#     dvc push
#     ```
#     where path2gdrive_folder is the path of your gdrive folder.
# 1. You can either export and append the corresponding query result from DBeaver or run ```python3 -m dsc.version_control.exercise_dvc 2019```
# 1. Run
#     ```bash
#     dvc move data/movies_2018.csv data/movies_2018_2019.csv &&
#     git add data/movies_2018_2019.csv.dvc data/movies_2018.csv.dvc data/.gitignore && 
#     git commit -m "Add movies from 2019 to movies_2018.csv.dvc and rename movies_2018.csv.dvc to movies_2018_2019.csv.dvc"
#     ```
# 1. Run
#     ```bash
#     dvc push
#     ```
# 1. The md5 hash of the corresponding .dvc files can be used to identify the folders, see the [cache section](./2_dvc.ipynb#The-cache) in `lecture_notes/2_version_control/2_dvc.ipynb`.
# 1. Let's roll back to step 4.
#     ```bash
#      git checkout HEAD~1 &&
#      dvc checkout
#     ```
# 1. Tidy up:
#     ```bash
#     git checkout main &&
#     git branch -D _dvc_exercise && 
#     dvc destroy &&
#     rm data/movies_2018.csv
#     ```
