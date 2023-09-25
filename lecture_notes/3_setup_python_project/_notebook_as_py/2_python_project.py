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

# %% slideshow={"slide_type": "notes"}
from dsc.notebook import embed_website
from dsc.setup_python_project.sys_path import SysInfo
sys_info = SysInfo()

# %% [markdown] slideshow={"slide_type": "slide"}
# # Agenda
# - In this chapter we discuss how to setup your Python project after you have created a Git repo and a virtual environment
# - In particular, we will use [PyScaffold](https://github.com/pyscaffold) in combination with the [datascience template](https://github.com/drivendata/cookiecutter-data-science/) of [Cookiecutter](https://www.cookiecutter.io/) so that
#     - Obtain a sound folder structure for your project so that you know where to put
#         - Data
#         - Notebooks
#         - Modules
#         - Reports
#         - ...  
#     - You can easily pip-install your project package in editable mode
# - We talk about how you can rapidly develop prototypes and conduct analyses in Jupyter notebooks and when you should modularize your code into modules or a package.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Using PyScaffold for setting up your Python project

# %% [markdown] slideshow={"slide_type": "slide"}
# ## What is PyScaffold?
# <!-- A Scaffold is a project template a.k.a. bootstrap, boilerplate or skeleton  -->
# From the [website](https://pyscaffold.org/en/stable/):
#
# - PyScaffold is a **project generator** for bootstrapping high-quality Python packages, ready to be shared on PyPI and installable via pip. 
# - PyScaffold incentives its users to use the **best tools and practices** available in the Python ecosystem.
#
#     - A generated project will contain **sane default configurations** for 
#         - Setuptools (the de facto standard for building Python packages)
#         - Sphinx (the one & only Python documentation tool)
#         - Pytest and tox (most commonly used Python testing framework & task runner)
#     -  PyScaffold can also bring **pre-commit** into the mix to run a set of prolific linters and automatic formatters in each commit in order to adhere to common coding standards like pep8 and black.

# %% [markdown] slideshow={"slide_type": "fragment"}
# "Using PyScaffold is like having a Python Packaging Guru, who has spent a lot of time researching how to create the best project setups, as a friend that is helping you with your project." &#128515;

# %% [markdown] slideshow={"slide_type": "slide"}
# - Moreover, there is a [PyScaffold extension tailored for Data Science projects](https://github.com/pyscaffold/pyscaffoldext-dsproject) 	&#128522;
# - This extension creates a folder structure that is inspired by [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science). 
# - In contrast to cookiecutter-data-science alone it
#     1. Advocates a proper Python package structure that can be shipped and distributed.
#     2. Uses a conda environment instead of something virtualenv-based and is thus more suitable for data science projects.
#     3. More default configurations for Sphinx, pytest, pre-commit, etc. to foster clean coding and best practice.
# - Moreover, the scripts folder is added (cookiercutter-data-science proposes to put scripts inside src/package, which I would not suggest)
#
# <!-- Cookiecutter is a tool that allows the definition of templates 
# for a broad range of software projects. On the other hand, PyScaffold focus is on developing distributable Python packages (exclusively) in a simple way
# -->

# %% [markdown] slideshow={"slide_type": "slide"}
# - In this course, we will only use a subset of the features that the standard PyScaffold (DataScience) provides:
#     - A sound folder structure
#     - Using it to easily install the project package in editable mode
#     - Settinp up documentation (will be discussed when we talk about good code)
#     - Setting up pre-commit hooks (will be discussed when we talk about collaboration)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Installing PyScaffold and creating a project with PyScaffold
# <a id="pyscaffold_test"></a>

# %% [markdown] slideshow={"slide_type": "-"}
# - Cd to the parent directory of this project.
# - Run ```conda create -n pyscaffold_test -c conda-forge python=3.10 pyscaffoldext-dsproject pip pandas jupyter matplotlib```.
# <!-- The Python version is pinned to 3.10 because when a new version of Python is released, some packages might not be immediately compatible with this new version (according to their metadata). But you investigate whether not pinning the version works (which should be the case in 99.9% of the cases) -->
# - Activate the pyscaffold_test environment.
# - Run ```putup --dsproject pyscaffold_test``` to create a directory called pyscaffold_test which is set up by PyScaffold.
#     - If you use a unix-based OS, you can also add the flag ```--no-tox``` to the previous command and build your documentation later with make.
# - Note: You can only create a project with PyScaffold if the directory is not tracked by Git.
#     - If the parent directory of `dsc` is tracked by Git
#         - Either move the `dsc` project to a different directory that is not tracked by Git and run the previous  ```putup``` command in the new parent directory
#         - Or cd into the root of the Git repo that tracks the parent directory of `dsc` and run ```rm -rf .git``` to delete the Git repo (only do this if you don't need the Git repo!)

