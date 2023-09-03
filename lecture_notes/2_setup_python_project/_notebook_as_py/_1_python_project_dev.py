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
# - Cd into a location that is not a git repo (e.g., the parent folder of this project).
# - Run ```conda create -n pyscaffold -c conda-forge pyscaffoldext-dsproject pandas```.
# - Activate the pyscaffold_test environment.
# - Run ```putup --dsproject --no-tox pyscaffold_test``` to create a directory called pyscaffold_test which is set up by PyScaffold.

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

# %% [markdown] slideshow={"slide_type": "notes"} tags=["note"]
# - Think about the Filesystem Hierarchy Standard for Unix-like systems
#     - The /etc directory has a very specific purpose, as does the /tmp folder, and everybody (more or less)
# agrees to honor that social contract.
# - Not all developers start with a project, new developers may join the project when it is already running or junior people might work on the project, providing them guidelines with templates is very useful

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
# <div>
# </div>

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
#     - Put imports in the first cell of the notebook (unless the import is only temporary for a non-persistent analysis)
#     - Do not scatter variables, that determine the output of notebook cells, across many different cells, but place them at the beginning of the notebook
#     - Do not overwrite variables 
#     - All these steps make your notebook more understable and simplifies the modularization of notebooks cells into functions and modules later on (if required)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Exercise
# - Move the notebook [```dsc
# - /lecture_notes/2_setup_python_project/code_structure/0_messy_notebook.ipynb```](./code_structure/0_messy_notebook.ipynb) to the notebooks folder of your pyscaffold_test project that you have created [before](#pyscaffold_test).
# - Have a look at the resulting notebook ```pyscaffold_test/notebooks/0_messy_notebook.ipynb```.
# - Make a copy of this notebook and rename it to ```pyscaffold_test/notebooks/1_structured_notebook.ipynb```.
# - Make this notebook more structured by considering the previously mentioned [recommendations](#reco).

# %% [markdown] slideshow={"slide_type": "fragment"}
# - A proposal for such a restructured notebook is given by [```dsc
# - /lecture_notes/2_setup_python_project/code_structure/1_structured_notebook.ipynb```](./code_structure/1_structured_notebook.ipynb).

# %% [markdown]
# - When you notebook further evolves, it makes sense to put (some) variables, functions and classes into a module.
# - Therefore, let's have a look at Python modules/packages and how to import them.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Modules and Packages

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
sys_info()  # information about sys.path of this interactive Python session

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
# #### Running a module as a program
# - You can run a module 
#     1. As a normal Python program, e.g., ```python3 module_path```, where module_path is the path to a module, e.g., ```src/dsc/version_control/exercise_dvc.py```
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
# ### Exercise

# %% [markdown] slideshow={"slide_type": "-"}
# - Cd into your pyscaffold_test project that you have created [before](#pyscaffold_test).
# - Make a copy of  
# ```pyscaffold_test/notebooks/1_structured_notebook.ipynb```  
# and rename it to  
# ```pyscaffold_test/notebooks/2_structured_notebook_with_module.ipynb```
# - In a first step, think about what functions could be put into a module called 
# ```pyscaffold_test/notebooks/2_structure_notebook_with_module_companion.py```
# - Create the companion module  
# ```pyscaffold_test/notebooks/structure_notebook_with_module_companion.py```  
# and use it in  
# ```pyscaffold_test/notebooks/structured_notebook_with_module.ipynb```  
# accordingly.
# - Note that the module doesn't start with "two" because modules must not start with an integer.

# %% [markdown] slideshow={"slide_type": "slide"}
# - A proposal for such a restructured notebook and the companion module is given in
# ```dsc_2022/lecture_notes/2_setup_python_project/code_structure```  
# by the two files 
#     - [```2_structured_notebook_with_module.ipynb```](./code_structure/2_structured_notebook_with_module.ipynb)
#     - [```structure_notebook_with_module_companion.py```](./code_structure/structured_notebook_with_module_companion.py)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Packages

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Structure
# - A package is a directory that contains multiple modules and helps to organize them
# - A **regular** package is a folder that contains a file named ```__init__.py``` and modules or (sub)packages, e.g.,
# ```python
# my_package/
#         __init__.py
#         __main__.py
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
# - If you run a package, ```__main__.py``` is executed. This file is optional.
# - With this package structure (and provided the package is importable):
#     - ```from my_package import module_a``` imports module_a
#     - ```from my_package.sub_package.sub_sub_package import module_d``` imports module_d
#     - ```from my_package.sub_package.module_b import attr``` imports the attribute attr from module_b

