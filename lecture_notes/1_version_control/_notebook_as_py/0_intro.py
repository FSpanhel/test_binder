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
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% slideshow={"slide_type": "notes"}
from dsc.notebook import embed_website

# %% [markdown] slideshow={"slide_type": "slide"}
# <div align="center" style="font-size:70px;">
# VERSION CONTROL
# <div/>
#     
# <div align="left" style="font-size:16px;">
# <div/>
# <div align="left">
# <img src="./figures/vc_intro_commitstrip.png" alt="VC" width=700/>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# # Agenda
# - Review of [Q&A](https://partici.fi/83687465).
#
# <div align="center">
# <img src="../0_introduction/figures/0_p.png" alt="drawing" width="1200"/>
# </div>
#
# <div align="left" style="font-size:16px;">
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# **Agenda**
# - In this lecture we won't discuss the basics of Git. 
# - You (hopefully) have used Git already in your study and during your intership in the 4th semester.
# - However, we will consider some points that **facilitate collaboration with Git** and that you might not know.
# - We will also address **how to version Jupyter notebooks**
# - After that we will consider **data versioning with a focus on DVC**.
# - The tracking of models will be discussed in a later chapter when we consider MLflow. 

# %% [markdown] slideshow={"slide_type": "slide"}
# # Introduction

# %% [markdown] slideshow={"slide_type": "-"}
# - **Source code is the heart and soul** of almost all software projects.
#
# - To protect, develop and manage source code, **version control systems** are used and help to
#     - track every individual change by each contributor
#     - allow simultaenous work 
#     while preventing concurrent work from conflicting
#     - compare and roll back to earlier versions of the code to fix mistakes
#     - build the fundament for other tools that improve software development (e.g., CICD, data versioning, issues for project management)
#
# - Version control is **essential for modern professional collaborative software development** but 
# also provides **high value for small solo projects and even non-software projects**.
#
#

# %% [markdown] slideshow={"slide_type": "slide"}
# **Version control and data science**
#
# - A lot of **classical software** mainly consists of **text files** which can be tracked by classical version control systems.
# - However, these version control systems are not sufficient for data science.
#
# - **In data science the application is not specified by the code**:
#     - We also have input data and fitted models.  
#     - **The code, data and model determine the output of the application**. 
#     - All of them might change.
#     - Each state of code, data and model is an experiment that we want to track and share.
#

# %% [markdown] slideshow={"slide_type": "slide"}
# # Code versioning with Git

# %% [markdown] slideshow={"slide_type": "-"}
# - There are many [version control systems for code](https://en.wikipedia.org/wiki/List_of_version-control_software)
# - [Git](https://git-scm.com/) is the **most popular version control system for code** and offers
# a [strong set of features](https://www.atlassian.com/git/tutorials/what-is-git) for developers
# - [Wikipedia](https://en.wikipedia.org/wiki/Git): "Git is a free and open source software for **distributed version control**: **tracking changes** in any set of (text) files, 
# usually used for coordinating work among programmers **collaboratively developing 
# source code** during software development."
# - Files that contain credentials should not be versioned with Git (!)
# - Git is **not designed to serve as a backup tool or for storing binary or large files**
#     - Versioning non-text files (no code) is not meanigful with Git
#     - Git **repositories should be small**, ideally less than 1 GB and providers also have a push limit ([100 MB for GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github))
# - For larger files, it is not recommended to use Git and instead use **tools for data versioning**.
#
#
#
#

# %% [markdown] slideshow={"slide_type": "subslide"}
# **But can I add small binary files (presentations, figures, data) to Git?**
#
# - In principle yes.
# - But note that, e.g., if you commit a 10 MB binary file and then commit a change that doesn't change the file size, you will be adding 10 MB to the repository.
# - As a result, **the size of your repository can quickly blow up if you are making a lot of changes to the binary files**. 

# %% [markdown] slideshow={"slide_type": "slide"}
# # Tools for data versioning

# %% [markdown] slideshow={"slide_type": "-"}
# - There is a **handful of tools that provide versioning for data science** with each tool focussing
# on different aspects.