# %% [markdown] slideshow={"slide_type": "slide"}
# The resulting folder structure should look like this
#
# ```
# ├── AUTHORS.md              <- List of developers and maintainers.
# ├── CHANGELOG.md            <- Changelog to keep track of new features and fixes.
# ├── CONTRIBUTING.md         <- Guidelines for contributing to this project.
# ├── Dockerfile              <- Build a docker container with `docker build .`.
# ├── LICENSE.txt             <- License as chosen on the command-line.
# ├── README.md               <- The top-level README for developers.
# ├── configs                 <- Directory for configurations of model & application.
# ├── data
# │   ├── external            <- Data from third party sources.
# │   ├── interim             <- Intermediate data that has been transformed.
# │   ├── processed           <- The final, canonical data sets for modeling.
# │   └── raw                 <- The original, immutable data dump.
# ├── docs                    <- Directory for Sphinx documentation in rst or md.
# ├── environment.yml         <- The conda environment file for reproducibility.
# ├── models                  <- Trained and serialized models, model predictions,
# │                              or model summaries.
# ├── notebooks               <- Jupyter notebooks. Naming convention is a number (for
# │                              ordering), the creator's initials and a description,
# │                              e.g. `1.0-fw-initial-data-exploration`.
# ├── pyproject.toml          <- Build configuration. Don't change! Use `pip install -e .`
# │                              to install for development or to build `tox -e build`.
# ├── references              <- Data dictionaries, manuals, and all other materials.
# ├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
# │   └── figures             <- Generated plots and figures for reports.
# ├── scripts                 <- Analysis and production scripts which import the
# │                              actual PYTHON_PKG, e.g. train_model.
# ├── setup.cfg               <- Declarative configuration of your project.
# ├── setup.py                <- [DEPRECATED] Use `python setup.py develop` to install for
# │                              development or `python setup.py bdist_wheel` to build.
# ├── src
# │   └── PYTHON_PKG          <- Actual Python package where the main functionality goes.
# ├── tests                   <- Unit tests which can be run with `pytest`.
# ├── .coveragerc             <- Configuration for coverage reports of unit tests.
# ├── .isort.cfg              <- Configuration for git hook that sorts imports.
# └── .pre-commit-config.yaml <- Configuration of pre-commit git hooks.
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# - Note that PyScaffold automatically turns pyscaffold_test into a git repo (please rename the initial branch).
# - The folders data, models, references, reports/figures are ignored by Git
# - Some folder also contain templates that you can investigate
# - You should also edit the environment.yml and files in uppercase letters, i.e.,README.md, AUTHORS.md, CONTRIBUTING.md, and LICENSE.txt
# - All configuration is done in setup.cfg

# %% [markdown] slideshow={"slide_type": "slide"}
# Why is it important to use a tool like PyScaffold that setups a common folder structure that everybody use?

# %% [markdown] slideshow={"slide_type": "fragment"} tags=["solution"]
# - Starting a project without a template is cumbersome
#     - Everyone thinks differently and has their own idea of how files and folders should be organized.
#     - If you collaborate with others you have to make an agreement about how the project should look like.
#     - Still, it is possible that your project folder becomes a dumping ground for files because this agreement is never done or not taken into account.
# - Making these agreements for each project individually is time-consuming and may result in different agreements and thus different folder structures.
# - Imagine booting your computer and the folder structure is different every time.... &#128556;&#128556;&#128556;

# %% [markdown] code_folding=[] slideshow={"slide_type": "slide"} tags=["solution"]
# - Using a sensible template for a project
#     - Saves time and helps you focus on the project without having to create folder and files manually from scratch every time
#     - Makes it easier for developers to do things right and enforce best practises by providing structure
#     - Recudes the likelihood that the project folder becomes a dumping ground for files
#     - Lowers the entry level for new collaborators
#     - Allows to expand the folder structure without having to reorganize it from time to time
# - Using one template for all projects with the same underlying structure (e.g., data science, web application, ...)
#     - Standardizes the workflow of projects and increases consistency and reproducibility across projects
#     - Helps developers to quickly find resources (modules, scripts, documentation...) with confidence
#     - Helps developers to store files in the right place, again with confidence
#
# <!-- Think about the Filesystem Hierarchy Standard for Unix-like systems
#     - The /etc directory has a very specific purpose, as does the /tmp folder, and everybody (more or less)
# agrees to honor that social contract.
# Not all developers start with a project, new developers may join the project when it is already running or junior people might work on the project, providing them guidelines with templates is very useful -->

# %% [markdown] slideshow={"slide_type": "slide"}
# # Structuring your code

# %% [markdown] slideshow={"slide_type": "-"}
# - A sound project template provides a good basis for your project because it provides guidelines how to structure your code into notebooks, scripts and modules
# - However, these guidelines are not strict and you have to decide how to structure your code
# - When doing data science, you might often start with a simple script or a Jupyter notebook to prototype quickly and do some analyses
# - But when your code grows it's important to think more about the structure of your code 
# - In case of a Python, you can modularize your project code into scripts and different modules which can be organized in a package
# - Sometimes you even want to reuse your project code for other projects and make it installable with pip
# - On the following slides, we will consider these points in more detail

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Resources
# - [Scrips, Modules, Packages, Libraries](https://realpython.com/lessons/scripts-modules-packages-and-libraries/)
#     - [How to run your Python script](https://realpython.com/run-python-scripts/)
#     - [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages)
# - Code structure
#     - [PyScaffold](https://florianwilhelm.info/2018/11/working_efficiently_with_jupyter_lab/)
#     - [Structuring Your Project](https://docs.python-guide.org/writing/structure/)
# - Jupyter notebooks 
#     - [A Beginner’s Tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
#     - [Contributed extensions](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html)
#     - [Conda environment and package access extension](https://github.com/Anaconda-Platform/nb_conda): Useful to change the kernel of the notebook.
#     - [NbConvert](https://nbconvert.readthedocs.io/en/latest/index.html): In contrast to Jupytext this includes the cell outputs.
#     - [Jupytext](https://jupytext.readthedocs.io/en/latest/install.html): Does not include the cell outputs. Useful for notebook versioning.
#     - [NbFormat](https://nbformat.readthedocs.io/en/latest/): Can be used to programmatically create notebooks.
# - [Comparing data dashboarding tools and frameworks](https://www.datarevenue.com/en-blog/data-dashboarding-streamlit-vs-dash-vs-shiny-vs-voila)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Jupyter Notebooks: The good, the bad, and the ugly.