# %% [markdown] slideshow={"slide_type": "slide"}
# - For your data science projects, it might be useful to use the following subpackages
#     - data
#     - features
#     - models
#     - visualization
#     - ...

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Pip-install a package in editable mode
# <a id="editable"></a>

# %% [markdown]
# - To make a package importable, its parent directory must be located on sys.path.
# - If you put your package in the directory of the notebook (or script) on which you are working on, the package can be imported.
# - However, a single directory containing all notebooks and packages/modules becomes messy when your project evolves.
# - Restructuring you notebooks and modules requires adjusting sys.path or the working directory manually each time, which is not a good idea.
# - Therefore, I recommend to pip-install your package in **editable mode** so that it can always be imported within the corresponding activated environment.
# - You can pip.install a package in editable mode using ```pip install -e [path]``` where path is the folder where setup.py is located.
# - Note
#     - A package that is installed in editable mode is not put into the site-packages directory but directly on sys.path.
#     - There are some requirements to be satisfied so that you can pip-install a package, PyScaffold takes care of this.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Exercise

# %% [markdown] slideshow={"slide_type": "-"}
# - Cd into your pyscaffold_test project that you have created [before](#pyscaffold_test).
# - Make a package out of ```pyscaffold_test/notebooks/structured_notebook_with_module_companion.py```
#     - Put all data-related functionality of this module into the file  
#     ```pyscaffold_test/src/data.py```
#     - Put all model-related functionality of this module into the file  
#     ```pyscaffold_test/src/model.py```
#     - Pip install the resulting package in editable mode
# - Make a copy of  
# ```pyscaffold_test/notebooks/2_structured_notebook_with_module.ipynb```,    
# rename it to  
# ```pyscaffold_test/notebooks/2_structured_notebook_with_package.ipynb```,  
# and import the package accordingly

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Scripts

 # %%
 Due to this behaviour many people start creating their custom modules in
    the directory holding their notebook. Since JupyterLab is nice enough to set 
    the current working directory to the directory containing your notebook, 
    everything is fine at the beginning. But as the number of notebooks that 
    share common functionality imported from modules grows, the single directory 
    containing notebooks and modules will get messier as you go. 
The obvious split of notebooks and modules into different folders
or even organizing your notebooks into different folders will not work with 
this approach since then your imports will fail.

A Python package adheres a certain structure and thus can be shipped and installed by others


# %% [markdown]
# ## Summary

# %%
- There is no right solution (but maybe bad solutions)
- I recommend:
    - create a clean, isolated environment for every project = (new git repo, new...)
    - start prototyping in a notebook
    - always factor out functions/classes in module packages
    - keep your notebook concise (it should execute but not contain library code, library code: code that is imported and may be reused)

# %%
- PyScaffold: Your package is located at src/project, where project is the name of your project
- make a folder explanatory for notebooks and reports " For example, notebooks/exploratory contains initial explorations, whereas notebooks/reports is more polished work"
-> what if notebooks in these two folders need to import the same module? -> useful to install a package in editable mode
- It make sense to add the following directories to src/project (?)
    - data
    - features
    - models
    - visualization

# %%
motivate package by starting
with a project:
    notebook
    companion file (kevin)
what if it gets more complex
sys.path

1) notebook: at the top: config/variables that determine the output of your "program" scattered around cells
2) put config variables at the top
- a cell should contain code that later might be a function
3) companion file:  Don't write code to do the same task in multiple notebooks. If it's a data preprocessing task, put it in the pipeline at src/data/make_dataset.py
4) notebooks working dir auf root ändern, jedes mal (darf man nicht dateien verschieben oder man schreibt sich was das die root automatisch findet)
4) package

goal:
    no library code in notebook, only execution, or maybe config/setup in first cell
    
