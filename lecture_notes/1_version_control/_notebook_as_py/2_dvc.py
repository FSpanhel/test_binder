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
#     display_name: Python [conda env:dsc_2022]
#     language: python
#     name: conda-env-dsc_2022-py
# ---

# %% slideshow={"slide_type": "skip"}
from dsc.notebook import embed_website

# %% [markdown] slideshow={"slide_type": "slide"}
# # What is DVC?
# <br>
# <div align="left">
# <img src="./figures/3_what_is_dvc.png" alt="What is DVC" width=800/>
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# - DVC extends Git to use it for data science. 
# - A [popular and established](https://hn.algolia.com/?q=dvc) tool for data versioning although there are alternatives.
# - Its commits are pointers to data sets.
#     - The actual data is added to .gitignore and thus not commited to Git but to a storage location.
#     - For file that is put into a storage location, DVC creates .dvc files wich are pointers to the data that are tracked by Git.
# - Storage is not GitHub or GitLab but can be local or a remote storage like S3 oder Google drive
#

# %% [markdown] slideshow={"slide_type": "slide"}
# <br>
# <div align="left">
# <figcaption>DVC Overview (Source: DVC) </figcaption>
# <img src="./figures/4_dvc_overview.png" alt="DVC Overview" width=800/>
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# **Differences to Git**
# - DVC is technically **not a version control system** 
#     - DVC creates .dvc files
#     - .dvc file contents determine data versions
#     - .dvc files are versioned by Git
#     - DVC checkouts working copies of data 
# - **Merging or comparing changes of data is not possible**, but merging/comparing changes of .dvc files possible
# - The command **dvc add also commits** (in the sense of DVC), so dvc commit is not required
# - The command **dvc pull does a fetch and a checkout** but not a merge

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Installation & resources
# [Installation](https://dvc.org/doc/install) -> **Please install DVC now!**
#
# **Resources**
# - [Official docs](https://dvc.org/doc/start) (pretty amazing!)
# - [Short video that motivates DVC](https://www.youtube.com/watch?v=UbL7VUpv1Bs)
# - [Official video introduction to DVC for data versioning](https://www.youtube.com/watch?v=kLKBcPonMYw) 
# - [Plugin for VSCode](https://marketplace.visualstudio.com/items?itemName=Iterative.dvc)
# - Also interesting...
#     - https://dvcfan.com/2021/04/14/some-hard-truths-about-dvc/
#     - https://www.youtube.com/watch?v=VttqJE-Vcjg

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Important commands
# - [init](https://dvc.org/doc/command-reference/init): init DVC, should be run in git repo root
# - [add](https://dvc.org/doc/command-reference/add): in contrast to Git, this also commits
# - [status](https://dvc.org/doc/command-reference/status): show file differences either between the cache and workspace, or between the cache and remote storage.
# - [move](https://dvc.org/doc/command-reference/move): files that are tracked by DVC should be renamed using this command
# - [checkout](https://dvc.org/doc/command-reference/checkout): update DVC-tracked files in the workspace based on current .dvc files.
# - [fetch](https://dvc.org/doc/command-reference/fetch): download files from remote storage to the cache based on .dvc files
# - [pull](https://dvc.org/doc/command-reference/pull): fetches files and makes them visible in the workspace
# - [push](https://dvc.org/doc/command-reference/push): upload tracked files to remote storage based on .dvc files.
# - [destroy](https://dvc.org/doc/command-reference/destroy): remove all DVC files and internals from a Git repo.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Initialization: dvc init

# %% [markdown] slideshow={"slide_type": "-"}
# - Let's checkout a new branch,

# %% slideshow={"slide_type": "-"}
!git checkout -b _dvc_illustration 

# %% [markdown] slideshow={"slide_type": "-"}
# - And go to Git repository root because DVC needs to be initalized from this directory.

# %% slideshow={"slide_type": "-"}
import os
os.chdir("../..")
os.getcwd()

# %% [markdown] slideshow={"slide_type": "slide"}
# - Let's initialize DVC.

# %% slideshow={"slide_type": "-"}
!dvc init

# %% [markdown] slideshow={"slide_type": "-"}
# - The previous command creates the file .dvcignore and the directory .dvc that are also put in the staging area of Git.
# - You have to commit them to Git so that DVC is read to use.

# %% slideshow={"slide_type": "-"}
!git status

# %% slideshow={"slide_type": "-"}
!git commit -m "Init DVC"

# %% [markdown] slideshow={"slide_type": "slide"}
# # Local usage