# %% [markdown] slideshow={"slide_type": "-"}
# - Jupyter notebooks are heavily used in the data science community (industry, science, kaggle)
# - Notebooks are wonderful for prototyping, exploration, analyses (including visualizations) and sharing results.
#     - Combing markdown with source code of many programming languages
#     - Seperating of code blocks into cells
#     - Plotting
#     - "Interactive debugger"
# - There are even companies that 
#     - Use Jupyter notebooks in production systems, e.g., [Netflix](https://netflixtechblog.com/notebook-innovation-591ee3221233)
#     - Provide [platforms](https://www.databricks.com/solutions/data-science) that productionize notebooks 
# <!-- (but if you don't need Spark, Databricks might be too expensive)-->
# - However, the use of Jupyter notebooks for code that is actually deployed and runs in production is rather the exception.  

# %% [markdown] slideshow={"slide_type": "fragment"}
# <div align="center">
# And there are good reasons for that!
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# <div>
# <img src="./figures/all_code_in_notebook_meme.png" alt="Notebook meme" width=1000/>
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# The (in)famous talk ["I don't like notebooks"](https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/) given by Joel Grus at JupyterCon 2018 highlights possible drawbacks of Jupyter notebooks for coding.

# %% slideshow={"slide_type": "-"}
# embed_website("https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/")  # activating this might lag the presentation

# %% [markdown] slideshow={"slide_type": "slide"}
# <a id="nb_drawbacks"><a/>   
# - In the talk the following **drawbacks of Jupyter notebooks** are mentioned:
#     1. **Reproducibility and hidden states** are a concern (slides 23, 24, 31, 42, 73-74)
#         - Re-running or running cells in different order give you much flexibility for exploring
#         - But it can be difficult to reproduce or understand results
#     1. Inspiring bad coding habits and **discouraging good coding habits** (slides 45-59, 76-90)
#         - No functions, abstractions or OOP, no writing of modules/packages
#         - Mixing "library" and "excecution" code
#         - Code is often not DRY and resuable
#         - No testing
#         - No type annotations
# <a id="ide_features"><a/> 
#     1. **Powerful features of IDEs are missing** (slides 60-70, this can be somewhat addressed in the meantime by opening a notebook directly in VSCode or PyCharm)
#         - Autosuggestion
#         - Automatic highlighting of possible errors by linters
#         - Code formatting using, e.g., black
#         - Type annotation checks
#         
# <!-- - The author also mentions in his notes that the Jupyter ecosystem consists of tools to work around people's bad habits so they don't have to fix them -->
#

# %% [markdown] slideshow={"slide_type": "slide"}
# - Drawbacks not mentioned in the talk:
#     - **Code versioning is difficult** (in the meantime, this can be addressed with Jupytext)
#     - **Collaboration is difficult** (everybody working on the same notebook? merge conflicts?)
# - See also [here](https://www.reddit.com/r/datascience/comments/nf47se/does_netflix_use_jupyter_notebooks_in_production/), [here](https://www.youtube.com/watch?v=9Q6sLbz37gk) and [here](https://www.reddit.com/r/datascience/comments/yfsxrn/a_critical_reflection_of_jupyter_notebooks/)
# for further discussions about using notebooks (in production).

# %% [markdown] slideshow={"slide_type": "slide"}
# - Jupyter notebooks and its extensions are tools. 
#     - Many **projects try to extend Jupyter notebooks and make them ready for collaboration and production** (or e.g., writing books with them).
#     - Like any tool you can use a notebook for a purpose it was not designed for: ["If Your Only Tool Is a Hammer Then Every Problem Looks Like a Nail"](https://en.wikipedia.org/wiki/Law_of_the_instrument).
# - Much "data science" education appears to be limited to showing beginners how to use notebooks but does not develop their programming skills or teach best practices.
# - Instead of extending and productionizing notebooks **I think it makes more sense to empower data scientists to build production-ready code the way it is typically done in other areas**
# - Especially if you project becomes more mature or complex it is beneficial to move away from notebooks and modularize your
#   code and factor it into a package/module
# - When the time comes, you'll be much closer to production-grade code and can rather ensure scalability, maintainability and resiliency that long-lived production code needs to support