# %% [markdown] slideshow={"slide_type": "-"}
# |                 | Database queries |       Files      | Databases      |   |
# |:---------------:|:----------------:|:----------------:|:--------------:|---|
# | **Git-centric** |        Git       | Git-LFS, DVC,... |         x      |   |
# |  **De-coupled** |         x        |    Mlfow, ...    | DataLake, Dolt |   |

# %% [markdown] slideshow={"slide_type": "-"}
# - **Git-centric**:
#     - Assuming you have the required database infrastructure, you can **version sql queries** with Git.
#     - Other tools **version data on the file level**, e.g., binary files or (big) .csv-files, and **connect the version to a Git commit**
#         - We will discuss **Git-LFS** shortly, but focus on **DVC** in this course.

# %% [markdown] slideshow={"slide_type": "-"}
# - **De-coupled**:
#     - You can "misuse" tools like [Mlflow](https://mlflow.org/) or [Tensorboard](https://www.tensorflow.org/tensorboard) to track data as a hyperparameter.
#     - There a tools to directly **version databases**, e.g., [(Databricks) Delta Lake](https://delta.io/), or [Dolt](https://github.com/dolthub/dolt) for MySql.

# %% slideshow={"slide_type": "slide"}
embed_website("https://neptune.ai/blog/best-data-version-control-tools", height=400)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Git-LFS

# %% slideshow={"slide_type": "-"}
embed_website("https://git-lfs.github.com/", height=300)

# %% [markdown] slideshow={"slide_type": "slide"}
# - Git-LFS **handles large files by storing pointers to the file in the repository**,
# but not the actual file itself. 
# - The files content are stored on a remote server like GitHub or GitLab.
#
# - **Almost works like normal Git** except that
#     - One has to specify which files are tracked by Git-LFS
#     - One needs to convert LFS pointers to the actual data to access it (depends on the version?)
#     - It primarily stores data, there is no easy way of resolving binary merge conflicts (but files can be locked)
#     - Users that work with the repo need Git-LFS installed, otherwise they can only fetch the pointer files but not the actual data (depends on the version?)

# %% [markdown] slideshow={"slide_type": "fragment"}
# - Remote servers have a **limit on storage and bandwith consumption**.
# - Using GitLab you can also store on external services like S3 (?).
# - But **GitHub has a strong limit on storage and bandwith consumption**, so that you have to buy more storage if you files and the number of transfers is not small. 
# - Thus, Git-LFS might be best for files that do not exceed 1 GB and do not change too much. 
# - Details:
#     - https://about.gitlab.com/pricing/
#     - https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage and https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-storage-and-bandwidth-usage

# %% [markdown] slideshow={"slide_type": "slide"}
# **Resources**
# - https://git-lfs.github.com/
# - https://about.gitlab.com/blog/2017/01/30/getting-started-with-git-lfs-tutorial/
# - https://github.com/git-lfs/git-lfs/wiki/Tutorial
# - https://github.com/git-lfs/git-lfs/tree/main/docs/man
# - https://www.youtube.com/watch?v=YQzNfb4IwEY
#
# **Similar tool**
# - [Git Annex](https://git-annex.branchable.com/) which can be self hosted

# %% [markdown] slideshow={"slide_type": "slide"}
# ## DVC

# %% slideshow={"slide_type": "-"}
embed_website("https://dvc.org/")

# %% [markdown] slideshow={"slide_type": "slide"}
# - DVC **extends Git (and Git-LFS) for data science usage**. 
# - Probably the most popular tool for file versioning.
# - **Its commits are pointers to data sets**.
#     - The actual data is added to .gitignore and thus not commited to Git but to a storage location
#     - For each data that is put into a storage location, DVC creates .dvc files wich are pointers to the data that are tracked by Git
# - **Storage can be local or a remote storage like S3, Google drive,** ...
# - Other features:
#     - Pipelines which connect versioned datasets, model and code
#     - Compare metrics and view plots across different commits 
#     - CICD
#     - Python API: https://dvc.org/doc/api-reference

# %% [markdown] slideshow={"slide_type": "slide"}
# DVC is a **good solution** 
# - To keep data or other binary files tightly in **sync with Git** and for sharing data.
# - For **smaller projects** where speed and scaling is not important.
# - When you cannot or don't want to version a database.
# - When versioning sql queries as a means to version data is not possible.
#
# We will later discuss data versioning with DVC in more detail.