# %% [markdown] hide_input=true slideshow={"slide_type": "-"}
# Let's create some dummy data that should be tracked by DVC.

# %% slideshow={"slide_type": "-"}
!echo "This is a really big data set" > big_data.txt

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Start tracking: dvc add
# - Files that are already tracked by Git cannot be tracked by DVC (and will raise an error).
# - To track files with DVC use dvc add.

# %% slideshow={"slide_type": "-"}
!dvc add big_data.txt

# %% [markdown] slideshow={"slide_type": "slide"}
# - DVC stores information about the added file in a .dvc file 
# named big_data.txt.dvc.
# - This metadata file is human-readable and a placeholder for the original data.
# - Like source code it can be easily versioned  with Git. 
# - **Do not modify .dvc files**, otherwise DVC gets confused/breaks!
# - **If you want to move data** that is tracked by DVC use dvc move so that the corresponding .dvc file is also updated!

# %% slideshow={"slide_type": "-"}
!cat big_data.txt.dvc 

# %% [markdown] slideshow={"slide_type": "-"}
# * The data, meanwhile, is append to .gitignore.

# %% slideshow={"slide_type": "-"}
!cat .gitignore | tail -n 1

# %% [markdown] slideshow={"slide_type": "slide"}
# ### The cache
# - Moreover, the data is committed (!) in the sense that the current 
# state of files and directories tracked by DVC are moved to the cache.
#
# - Use the --no-commit option to avoid this, and dvc commit to store the data in the cache.
#
# - The cache consists of directories
#     - A directory is named after the first two entries of the md5 hash of a corresponding .dvc file
#     - The following entries of the md5 hash constitute the name of the files in such a directory 

# %% slideshow={"slide_type": "-"}
!tree ./.dvc/cache/

# %% [markdown] slideshow={"slide_type": "fragment"}
# - Each file in the cache is a copy of the original data and DVC tries to replace the original data with a link to this copy.