# %% [markdown] slideshow={"slide_type": "slide"}
# - **This does not mean that you shouldn't use notebooks at all**...
#     - It's perfectly fine to use notebooks for analyses and sharing insights or doing reports 
#     - It's also okay to use them to execute code as long as it is 
#       just a wrapper for functions/objects that are imported and then executed
#     - Notebooks are like an interactive debugger and can be used to rapidly prototype
#     - Using pandas without notebooks can be painful due to pandas inconsistencies
#     - Not all code is meant to be "production code"
# - But you shouldn't put all of your code in one notebook
# - Also note that some IDEs ([VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks), PyCharm) directly support notebooks
# - VS Code also provides an [interactive mode](https://code.visualstudio.com/docs/python/jupyter-support-py) that resembles notebooks but works with .py files
#     - The code of the .py file can be separated into Jupyter-like cells
#     - Output is sent to the interactive terminal
#     - Since the code is written in a .py file possible [drawbacks](#nb_drawbacks) of notebooks are avoided
#         - Can use all [features that VS Code provides for .py files](#ide_features)
#         - Outputs are not tracked by Git

# %% [markdown] slideshow={"slide_type": "slide"}
# ### How to structure notebooks?

# %% [markdown] slideshow={"slide_type": "-"}
# - In many cases, it's a good idea to start your data science project with Jupyter notebook to prototype quickly and do some analyses
# <a id="reco"> </a>
# - I recommend that you
#     - Use the [table of contents extension](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/toc2/README.html) (which is also included by the [jupyter_contrib_nbextensions](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html) which provides other useful extension)
#     - Separate your code not only by cells but by creating sections using markdown cells and headings
#     - Place all imports at the beginning of the notebook (unless the import is only temporary for a non-persistent analysis)
#     - Place all functions right after the imports
#     - Do not scatter variables, that determine the output of notebook cells, across many different cells, but place them at the beginning of the notebook, e.g., after the functions
#     - Only overwrite variables if new content is added to a the underyling object but not removed, e.g., do not drop cells from a dataframe and assign it to the same variable name
#     - All these steps make your notebook more understable and simplifies the modularization of notebooks cells into functions and modules later on (if required)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Exercise
# 1. Move the notebook  
# [```dsc/lecture_notes/2_setup_python_project/code_structure/0_messy_notebook.ipynb```](./code_structure/0_messy_notebook.ipynb)  
# to the notebooks folder of your **pyscaffold_test project** that you have created [before](#pyscaffold_test).
# 1. Rename the notebook to ```pyscaffold_test/notebooks/1_[<name>]_structured_notebook.ipynb```,  
# where ```[<name>]``` is a identifier of your name, e.g, your initials.
# 1. Copy ```dsc/data/dsc.db``` to ```pyscaffold_test/data/raw/dsc.db```.
# <!-- - Add the folder ```pyscaffold_test/data/output```. -->
# 1. Activate the corresponding environment of the **pyscaffold_test project** and cd into the **pyscaffold_test project**.
# 1. Start a Jupyter notebook server, e.g., by running ```jupyter notebook``` in the terminal. Note that the notebook is running in the environment that is activated.
#
# 1. Make the resulting notebook ```pyscaffold_test/notebooks/1_[<name>]_structured_notebook.ipynb``` runnable by
#     1. Adjusting the connection to the database.
#     1. Writing the output of this notebook to the folder ```pyscaffold_test/models/predictions```.
# 1. Make this notebook more structured by considering the previously mentioned [recommendations](#reco).

# %% [markdown] slideshow={"slide_type": "subslide"}
# Some tips...
# - You can convert a code cell to a markdown cell in a Jupyter notebook by switching to command code (press esc) and the pressing ```m```
# - To write a heading in markdown use a hash \# or multiple hashes in front of the text
# - After you have installed the [jupyter_contrib_nbextensions](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html), you have to restart the notebook server so that the GUI is available at the top of the start page of the notebook server (look for Nbextensions and click it and then enable ```Table of Contents (2)```)
#     - In case the GUI does not appear (Windows?), you can install the extension via the terminal using ```jupyter nbextension enable toc2/main```
# - The table of contents is only available in the browser, but not in an IDE

# %% [markdown] slideshow={"slide_type": "slide"}
# #### Solution
# - If the project `dsc` and pyscaffold_test are located in the same folder, run ```python3 -m  dsc.setup_python_project.pyscaffold_test``` to obtain a proposal for such a restructured notebook given by ```pyscaffold_test/notebooks/1_fs_structured_notebook.ipynb```. 
# - Otherwise, run ```python3 -m  dsc.setup_python_project.pyscaffold_test [<path>]``` where ```[<path>]``` is the location of pyscaffold_test.
# - Note that 
#     - The table of contents have been enabled for this notebook, see the first cells for instructions how to enable the table of contents.
#     - Markdown cells haven been added to the notebook to explain its flow.
#     - All imports have been placed at the beginning of the notebook in the section Setup/Imports
#     - All functions have been placed right after the imports in the section Setup/Functions
#     - Variables that determine the cell outputs are now collected in the section Parameters
#     - Data processing is done in the section Data
#     - Data fitting and predicting is perfomred in the section Model
# - Note that these are only suggestions. It is not a problem if your proposal is different as long as it is structured &#128521;
# - You don't know if your proposal is structured? Ask me or your fellow students.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Modules and Packages
# - When you notebook further evolves, it makes sense to put (some) variables, functions and classes into a module.
# - Therefore, let's have a look at Python modules/packages and how to import them.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Modules