pipelines: use a script for orchestration or a notebook (we don't discuss tools for that like make or airflow etc.)

# %% [markdown]
# https://florianwilhelm.info/2018/01/ds_in_prod_packaging_ci/ auch gute quelle 
#     
# Being a data scientist does not free you from proper software engineering. **Of course most models start with a simple script or a Jupyter notebook maybe, just the essence of your idea to test it quickly. But as your model evolves, the number of lines of code grow, it’s always a good idea to think about the structure of your code and to move away from writing simple scripts to proper applications or libraries.**
#
# In case of a Python model, that means grouping functionality into different modules separating different concerns which could be organised in Python packages on a higher level. Maybe certain parts of the model are even so general that they could be packaged into an own library for greater reusability also for other projects. In the context of Python, a bundle of software to be installed like a library or application is denoted with the term package. Another synonym is distribution which is easily to be confused with a Linux distribution. Therefore the term package is more commonly used although there is an ambiguity with the kind of package you import in your Python source code (i.e. a container of modules).
#
# So what is now the key difference between a bunch of Python scripts with some modules and a proper package? A Python package adheres a certain structure and thus can be shipped and installed by others. Simple as it sounds this is a major advantage over having just some Python modules inside a repository. With a package it is possible to make distinct code releases with different versions that can be stored for later reference. Dependencies like numpy and scikit-learn can be specified and dependency resolution is automated by tools like pip and conda. 

# %% [markdown]
# https://florianwilhelm.info/2018/11/working_efficiently_with_jupyter_lab/
#     
# - sharing these notebooks is quite often an unnecessary pain. Notebooks that need you to tamper with the 
# PYTHONPATH or to start Jupyter from a certain directory for modules to import correctly.
# - The code in notebooks tends to grow and grow to the point of being incomprehensible. To overcome this problem, the only way is to extract parts of it into Python modules once in a while. Since it only makes sense to extract functions and classes into Python modules, I often start cleaning up a messy notebook by thinking about the actual task a group of cells is accomplishing. This helps me to refactor those cells into a proper function which I can then migrate into a Python module.
#
# At the point where you create custom modules, things get trickier. By default Python will only allow you to import modules that are installed in your environment or in your current working directory. Due to this behaviour many people start creating their custom modules in the directory holding their notebook. Since JupyterLab is nice enough to set the current working directory to the directory containing your notebook, everything is fine at the beginning. But as the number of notebooks that share common functionality imported from modules grows, the single directory containing notebooks and modules will get messier as you go. The obvious split of notebooks and modules into different folders or even organizing your notebooks into different folders will not work with this approach since then your imports will fail.
#
# This observation brings us to one of the most important best practices: **develop your code as a Python package**. A Python package will allow you to structure your code nicely over several modules and even subpackages, you can easily create unit tests and the best part of it is that distributing and sharing it with your colleagues comes for free. But creating a Python package is so much overhead; surely it’s not worth this small little analysis I will complete in half a day anyway and then forget about it, I hear you say. Well, how often is this actually true? Things always start out small but then get bigger and messier if you don’t adhere to a certain structure right from the start. About half a year later then, your boss will ask you about that specific analysis you did back then and if you could repeat it with the new data and some additional KPIs. But more importantly coming back to the first part of your comment, if you know how, it’s no overhead at all!
#
# -  If you are more into the Markdown syntax and thus rather want a README.md, you can install the pyscaffoldext-markdown extension for PyScaffold which adds a --markdown flag to PyScaffold’s putup command.
# - “The nice thing about standards is that you have so many to choose from”. The three most common docstring standards for Python are the default Sphinx RestructuredText, Numpy and Google style which are all supported by PyCharm.
# - After you have installed Sphinx you can build your documentation as HTML pages:
#
# conda install spinx
# python setup.py docs
#
# - **Why does PyScaffold ≥ 3 have a src folder which holds the actual Python package?**
# This avoids quite many problems compared to the case when the actual Python package resides in the same folder as your configuration and test files. A nice blog post by Ionel gives a thorough explanation why this is so. In a nutshell, the most severe problem comes from the fact that Python imports a package by first looking at the current working directory and then into the PYTHONPATH environment variable. If your current working directory is the root of your project directory you are thus not testing the installation of your package but the local package directly. Eventually, this always leads to huge confusion (“But the unit tests ran perfectly on my machine!”).
#
# Moreover, having a dedicated src directory to store the package files, makes it easy to comply with recent standards in the Python community (for example PEP 420).
#
#
#
# pyscaffold uses the src-layout
# https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout
#
# . Especially, structuring your files and directories the right way in order to build a Python package. Thereby, questions are addressed like “Where should my modules, documentation and unit tests go

# %%
Further links about notebooks and modularization (from https://www.reddit.com/r/datascience/comments/yfsxrn/comment/iu61tft/)
- https://ploomber.io/blog/nbs-myths/
- https://ploomber.io/blog/clean-nbs/
- https://ploomber.io/blog/nbs-production/

# %% [markdown] slideshow={"slide_type": "slide"}
# # Questions regarding next week's topic (Good code)

# %% [markdown] slideshow={"slide_type": "-"}
# Click [here](https://partici.fi/49867347), or scan the QR code below, to answer the questions about setting up your Python project.
# <div align="center">
# <img src="./figures/p_3.png" alt="drawing" width="1200"/>
# </div>
# <div align="left">
# <div/>