# %% slideshow={"slide_type": "-"}
!cat ./.dvc/cache/*/*    

# %% [markdown] slideshow={"slide_type": "slide"}
# To version big_data.txt with Git, we add and commit the corresponding .dvc file and 
# add the underlying data to Git's ignore list.

# %%
!git status

# %% slideshow={"slide_type": "-"}
!git add big_data.txt.dvc .gitignore && git commit -m "Add big_data.txt.dvc"  # I prefer to add big_data.txt.dvc and not big_data.txt so that it is clear that DVC is involved

# %% [markdown] slideshow={"slide_type": "slide"}
# ## View status: dvc (data) status

# %% [markdown] slideshow={"slide_type": "-"}
# We will now append new data to big_data.txt.

# %% slideshow={"slide_type": "-"}
!echo "It gets even bigger!" >> big_data.txt

# %% [markdown] slideshow={"slide_type": "slide"}
# Using git status we see that the change in big_data.txt is not visible because DVC has put it on .gitignore after we used dvc add big_data.txt.

# %% slideshow={"slide_type": "-"}
!git status

# %% [markdown] slideshow={"slide_type": "slide"}
# - There is no direct equivalent of git status in DVC.
# - But we can use ```dvc data status``` to show changes in the data tracked by DVC in the workspace.
# - Moreover, ```dvc data``` shows file mismatches either between the cache and workspace, or between the cache and remote storage.
# - As with Git it's a good practice to check the state of your DVC repository before doing something like dvc commit.
#

# %% slideshow={"slide_type": "-"}
!dvc data status  # files which are untracked by dvc and git can be shown by using the option --untracked-files)

# %% slideshow={"slide_type": "-"}
!dvc status  # compares files between the cache (local copy of the remote, files that are tracked) and workspace

# %% [markdown] slideshow={"slide_type": "-"}
# You can also use ```dvc diff```.

# %% slideshow={"slide_type": "-"}
!dvc diff

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Committing: dvc add

# %% [markdown] slideshow={"slide_type": "-"}
# - We can now commit the changes to DVC using ```dvc add``` (or ```dvc commit```)
# - Note that ```dvc add``` also commits the data.

# %% slideshow={"slide_type": "-"}
!dvc add big_data.txt

# %% slideshow={"slide_type": "-"}
!dvc data status

# %% [markdown] slideshow={"slide_type": "-"}
# Executing ```dvc add``` also changes the correspond .dvc file which should be committed to Git.

# %% slideshow={"slide_type": "-"}
!git status

# %% slideshow={"slide_type": "-"}
!git add "big_data.txt.dvc" && git commit -m "Update big_data.txt.dvc"

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Renaming files: dvc move

# %% [markdown] slideshow={"slide_type": "-"}
# - If you want to rename data use ```dvc move```.
# - This deletes big_data.txt and the corresponding .dvc file and replaces them by massive_data.txt and a corresponding .dvc file.

# %% slideshow={"slide_type": "-"}
!dvc move big_data.txt massive_data.txt

# %% slideshow={"slide_type": "-"}
!cat massive_data.txt.dvc

# %% [markdown] slideshow={"slide_type": "slide"}
# Having a look at the ```dvc data status``` shows that dvc move has also added and committed the changes to DVC (but not to Git).

# %% slideshow={"slide_type": "-"}
!dvc data status

# %% slideshow={"slide_type": "-"}
!dvc status

# %% [markdown] slideshow={"slide_type": "slide"}
# Committing to Git.

# %% slideshow={"slide_type": "-"}
!git add massive_data.txt.dvc big_data.txt.dvc .gitignore && git commit -m "Renamed big_data.txt.dvc into massive_data.txt.dvc"

# %% [markdown] slideshow={"slide_type": "-"}
# Calling ```dvc data status``` does not show DVC committed changes anymore if the corresponding .dvc files have been committed to Git.

# %%
!dvc data status

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Returning to previous data: dvc checkout
# - Versions of files are determined by the appropriate .dvc files that store their md5 checksums. 
# - Thus, data files are fully determined by the version of the corresponding .dvc files which are tracked by Git.
#
# - ```dvc checkout``` is ofter needed after ```git checkout```, ```git clone``` or other operations that change the current state
# of the .dvc files. 
# - It restores the corresponding versions of all DVC-tracked data files and directories from the cache to the workspace.
#
# - Let's checkout the previous commit.

# %% slideshow={"slide_type": "-"}
!git checkout HEAD~1

# %% [markdown] slideshow={"slide_type": "slide"}
# Let's investigate the status of Git.

# %% slideshow={"slide_type": "-"}
!git status

# %% [markdown] slideshow={"slide_type": "fragment"}
#  - Note that massive_data.txt was never added or committed to Git but put on .gitignore by dvc add.
#  - By checking out the previous commit we have also revoked putting massive_data.txt on .gitignore.
#  - Thus, massive_data.txt is now untracked by Git.

# %% [markdown] slideshow={"slide_type": "slide"}
# Let's have a look at the data status of DVC.

# %% slideshow={"slide_type": "-"}
!dvc data status

# %% [markdown] slideshow={"slide_type": "fragment"}
# - ```dvc data status``` now shows that big_data.txt is deleted (which was the effect of ```dvc move```)
# - This makes sense because in the next Git commit big_data.txt.dvc is replaced by massive_data.txt.dvc.

# %% [markdown] slideshow={"slide_type": "slide"}
# The file big_data.txt.dvc (which has been modified by ```git checkout```) contains the information to restore the data.

# %% slideshow={"slide_type": "-"}
!cat big_data.txt.dvc

# %% [markdown] slideshow={"slide_type": "-"}
# - To restore big_data.txt we have to use ```dvc checkout```.
# - This also deletes massive_data.txt (because massive_data.txt.dvc does not exist).

# %% slideshow={"slide_type": "-"}
!dvc checkout

# %% [markdown] slideshow={"slide_type": "slide"}
# # Working with remotes
# - Working with remote is similar to Git. 
# - You first have to specify a remote storate location for the data.
# - The remote is typically not a sofware based on Git like GitHub or GitLab.
# - The following storage types are supported to serve as a remote storage location.

# %% slideshow={"slide_type": "-"}
embed_website("https://dvc.org/doc/command-reference/remote/add#supported-storage-types")

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Setting up a remote storage location: dvc remote add

# %% [markdown] slideshow={"slide_type": "-"}
# - You can add a local remote store using ```dvc remote add -d myremote path2store```, where myremote is the name of the remote and path2store its location
# - In this course, we use GDrive as DVC remote because it is the simplest way to do it and free of charge.
# - Sign into [GDrive](https://www.google.com/intl/de/drive/).
# - Create a new folder called `dsc`.
# - Extract the **folder id** of the GDrive folder which is given by the letters after `folders/`
# - For instance, the folder id of https://drive.google.com/drive/u/2/folders/15vLYuJslaBGh2ZA_oSYk1lKxqKqiZfgt is `15vLYuJslaBGh2ZA_oSYk1lKxqKqiZfgt`
# - Note the Google [drive limits on storage and uploads](https://support.google.com/a/users/answer/7338880?visit_id=637995289613302718-2725308169&rd=1)

# %% [markdown] slideshow={"slide_type": "slide"}
# - To add the Google drive remote we use the following command.

# %% slideshow={"slide_type": "-"}
!dvc remote add -d -f origin gdrive://1UsBl0O7MYHVOVBWKpySxmCqGhb5yF2p-

# %% slideshow={"slide_type": "-"}
- With the flag -d this becomes the default remote.
- With the flag -f this adds the remote even if it has already been added.

# %% [markdown] slideshow={"slide_type": "slide"}
# We can investigate file differences between the cache and the remote storage using

# %% slideshow={"slide_type": "-"}
!dvc status -c

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Sharing the GDrive remote with others
# - Other user can interact with the GDrive remote using DVC if you share the GDrive folder with them.
# - To share your GDrive folder with other persons, right-click on the created dsc folder and enter the Gmail address (e.g., spanhelhm@gmail.com) of the person you want to share this folder with and grant the `Editor` role.
#     - Sharing this folder by a link is **not sufficient**.
#     - In previous versions of DVC it was also necessary to share the GDrive folder with at least one other person before an interaction with the remote was possible (?).

# %% [markdown] slideshow={"slide_type": "-"}
# ### Authentication
# - If you run a command that interacts with a GDrive remote like `dvc status -c` or `dvc push` or `dvc pull` for the first time, you will be prompted to visit a Google authentication web page.
#     - See section [11.3.1 of lectures_notes/0_introduction/0_intro.ipynb](../0_introduction/0_intro.ipynb#Using-WSL) how to access this web page if you are using WSL.
# - In this case, sign in with your Google account and check `Select all` on the webpage to give DVC access.
# - The authentication credentials will then be cached globally to a .json file with location given in the bullet point [gdrive_user_credentials_file](https://dvc.org/doc/user-guide/data-management/remote-storage/google-drive#configuration-parameters).
# - Note that, by default, the credentials .json file is not located within the Git repo and the file should never be tracked by Git.
# - In case you have problems to authenticate, for instance,
#     ```
#     ERROR: unexpected error - Failed to authenticate GDrive: Access token refresh failed: invalid_grant: Bad Request
#     ```
#     <!-- https://discuss.dvc.org/t/manually-prompt-gdrive-authentication-step/858/4 -->
#   it is best to remove the credential file and authorize again.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Push data to remotes: dvc push

# %% slideshow={"slide_type": "-"}
!dvc push

# %% [markdown] slideshow={"slide_type": "slide"}
# - Normally, we should now push the Git commited .dvc files to a Git remote - but we don't do it in this illustration.

# %% [markdown] slideshow={"slide_type": "-"}
# ```bash
# git remote add git_remote_url
# git push -u origin dvc_lecture_temp
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Retrieve data from remote: dvc pull

# %% [markdown] slideshow={"slide_type": "-"}
# - Let's delete big_data.txt and pull it from the remote storage.

# %% slideshow={"slide_type": "-"}
!rm big_data.txt && dvc data status

# %% [markdown] slideshow={"slide_type": "-"}
# - Comparing files between the cache and the remote storage shows no difference.
# - That is because the same version of big_data.txt exists both in the cache and the remote storage.

# %% slideshow={"slide_type": "-"}
!dvc status -c

# %% [markdown] slideshow={"slide_type": "-"}
# By pulling the data, we fetch the data the from the remote storage that corresponds to the current commit
# and checkout its version.

# %% slideshow={"slide_type": "-"}
!dvc pull

# %% [markdown] slideshow={"slide_type": "slide"}
# # Remove dvc from git repo: dvc destroy
# - Let us remove all DVC files and internals.
# - This does not remove the actual data.
# - To recover DVC you can checkout the corresponding Git commit, pull from the remote and checkout.

# %% slideshow={"slide_type": "-"}
!yes | dvc destroy

# %% [markdown] slideshow={"slide_type": "-"}
# - Note that big_data.txt will remain.

# %% slideshow={"slide_type": "-"}
!ls

# %% [markdown] slideshow={"slide_type": "-"}
# - Thus, we delete big_data.txt and checkout to main.

# %% slideshow={"slide_type": "-"}
!rm big_data.txt && git checkout main && git branch -D _dvc_illustration