# %% [markdown] slideshow={"slide_type": "-"}
# - Import statements are typically the first thing you see at the top of any Python file.
# - The ```import [<module|package>]``` statement is used to import other .py files into the current interpreter session, e.g., the following lines import the built-in module sys and the third-party module numpy with the alias np
# ```python
#     import sys
#     import numpy as np
# ```
# - It can be used to re-use code and share it among different files and projects.
# - Note that a module is cached if it is imported, meaning changes to the module are not reflected in the Python interpreter unless
#     - You start a new Python session/restart the Jupyter kernel
#     - Use Jupyters [autoreload](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html) magic, click [here](https://www.wrighters.io/using-autoreload-to-speed-up-ipython-and-jupyter-work/) for an illustration
#     - Reload the module using the built-in importlib.reload
# - Modules can also be run as script.
# - Any .py-file is a module.
# - Several modules can be organized in a package.

# %% [markdown] slideshow={"slide_type": "slide"}
# - Consider the following content of example.py
# ```python
#     import sys
#
#     a = 1
#     def fun():
#         return 2
# ```
# - [Assuming the module example can be imported](#import_modules), we can access its content as follows
#     - Import the module and access its attributes via dot notation 
#     ```python
#     import example
#     example.sys  # returns the sys module
#     example.a  # returns 1
#     example.fun()  # returns 2
#     ```
#     - Directly import attributes using a "from import"
#     ```python
#     from example import sys, a, fun
#     sys  # returns the sys module
#     a  # returns 1
#     fun()  # returns 2
#     ```

# %% [markdown] slideshow={"slide_type": "slide"}
# #### When can a module be imported?
# <a id="import_modules"></a>

# %% [markdown] slideshow={"slide_type": "-"}
# - Every .py-script is a Python module and can be imported provided it is **accessible via sys.path**.
# - The following modules can always be imported
#     - **Built-in** modules because pythonX.YY is always on sys.path.
#     - **Pip- or conda-installed modules** because site-packages is always on sys.path.
#     - Moreover, packages that have been pip-installed in **editable mode** appear on sys.path.
# - Depending on how you invoke Python, (non-built-in or non-installed) modules might be accessible via sys.path or not.

# %% [markdown] slideshow={"slide_type": "slide"}
# - If you start an **interactive Python session** using ```python3``` (or import a module during an interactive Python session) then 
#     - The working directory from which the session has been started or (the module is imported) is added to sys.path
#     - ```''``` appears on sys.path, implying that modules inside the current working directory (accessible via os.getcwd()) can be imported
# - Note that an interactive Python session is started when you start a Jupyter notebook or run ```jupyter console```

# %% slideshow={"slide_type": "-"}
sys_info();  # information about sys.path of this interactive Python session

# %% [markdown] slideshow={"slide_type": "slide"}
#  <a id="sys_path_run"></a>
#  - If you **run a Python program** the directory in which the program is located is put on sys.path

# %% slideshow={"slide_type": "-"}
!cd ../.. && python3 src/dsc/setup_python_project/sys_path.py  # information about sys.path when a program is run

# %% [markdown] slideshow={"slide_type": "fragment"}
# - If you **run a Python module as a script** using the ```m``` flag the directory from which the programm is called is put on sys.path (in this case the directory of this notebook)

# %% slideshow={"slide_type": "-"}
!cd ../.. && python3 -m dsc.setup_python_project.sys_path  # information about sys.path when a module is run as a script

# %% [markdown] slideshow={"slide_type": "slide"}
# - If you invoke Python with the ```c``` flag (e.g., ```python3 -c "import sys; print(sys.path)"```) then ```''``` is added to sys.path.
# - If you cannot import a module because it is not on sys.path, you can append its corresponding folder to sys.path, e.g.,
# ```python
#     import sys
#
#     sys.path.append("path_of_new_folder")  # add path_of_new_folder to sys.path
# ```
# - Alternatively, you can change the working directory if it is on sys.path, e.g., 
# ```python
#     import os
#
#     os.setcwd("..")  # set working directory to previous parent directory
# ```
# - However, this is more like a quick fix and not robust (moving files breaks imports).
# - It is better to pip-install the package in editable mode (see [later](#editable)).
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Exercise

# %% [markdown] slideshow={"slide_type": "-"}
# 1. Cd into your pyscaffold_test project that you have created [before](#pyscaffold_test).
# 1. Make a copy of  
# ```pyscaffold_test/notebooks/1_[<name>]_structured_notebook.ipynb``` 
# and rename it to  
# ```pyscaffold_test/notebooks/2_[<name>]_structured_notebook_with_module.ipynb```, where ```[<name>]``` is a identifier of your name.
# 1. Think about what cells could be summarized (and possibly generalized) into functions that could be put into a module.
# 1. Create the companion module  
# ```pyscaffold_test/notebooks/companion_module.py```  
# and use it in  
# ```pyscaffold_test/notebooks/2_[<name>]_structured_notebook_with_module.ipynb``` 
# accordingly.

# %% [markdown] slideshow={"slide_type": "slide"}
# #### Solution
# - Run ```python3 -m  dsc.setup_python_project.pyscaffold_test``` to obtain a proposal for such a restructured notebook and the companion module located in  
# ```pyscaffold_test/notebooks/fs_companion_module.py``` and  
# ```pyscaffold_test/notebooks/2_fs_structured_notebook_with_module.ipynb```
# - Note that
#     - The content of section Setup/Functions has been transferred to the companion module which is imported in the section Setup/Imports
#     - In addition,
#         - Operations that load or change the data have all been put into the companion module
#         - Plotting functions have been put into the companion module
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Packages
# - A package is a directory that contains multiple modules (or subpackages) and helps to organize them.
# - For data science projects, it might be useful to use separate your package into the following modules
#     - data
#     - features
#     - splits
#     - models
#     - visualization
#     - ...

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Structure
# - A **regular** package is a folder that contains a file named ```__init__.py``` and modules or (sub)packages, e.g.,
# ```python
# my_package/
#         __init__.py
#         module_a.py
#         sub_package/
#                 __init__.py
#                 module_b.py
#                 module_c.py
#                 sub_sub_package/
#                         __init__.py
#                         module.d
# ```
# - If you import a package, ```__init__.py``` is executed. This file can be empty. Each subpackage should have a ```__init__.py```.
# - With this package structure (and provided the package is importable):
#     - ```from my_package import module_a``` imports module_a
#     - ```from my_package.sub_package.sub_sub_package import module_d``` imports module_d
#     - ```from my_package.sub_package.module_b import attr``` imports the attribute attr from module_b

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Pip-install a package in editable mode
# <a id="editable"></a>

# %% [markdown] slideshow={"slide_type": "-"}
# - To make a package importable, its parent directory must be located on sys.path.
# - If you put your package in the directory of the notebook (or script) on which you are working on, the package can be imported.
# - However, a single directory containing all notebooks and packages/modules becomes messy when your project evolves.
# - Restructuring you notebooks and modules requires adjusting sys.path or the working directory manually each time, which is not a good idea.
# - Therefore, I recommend to pip-install your package in **editable mode** so that it can always be imported within the corresponding activated environment.
# - If a project has been set up by PyScaffold, you can pip-install a package in editable mode using ```pip install -e [path]``` where path is the root folder of your project.
# - Note
#     - A package that is installed in editable mode is not put into the site-packages directory but directly on sys.path.
#     - There are some requirements to be satisfied so that you can pip-install a package, PyScaffold takes care of this.
#     - In an **environment.yml** you can specify that a package should be pip-installed in editable mode (e.g., see the environment.yml of the `dsc` project) when the conda environment is created

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Exercise

# %% [markdown] slideshow={"slide_type": "-"}
# 1. Cd into your pyscaffold_test project that you have created [before](#pyscaffold_test) and activate the corresponding environment.
# 1. Make a package out of your ```pyscaffold_test/notebooks/companion_module.py```
#     1. Put all data-related functionality of this module into the file  
#     ```pyscaffold_test/src/pyscaffold_test/data.py```
#     1. Put all model-related functionality of this module into the file  
#     ```pyscaffold_test/src/pyscaffold_test/model.py```
#     1. Put all plot-related functionality of this module into the file  
#     ```pyscaffold_test/src/pyscaffold_test/plot.py```
#     1. Pip install the resulting package in editable mode
# 1. Make a copy of  
# ```pyscaffold_test/notebooks/2_[<name>]_structured_notebook_with_module.ipynb```,    
# rename it to  
# ```pyscaffold_test/notebooks/3_[<name>]_structured_notebook_with_package.ipynb```,  
# where ```[<name>]``` is a identifier of your name,   
# and import the package accordingly.
# 1. Save a copy of both notebooks in the root directory of pyscaffold_test.
# 1. Execute the first code cell in which modules are imported. What do you observe?

# %% [markdown] slideshow={"slide_type": "slide"}
# #### Solution
# - Run ```python3 -m  dsc.setup_python_project.pyscaffold_test``` to obtain a proposal for such a package and the first notebook located at
#     - ```pyscaffold_test/src/pyscaffold_test_fs``` (if this package cannot be imported, run ```pip install -e .``` again)
#     - ```pyscaffold_test/notebooks/3_fs_structured_notebook_with_package.ipynb```
# - Note that the only difference between 3_fs_structured_notebook_with_package.ipynb and 2_fs_structured_notebook_with_module.ipynb is the first code cell where imports from the the companion module
# are replaced by imports from the pyscaffold_test package.
# - ```pyscaffold_test/2_fs_structured_notebook_with_module.ipynb``` does not run because the companion module is not on sys.path anymore (the working directory is ```pyscaffold_test```, but the module is located in the folder ```pyscaffold_test/notebooks```)
# - ```pyscaffold_test/3_fs_structured_notebook_with_package.ipynb``` runs everywhere because psyscaffold_test_fs is in a directory which has been pip-installed in editable mode (assuming the environment in which it has been installed is activated)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Scripts

# %% [markdown] slideshow={"slide_type": "-"}
# - A script is a Python file that should be run directly by using ```python3 [<script>]```, where ```[<script>]``` is the path of the script.
# - You should separate different steps of your project (e.g., training, prediction) into several scripts
# - For handing over your project code it is required that you provide
#     - A script for training a model that can be called from the command line which
#         - Loads a specified dataset
#         - Transforms the data and engineers the features
#         - Trains a model
#         - Stores the trained model (e.g., using MlFlow)
#     - A script for predicting data that can be called from the command line which
#         - Loads a trained model (e.g., using MlFLow)
#         - Predicts data on the basis of the specified dataset
#         - Stores the predicted data
#
#

# %% [markdown] slideshow={"slide_type": "slide"}
# - Scripts should be run from the **project root**. 
#     - In this case, the working directory of the executed script is the project root. 
#     - The location of the script is available via sys.path if you run the script via ```python3 [<script>]```.
# - If you run a script from a different directory it probably won't complete.
# - In general, scripts that are specific to your project should not be put into a package but in the ```scripts``` folder.
# - Cookiecutter recommends that models and their predictions should be stored in ```models``` and we will do so in this chapter.
#     - Personally, I would store models and their predictions in ```data```.
# - There are two challenges that you have to adress when you split a notebook (or script) into separate scripts
#     - How to transfer data from one script to another?
#     - How to execute scripts in a specific order?
#     - How to write the command line interface?
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Orchestration
# - In order to transfer data from one program to another you need to load and store data. For this,
#     - You can write your own functions
#     - Use tools (e.g. Mlflow)
# - Moreover, if your pipeline gets more complicated and consists of several scripts that must be run in a specific order it is useful to use tools that orchestrate this workflow.
# - There are a lot of tools to manage workflows
#     - Make
#     - Airflow
#     - AWS step functions
#     - Metaflow
#     - ...
# - For this course, it is sufficient to run your scripts manually from the command line.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Comand line interface
# - The **command line interface** determines how the user interacts with a script and determines its output.
# - For instance, the unix command ```ls -a ~``` passes the flag ```a``` and the path of the home directory ```~``` to list directories and files of the home directory, including hidden objects.
# - There are several tools available in Python to simplify the writing of command line interfaces.
#     - [argparse](https://docs.python.org/3/library/argparse.html) (built-in): Gets the job done but pretty verbose and rather akward to use
#     - [click](https://click.palletsprojects.com/en/8.1.x/) (not maintained): Uses decorators for parsing command-line arguments
#     - [docopt](https://github.com/docopt/docopt) (not maintained): Implemented in several languages. Parses docstrings to parse command-line arguments
#     - [clize](https://clize.readthedocs.io/en/stable/index.html): Turns functions into command-line interfaces
# - For very simple programs, you can also just use ```sys.argv``` as it is done for the `dsc` package.

# %% [markdown] slideshow={"slide_type": "slide"}
# - To simplify the interaction with a script one can use configuration files
# - For instance, instead of running
# ```
# python3 fit.py \
#   --path2db="data/raw/data.db" \
#   --sql_query="SELECT * from broadcast" \
#   --storage_interim="data/interim/data_interim.csv" \
#   --model="xgboost"
# ```
# you could proceed as follows
# - In the same directory as fit.py, create cfg.py with the following content
# ```python3
# path2db = "data/raw/data.db"
# sql_query = "SELECT * from broadcast"
# storage_interim = "data/interim/data_interim.csv"
# model = "xgboost"
# ```
#   and import the module cfg into fit.py and use its attributes correspondingly in fit.py
# - You can then run the program using only ```python3 fit.py```
# - Edit cfg.py if you want to use a different configuration (or pass a different configuration file)
# - You can also pass some arguments to a program via the command line and the rest via a configuration file

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Running a module as a script
# - You can run a module 
#     1. As a normal Python script, e.g., ```python3 module_path```, where module_path is the path to a module, e.g., ```src/dsc/version_control/exercise_dvc.py```
#     2. **As a script** using its name by invoking the ```m``` flag, e.g., ```python3 -m module_name```, where module_name is the name of a module that is always located on sys.path, e.g., ```dsc.version_control/exercise_dvc```
# - Note that the sys.path of the program that is executed by 1. is [different](#sys_path_run) from a program executed by 2.!
# - However, in both cases the value of the Python variable ```__name__```  of the program is ```__main__```
# - If a module is imported by another program, the value of  ```__name__``` is the module's name
# - One can use this fact to execute some code only when the module is run as a program as the following example demonstrates

# %% [markdown] slideshow={"slide_type": "slide"}
# - Consider the following content of
#     - module_a.py
# ```python
#     print("Hello from module a.")  
#     
#     if __name__ == '__main__':
#         print("I am the main program.)
#     else:
#         print("I have been imported by another program.)
# ```
#     - module_b.py
# ```python
#     import module_a
# ``` 
# - Running ```python3 module_a.py``` or ```python3 -m module``` returns "Hello from module a. I am the main program"
# - Running ```python3 module_b.py``` returns "Hello from module a. I have been imported by another program"

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Running a package as a script
# - Recall that a package is just a folder containing an ```__init__.py``` file.
# - If you run a package, its ```__main__.py``` is executed (if available).

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Exercise
# - Make scripts of ```pyscaffold_test/notebooks/3_[<name>]_structured_notebook_with_package.ipynb```
#     - Create **```pyscaffold_test/scripts/cfg.py```** where you put your configuration that is imported in the following scripts.
#     - Create **```pyscaffold_test/scripts/fit.py```** to reproduce the part of ```pyscaffold_test/notebooks/3_[<name>]_structured_notebook_with_package.ipynb``` until a model has been fitted
#     - Also, update the pyscaffold_test package so that this script uses it along with the configuration to
#         - Store the *transformed dataframe* (after the column month has been added) as ```pyscaffold_test/data/interim/data_transformed.csv```
#         - Store *agg_df* as ```pyscaffold_test/data/processed/target_feature.csv```
#         - Store the *fitted model* as ```pyscaffold_test/model/models/model.pkl```
#     - Create **```pyscaffold_test/scripts/predict.py```** which reproduces the prediction of ```pyscaffold_test/notebooks/3_[<name>]_structured_notebook_with_package.ipynb```. For this purpose, use the configuration and an updated ```pyscaffold_test``` package to
#         - Load the *feature* from ```pyscaffold_test/data/processed/target_feature.csv```
#         - Load the *fitted model* from ```pyscaffold_test/model/models/model.pkl```
#         - Store the *predictions* in ```pyscaffold_test/model/predictions/prediction.csv```
#         
# - Note: To [debug](https://www.codementor.io/@stevek/advanced-python-debugging-with-pdb-g56gvmpfa) your script you can run ```python3 -m pdb [<script>]``` in the terminal or use your IDE

# %% [markdown] slideshow={"slide_type": "slide"}
# #### Solution
# - Run ```python3 -m  dsc.setup_python_project.pyscaffold_test``` to obtain a proposal for the scripts and the update package
# located at
#     - ```pyscaffold_test/src/fs_pyscaffold_test```
#     - ```pyscaffold_test/scripts_fs/cfg.py```
#     - ```pyscaffold_test/scripts_fs/fit.py```
#     - ```pyscaffold_test/scripts_fs/predict.py```
# - The scripts can then be run using
#     - ```python3 scripts_fs/fit.py```
#     - ```python3 scripts_fs/predict.py```
# - Moreover, you can get help for each script using the flag ```h```, e.g.,  ```python3 scripts_fs/fit.py -h```
# - Note that the solution gets the job done and is totally fine for this course but for more complex applications you might need more abstractions.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Reports, Dashboard and Apps
# - It is not unlikely, that your work is not done with the prediction, but you also have to report these predictions, build a dashboard, or provide an app with which (non-technical) stakeholders can interact and extract information.
# - There are a lot of tools that you can use to generate nice looking reports or dashboards
#     - Jupyter notebooks (in combination with [interactive browser controls](https://ipywidgets.readthedocs.io/en/stable/]) and [binder](https://jupyter.org/binder))
#     - [Quatro](https://quarto.org/): Scientific and technical publishing system for Python, R, and Julia.
#     - [Voila](https://github.com/voila-dashboards/voila): Turns Jupyter notebooks into standalone web applications.
#     - [Streamlit](https://streamlit.io/): Turns data scripts into shareable web apps in minutes.
#     - [Shiny](https://shiny.rstudio.com/): Build interactive web apps straight from R.
#     - [Plotly Dash](https://dash.plotly.com/): Low-code framework for rapidly building data apps in Python, R, and Julia.
# - If you want to build your own solution from the ground up then [Flask](https://flask.palletsprojects.com/en/2.2.x/), [Django](https://www.djangoproject.com/), or [FastAPI](https://fastapi.tiangolo.com/) might be helpful.

# %% [markdown] slideshow={"slide_type": "slide"}
# - It is not required that you include a report or dashboard in your code submission.
# - However, submitting functionality for creating a report or dashboard gets you some bonus points.
# - Running the script ```pyscaffold_test/scripts_fs/report.py``` creates a very simple Jupyter notebook report located at ```pyscaffold_test/reports/prediction.ipynb```
#

# %% [markdown] slideshow={"slide_type": "slide"}
# # Summary

# %% [markdown] slideshow={"slide_type": "-"}
# - In this chapter we discussed how to setup your Python project
# - Your Python project is determined by its folder structure, the virtual environment, and the corresponding Git repo
# - To obtain a sound folder structure and simplify the development of your code you can use the PyScaffold DS extension
# - You should start prototyping in a Jupyter notebook and then modularize your code into modules or a package when the project gets too complex or/and you are sure what features you need.
# - Pip-installing your package in editable mode greatly simplifies your working process because you don't have to worry about getting your own modules imported
# - The final product of your work should be accessible via scripts that can be run from the command line to execute different tasks

# %% [markdown] slideshow={"slide_type": "slide"}
# # Questions regarding the next topic (Good code)

# %% [markdown] slideshow={"slide_type": "-"}
# Click [here](https://partici.fi/49867347), or scan the QR code below, to answer the questions about setting up your Python project.
# <div align="center">
# <img src="./figures/p_3.png" alt="drawing" width="1200"/>
# </div>
# <div align="left">
# <div/>
