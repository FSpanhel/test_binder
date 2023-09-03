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
import sys

from dsc.setup_python_project.virtual_environment import (
    conda_env,
    site_packages,
    python,
    pandas,
    path)

# %% [markdown] slideshow={"slide_type": "slide"}
# # Agenda
# - In this chapter, we will see why we should always use an virtual environment and what a virtual environment actually is.
# - Moreover, we address package management and environment management with conda.
# - Please start this notebook from an activated `dsc` environment.

# %% [markdown] slideshow={"slide_type": "slide"}
# # (Virtual) environments and package management

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Why should you use a virtual environment?
#
# - If you’re not specific, **pip (or other package managers) will place all Python packages that you install in a folder called site-packages located in your operating system’s global Python installation**.
# - Placing all your packages in the same folder as your global Python installation results in the following **issues**
#     - Your packages can **mix with system-relevant packages** that operating systems such as Linux or macOS use, resulting in unexpected side effects on your operating system’s normal behavior.
#     - Your packages might get overwritten and lost if you update your OS.
#     - You can only use **one version of a package**. 
#         - Quite frequently, projects require different package versions. 
#         - You have to overwrite the package by its required version whenever you switch projects.
#     - You might run into a **dependency conflict** when you want to install a new package.
#         - Package A might require package B v1.3. But the new package C might require package B v.1.0.
#     - It is **difficult to know what project requires which packages**.
#     - The previous three points make it **practically impossible to collaborate with others**. 
#     - You may not be able to globally install packages because you need admin privileges.
#             
#

# %% [markdown] slideshow={"slide_type": "slide"}
# - Using virtual environments
#     - Your packages don't interfere with system-relevant packages.
#     - Your global site-packages directory is not polluted by packages which you might only need for one project.
#     - You can simply activate one environment to use specific package versions without reinstalling packages.
#     - Provided you use a virtual environment for each separate project
#         - You can make your project self-contained and reproducible by capturing all package in a environment file.
#         - You can easily share your project and collaborate with others because they can easily install the required packages and reproduce your setup.
# - As a result, you should use virtual environments for all your Python projects (**no exception!**).

# %% [markdown] slideshow={"slide_type": "slide"}
# ## What is a virtual environment?
# - In a nutshell, a virtual environment is just
#     - An isolated installation of Python and its installed third-party modules.
#     - A bunch of activation scripts that modify your PATH variable when you activate the environment.
# - Let's have a detailed look at this in the following.

# %% [markdown] slideshow={"slide_type": "slide"}
# ###  It stores a Python interpreter and packages into a separate folder

# %% [markdown] slideshow={"slide_type": "-"}
# - A virtual environment is a separate folder that, among other things, contains an isolated site-packages folder and either
#     - A copy of or symlink to the global Python executable.
#     - A separate Python executable with a possibly different version than the global Python executable.
# - This seperate folder provides an isolated Python environment that reproduces the folder structure of the global Python installation.
# - The exact location and structure of this separate folder depends on the tool that you use to create a virtual environment.
# - In the following we consider **conda** which has been used to set up the virtual environment `dsc` of this project by executing ```conda env create -f environment.yml```  from the root directory of this project. 
# - The base environment of conda is given by the location where conda is installed and also contains all other environments.
# - The `dsc` environment of conda is located in the env folder of this base environment and located at

# %% slideshow={"slide_type": "-"}
conda_env

# %% [markdown] slideshow={"slide_type": "slide"}
# - The structure of the virtual conda environment is complex...

# %% slideshow={"slide_type": "-"}
!tree -L 1 {conda_env}

# %% [markdown] slideshow={"slide_type": "slide"}
# - (Non-built-in) packages are installed in a subdirectory of the lib folder

# %% slideshow={"slide_type": "-"}
site_packages

# %% slideshow={"slide_type": "-"}
!tree -L 1 {site_packages}

# %% [markdown] slideshow={"slide_type": "subslide"}
# - For instance, the first level of the pandas package looks as follows

# %% slideshow={"slide_type": "-"}
!tree -L 1 {pandas}

# %% [markdown] slideshow={"slide_type": "slide"}
# - The Python interpreter of the conda environment is located at

# %% slideshow={"slide_type": "-"}
python 

# %% [markdown] slideshow={"slide_type": "-"}
# - This Python interpreter can be executed by specifying the full path to the executable

# %% slideshow={"slide_type": "-"}
!{python} -c "import sys; print(f'Hello from the Python interpreter located at {sys.executable}')"

# %% [markdown] slideshow={"slide_type": "slide"}
# ### It modifies its Python interpreter, in particular its sys.path

# %% [markdown] slideshow={"slide_type": "-"}
# - We can also see that the Python interpreter of the `dsc` environment is aware of the location of the corresponding site-packages directory

# %% slideshow={"slide_type": "-"}
!{python} -c "import site; print(site.getsitepackages())"

# %% [markdown] slideshow={"slide_type": "fragment"}
# - If we import a module during a Python session which has been started in an activated environment the corresponding module of the environment is loaded

# %% slideshow={"slide_type": "-"}
!{python} -c "import pandas as pd; print(pd)"  # you can see all imported modules using sys.modules

# %% [markdown] slideshow={"slide_type": "slide"}
# - How does the Python interpreter know from which location a module should be imported?
# - When a Python interpreter imports a (non-built-in) module, the interpreter looks through the list of directories given in sys.path.
# - As already demonstrated, the Python interpreter of the environment knows the location of its site-packages directory and adjusts sys.path accordingly when the interpeter is started.
# - The following program returns sys.path and thus all directories from where modules can be imported (The empty string refers to the current working directory).

# %% slideshow={"slide_type": "-"}
!{python} -c "import sys; from pprint import pp; pp(sys.path)"  # lib/python3.10' built-in packages

# %% [markdown] slideshow={"slide_type": "slide"}
# ### It provides activation scripts to make them user-friendly
# - If virtual environments would only be a separate folder with a modified Python interpreter then...
#     - Running the ```python``` command would always start the global Python interpreter (if installed).
#     - We would always have to specify the absolute path to the executable to execute the Python program of the environment.
# -Therefore, virtual environments also provide **activation scripts** to 
# run the corresponding executables as simple commands without having to specify the absolute paths.

# %% [markdown] slideshow={"slide_type": "slide"}
# #### Activating an environment modifies the PATH variable

# %% [markdown] slideshow={"slide_type": "-"}
# - If you activate the `dsc` environment and execute the command ```python3``` in the terminal, the corresponding Python program of this environment is executed.
# - How can this happen?
# - More general, what does happen when you execute commands like ```ls``` or ```python3``` in the terminal?
# - Obviously, these commands are located somewhere, but where are they?

# %% [markdown] slideshow={"slide_type": "slide"}
# - The unix command ```which <command>``` returns the full path of the executable of a command.
# - For instance, the following command shows that the exectuable for the command ```ls``` is located in the directory bin which is a subdirectory of the root directory /

# %% slideshow={"slide_type": "-"}
!which ls

# %% [markdown] slideshow={"slide_type": "-"}
# - Thus, running the command ```ls``` actually executes ```/bin/ls``` to list files and directories.
# - How does your terminal know that ```/bin/ls``` should be executed when you execute the command ```ls```?
# - Whenever you don't specify the full path to the executable, the terminal investigates the PATH variable to locate the underyling executable of the command.

# %% [markdown] slideshow={"slide_type": "slide"}
# - On many operations systems, the PATH variable is the search path where executable programs are located.
# - The PATH variable is an environment variable and consists of a colon-delimited list of directories.
# - In general, each executing process or user session has its own PATH variable.
# - When you run a command, the shell investigates each of these directories, from top to bottom, until it finds a directory where the executable is located.
# - You can set ```PATH=""``` in a unix-like shell session. Commands which are not built-in can then only be called by specifying the full path to the executable.

# %% [markdown] slideshow={"slide_type": "slide"}
# - The first entries of the PATH variable of the activated environment are as follows

# %% slideshow={"slide_type": "-"}
path[0:9]

# %% [markdown] slideshow={"slide_type": "-"}
# - Note that the first entry of the PATH variable
#     - Is a directory of the `dsc` environment.
#     - Contains the Python executable.
# - This first entry of the PATH variable has been **added by conda during the activation of the `dsc` environment**.
# - This first entry changes accordingly if you activate another conda environment.

# %% [markdown] slideshow={"slide_type": "slide"}
# - Thus, when the command ```python3``` is executed in the activated `dsc` environment, your terminal investigates the directory

# %% slideshow={"slide_type": "-"}
path[0]

# %% [markdown] slideshow={"slide_type": "-"}
# - and finds the Python executable located at

# %% slideshow={"slide_type": "-"}
!which python3

# %% [markdown] slideshow={"slide_type": "-"}
# - which is then executed. 

# %% [markdown] slideshow={"slide_type": "slide"}
# #### Activating an environment modifies the command prompt
# - If you activate an environment the name of the environment is put in parentheses at the beginning of your prompt, e.g., `(dsc)`.
# - This helps you to see which environment is activated.

# %% [markdown] slideshow={"slide_type": "slide"}
# #### Review question
# - What happens if you run ```pip install pandas``` from an activated environment?

# %% [markdown] slideshow={"slide_type": "slide"}
# **Answer:** 
# - [By default](https://conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html#add-pip-as-python-dependency-add-pip-as-python-dependency), pip is always installed in a conda environment. 
# - Thus, pandas is installed in the activated environment.
#     

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Summary
# - A **virtual environment**
#     - Is **a folder** structure that mimics the structue of a global Python installation.
#     - Contains procedures that modify its Python interpreter so that the **corresponding Python modules of the environment are imported**.
# - For convenience, **its activation script modifies the PATH variable** so that applications look for the executables of the environment when a command is run.
# - With this change you don't need to provide the absolute paths of executables but can only type ```pip``` or ```python``` to run the respective programs of the virtual environment (provided the programs have been installed into the environment).
# - If you don't use virtual environments you can run into several problems.
# - Thus, **you should always use virtual environments** for all your Python projects (**no exception!**).
#

# %% [markdown] slideshow={"slide_type": "slide"}
# **Note!**
#
# - **The functionality of your Python project is determined by**
#     1. The activated environment.
#     1. The working directory.
#     1. The currently checked-out Git branch (plus possible uncommitted changes).
# <br><br>
# - Always check that you use the correct environment, working directory and Git branch (!)

# %% [markdown] slideshow={"slide_type": "slide"}
# # Package management

# %% [markdown] slideshow={"slide_type": "-"}
# - In this course we will use **conda** and **pip** for package management to install and manage packages that aren’t part of the Python standard library.
# - [pip](https://realpython.com/what-is-pip/) stands for Pip Install Packages and is the standard package manager for Python.
# - pip connects to **PyPi** (the [Python Package Index](https://en.wikipedia.org/wiki/Python_Package_Index)) which is the official third-party software repository for Python.
# - Assuming you have activate the correct environment (and pip installed!), you can install a package from PyPi into this environment via
# ```pip install [<package>]```
# - It is also possible to install a package directly from other sources, e.g., GitHub, e.g., ```pip install git+https://github.com/googleapis/python-bigquery-pandas.git```
# - However, in the following we will focus on conda for installing packages which we will dicuss next.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Conda

# %% [markdown] slideshow={"slide_type": "-"}
# ## Resources
# - [Offical documentation](https://conda.io/projects/conda/en/latest/index.html)
#     - [User guide](https://conda.io/projects/conda/en/latest/user-guide)
#     - [How to manage environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
#     - [Command reference](https://docs.conda.io/projects/conda/en/latest/commands.html): Note that this site does not mention ```conda env```. Use ```conda env -h``` for infos or [How to manage environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
#     - [Anaconda tasks](https://docs.anaconda.com/anaconda/user-guide/tasks/)
#     - [Cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)
#     - [Comparison of pip, venv and conda commands](https://docs.conda.io/projects/conda/en/latest/commands.html#conda-vs-pip-vs-virtualenv-commands)
# - What is conda?
#     - [What is the difference between pip and conda](https://stackoverflow.com/questions/20994716/what-is-the-difference-between-pip-and-conda)
#     - [Conda myths and misconceptions](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions)
#     - [The definitive guide to Python virtual environments with conda](https://whiteboxml.com/blog/the-definitive-guide-to-python-virtual-environments-with-conda)
# - How to use conda
#     - [A guide to conda environments](https://towardsdatascience.com/a-guide-to-conda-environments-bc6180fc533)
# - [How conda resolves dependencies](https://www.anaconda.com/blog/understanding-and-improving-condas-performance), see also [here](https://www.palantir.com/docs/foundry/transforms-python/environment-creation-overview/#performance)
# - [Using conda for commerical purposes](https://florianwilhelm.info/2021/09/Handling_Anaconda_without_getting_constricted/)
#
#
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## What is conda?

# %% [markdown] slideshow={"slide_type": "-"}
# - **Conda** is an open-source package and environment management system that
#     - Runs on  Windows, macOS, and Linux.
#     - Is language agnostic (Python, R, Ruby, Lua, Scala, Java, JavaScript...).
#     - Is written in Python.
#     - Was [initiated](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/#Myth-#4:-Creating-conda-in-the-first-place-was-irresponsible-&-divisive) by the NumPy community.
#     - Is owned and maintained by the conda open source community.
# - **Anaconda**
#     - Anaconda, previoulsy Continuum Analytics, is a commercial software organization providing the Anaconda **distribution** which includes conda, Python, an IDE, and 250+ open-source scientific packages including most common data science libraries.
#     - Includes the Anaconda Navigator, a GUI tool that helps you manage conda environments and packages without a command line interface &#128078;
#     - Requires about 3GB disk space.
# - **[Miniconda](https://github.com/conda/conda) (recommended)**
#     - Miniconda is a small, bootstrap version of Anaconda that includes only conda and a small number of packages.
#     - Requires about 400MB disk space.
#     
#     
# <!-- Anaconda, Inc. is one of a large team of maintainers in the conda package open source community. Anaconda hosts conda-forge-->

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Using conda for commercial purposes
# - By default, conda is free for individual and educational purposes.
# - Note that, **by default, conda cannot be used for commercial purposes** if the company has more than 200 employees (!)
#     - See [here](https://www.anaconda.com/blog/anaconda-commercial-edition-faq) and [here](https://conda-forge.org/blog/posts/2020-11-20-anaconda-tos/).
# - The reason is that the **defaults [channel](https://conda.io/projects/conda/en/latest/user-guide/concepts/channels.html)** of conda uses the Anaconda repository (i.e. anaconda.com) to download packages. This repository is maintained by Anaconda and requires a license.
# - However, you **can use conda for commerical purposes if you remove this channel from your conda configuration and use the conda-forge repository (i.e. anaconda.org)**, see also [here](https://florianwilhelm.info/2021/09/Handling_Anaconda_without_getting_constricted/).
# - Or, directly use [miniforge](https://github.com/conda-forge/miniforge) or [mambaforge](https://github.com/conda-forge/miniforge#mambaforge) which use the conda-forge repo by default.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Why conda?

# %% [markdown] slideshow={"slide_type": "-"}
# - There are a [lot of package and/or virtual environment managers in the wild](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe)
#     - easy_install
#     - pip
#     - pyenv
#     - venv
#     - virtualenv
#     - pyenv-virtualenv
#     - virtualenvwrapper
#     - pyenv-virtualenvwrapper 
#     - pipenv 
#     - conda
#     - mamba
#     - pdm
#     - poetry
#     - ...

# %% [markdown] slideshow={"slide_type": "slide"}
# **Why should one use conda?**
#
# - Conda provides a **unified approach of package and environment management**.
#     - Manages Python versions.
#     - Manages Python packages.
#     - Manages virtual environments.
# - You may need to use three tools, e.g., pip, virtualenv and pyenv to reproduce this subset of condas functionality
# - Conda **manages also non-Python libraries**. 
#     - For instance, you can also install system libraries like glibc or the correct CUDA 
# in your environment for neural network libraries that need a GPU/CUDA.
#     - Or other usefull programs like make, postgresql, aws-cli, ...
#     - If you cannot install a program due to insufficient rights, you can often used conda to install the program into an environment (!)<!-- Using https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html one cannot install the aws-cli on Windows. With mamba it works-->
# - Conda environment directories are **self-contained** and can be moved to a different location. They are not dependent on any global python libraries, nor conda itself. 
# - Supported by a lot of third-party packages.
# - In comparison with pip (the last two points will also be discussed on the next slides):
#     - Installing packages with conda can be very slow -> mamba is much faster than conda but still slower than pip (?)
#     - Installation of (data) science packages was much more straight forward with conda than with pip (still is?)
#     - Installation of packages resulted in less dependency conflicts (still true since pip 20.3?)
#
#
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Comparison with Pip
# - Pip requires a global Python installation, conda not.
# - Conda only **installs binary packages**
#     - Originally, pip could only install from source and did not support binary packages.
#         - This is not a problem if the package is only written in Python.
#         - However, if the package includes C or FORTRAN code (which is often the case for (data) science packages) or other third-party dependencies that needs to be compiled, you need to have the tools to compile it [which can be quite painful](https://stackoverflow.com/questions/28413824/installing-numpy-on-windows) &#128557;
#         - This is especially true for Windows but can even be true for Unix systems.
#     -  Conda leaves the potentially difficult compilation step to the package maintainer so that the installation with pre-compiled binaries is straight forward.
#     - Nowadays, pip can install packages via the binary [wheel](https://realpython.com/python-wheels/) format, however [conda still handles non-Python dependencies better](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/#Myth-#6:-Now-that-pip-uses-wheels,-conda-is-no-longer-necessary).

# %% [markdown] code_folding=[0] slideshow={"slide_type": "slide"}
# **Comparison with Pip Cont'd**
#
# - [Conda has a true dependency resolver](https://www.anaconda.com/blog/understanding-conda-and-pip), something pip had been lacking for a long time or is [still lacking]((https://github.com/pypa/pip/issues/988)) (?)
#     - In the past, installing packages with pip could result in a broken environment (current status unknown to me since pip 20.3 introduced a new dependency solver).
#     - As long as package metadata about dependencies is correct, conda produces working environments with the downside of [taking more time](https://docs.conda.io/projects/conda/en/latest/dev-guide/deep-dives/solvers.html).
# - Not all, but almost all PyPi packages that you will need are available on conda channels.

# %% [markdown] slideshow={"slide_type": "-"}
# <table>
# <caption>This table is inspired by https://www.anaconda.com/blog/understanding-conda-and-pip </caption>
#         
# |                    |         conda         | pip                       |   |
# |:------------------:|:---------------------:|---------------------------|---|
# |      installs      |        binaries       |      from source or wheels      |   |
# |    package types   |          any          | Python                    |   |
# | create environment |          yes          | no                        |   |
# | dependency checks  | full                  | ? (was recursive in 2018) |   |
# | package sources    | Anaconda, conda-forge,... | PyPi, Github...           |   |
#
# </table>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### So...?
# - If you are using complex Python environments (which is common in data science) I (still) recommend conda.
# - Otherwise you could just use pip, pyenv & venv/virtualenv or still just stick with conda.
# - Be aware, however, that many Python developers who don't do (data) science seem to reject conda, probably out of ignorance
# &#128529; See also the brilliant article [conda myths and misconceptions](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions).

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Conda's two command types
# - There are two types of conda commands
#     - Commands that start with ```conda env```, such as ```conda env list``` or ```conda env create```
#         - Information about these commands is (only) scattered in the section on [managing environments with conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#).
#     - All other commands.
#         - Information about these commands is available at [conda's command reference](https://docs.conda.io/projects/conda/en/latest/commands.html)
# - This can be a little bit confusing because, e.g.,
#     - ```conda env list``` and ```conda info --envs``` yield the same result.
#     - ```conda env remove --name myenv``` and ```conda remove --name myenv --all``` yield the same result (?).
#     - ```conda env export``` and ```conda list``` yield similar but not identical results. 
#     - One can use ```conda env create -f environment.yml``` or ```conda create -n env -f environment.yml``` to create environments in a [certain way](https://stackoverflow.com/questions/65668913/can-i-create-a-conda-environment-from-multiple-yaml-files).
# - However, apart from manually creating an environment, most basic tasks can be done with commands that start with ```conda env```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Creating an environment by hand
# <!--
# - You can create an empty environment called "env" by running 
# ```conda create -n env```
#      - There is nothing installed in this environment
# -->
# - Conda comes with a **base environment** which can be activated by executing the conda activation script or, provided the activation script is on the PATH variable, by running ```conda activate```
# - While you can install some packages in the base environment, you should **use a separate environment for each separate project** (both with the same name).
# - You can **create an environment** called ```env``` which contains packageA with version number 2.1. and the most current compatible version of packageB by running  
# ```conda create -n env packageA=2.1 packageB```
# - This will also install the most recent compatible Python version, use  
# ```conda create -n env python=3.X packageA packageB```
# to install a specific Python version.
# - Note that, by default, conda install packages only from the defaults channel (anaconda.com).
#     - Thus, if a package is not available on the defaults channel, it cannot be installed.
#     - Moreover, the use of the defaults channel requires a license for commercial purposes.
#     - **To install packages from other [channels](https://docs.conda.io/projects/conda/en/latest/glossary.html#channels), in particular [conda-forge](https://conda-forge.org/docs/user/introduction.html)**, read the documentation of the command ```conda create/install``` or modify the .condarc file.
# - It is also possible to install the conda environment into a [different location](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#specifying-a-location-for-an-environment), e.g., as a subdirectory of your project.
#  

# %% [markdown] slideshow={"slide_type": "slide"}
# ## (De)activating an environment
# - You can **activate** the environment ```env``` by running  ```conda activate env``` (assuming the base environment had been activated before).
# - Running ```conda deactivate``` **deactivates** the current environment.
# - To see a list of the conda environments use ```conda env list```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Installing more packages
# - To add packages to the environment ```env``` run ```conda install -n env packageC packageD ...```
# - You should try to install all packages at once and not individually to save time and reduce the possibility of dependency conflicts.
# - That is, do not use  
# ```
# conda create -n env packageA &&
# conda install -n env packageB &&
# conda install -n env packageC
# ```
# but instead
# ```
# conda install -n env packageA packageB packageC
# ```
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Creating an environment file
# - To make your environment reproducible and share it with others you can create **a file that lists the dependencies** of your project
#     - **Abstract** dependencies list libraries which are directly imported. They (often) do not pin the version of libraries.
#     - **Concrete** dependencies state all dependencies with exact version numbers.
#         - Ensures that the project runs on a different computer with the same operating system.
#         - The environment cannot be created on a different operating system using concrete dependencies.
#     - If some dependencies are only required for the development of a project but not for running the code, you can also put these dependencies in a separate file. To consider multiple files when building the environment, click [here](#multiple_envs).
# - In conda, dependencies should be put into an **environment.yml** file.
#     - Concrete dependencies (including pip) can be created via ```conda env export > environment.lock.yml``` 
#     - Note that ```conda env export --from-history > environment.yml``` can only be used to obtain abstract dependencies if no package has been installed with pip.
#     - I recommend to create abstract dependencies manually. 
#     - Each project should have an environment file with abstract dependencies.

# %% [markdown] slideshow={"slide_type": "slide"}
# - An (abstract) environment.yml file looks as follows
# ```
# name: env
# channels:
#   - conda-forge
#   - nodefaults
# dependencies:
#   - numpy
#   - pandas
#   - pip:
#     - dateutil
# ```
#     - The name in the first line is the name of the environment.
#     - The channels specify the channels from which packages are downloaded.
#     - The dependencies list the packages to be installed (via conda).
#     - If a dependency is ```pip:``` the next indented packages are installed via pip.
# - The environment.yml should be located in the project root.
# - Its file extension must be .yml (not .txt or something else).

# %% [markdown] slideshow={"slide_type": "slide"}
# - The content of the environment.yml of this project is

# %% slideshow={"slide_type": "-"}
!cat ../../environment.yml    

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Creating an environment from an environment file
# - To create a conda environment from an environment.yml file simply run  
# ```conda env create -f environment.yml```  
# from the directory where the .yml file is located.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Using Pip with Conda
# - Packages can also be installed with pip into conda environments, provided you have installed pip in the environment with ```conda install -n env pip```
# - You need to use pip if the package is unavailable through the conda channels (this should be an exception) or you want to install your own package in editable mode (which we will discuss later).
# - However, to maintain the environment integrity, you should **[only use pip after you have installed all packages with conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#using-pip-in-an-environment)**.
# - Otherwise, do not mix conda and pip.
# - If you need to install a conda package after you have installed a package with pip it's best to delete the environment and create it again by installing all conda packages first.
# - Alternatively, you may try an [experimental feature](https://conda.io/projects/conda/en/latest/user-guide/configuration/pip-interoperability.html) that improves the interoperability between conda and pip.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Mamba
# - See [here](https://www.anaconda.com/blog/understanding-and-improving-condas-performance) how to generally improve condas performance.
# - Still, conda might be too slow for you so you can use the drop-in replacement mamba.
# - From the [website](https://github.com/mamba-org/mamba)
#     - Mamba is a reimplementation of the conda package manager in C++.
#     - Parallel downloading of repository data and package files using multi-threading.
#     - Libsolv for much faster dependency solving, a state of the art library used in the RPM package manager of Red Hat, Fedora and OpenSUSE.
#     - Core parts of mamba are implemented in C++ for maximum efficiency.
#     - At the same time, mamba utilizes the same command line parser, package installation and deinstallation code and transaction verification routines as conda to stay as compatible as possible.
# - You can also [switch conda's solver to the same solver mamba uses](https://github.com/conda-incubator/conda-libmamba-solver). 
# - **mambaforge** uses only the conda-forge channel by default, so you can always use it without a license, and can be downloaded [here](https://github.com/conda-forge/miniforge#mambaforge). 
# - There is also **micromamba**: a pure C++-based CLI, self-contained in a single-file executable which does not depend on conda.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Supplementary material
# ### How to use the base environment
# - Use the base environment to install common command-line utilities, e.g., [PyScaffold](https://pyscaffold.org/en/stable/), [tox](https://tox.wiki/en/latest/), or [conda-merge](https://github.com/amitbeka/conda-merge), that you use for all your projects.
# - The base environment should not be a dumping ground for packages.
# - Build a separate environment for adhoc analyses in which you install common Python packages, e.g., put pandas and numpy in an environment called datasciene.
# - If you install everything in the base environment
#     - Installing new packages takes a lot of time because more dependencies have to be checked.
#     - You might not be able to install a new package due to incompatibility.
#     - Since there is no usable environment file collaboration gets complicated.
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Run an exectuable in a specific conda environment
# - Use ```conda run``` to run executables in activated environments, e.g.,  
# ```conda run -n base python -c 'import sys; print(f"The python executable of this environment is {sys.executable}")'```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Stacking environments:
# - By default, conda activate deactivates the current environment before it activates the new environment, and reactivates it when the new environment is deactivated. 
# - Sometimes it is useful to access command-line utilities from the previous environment. This is especially true if you use the base environment to install command-line programs.
# - Use ```conda activate --stack myenv``` to append the PATH entries of the previous environment to the new PATH variable.
# - PATH entries from the previous environment have a lower priority, i.e., only the Python executable of the activated environment is considered.
# - Use ```conda config --set auto_stack 1``` to keep the PATH entries of the base environment.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Using multiple conda environment files to build one environment
# <a id="multiple_envs"></a>
# - It is useful to distribute required packages to different environment files. 
#     - For instance, the main environment file contains all packages that are required to run the code of a project.
#     - The dev environment file contains all additional packages that are useful to develop the project (e.g., running tests).
# - [At the moment](https://github.com/conda/conda/issues/9294#issuecomment-781347771) there is [no way](https://stackoverflow.com/a/74245058) to **directly** create an environment based on multiple .yml environment files that also takes into account that some packages require an installion with pip.
#     - ```conda env create``` is designed to take only one single .yml file.
#     - ```conda create``` accepts multiple [.txt requirement files that pip uses](https://pip.pypa.io/en/stable/reference/requirements-file-format/).
#         - For instance, ```conda create -n env --file=a.txt --file=b.txt```, where a.txt can be automatically created using ```conda list --explicit```.
#         - However, since these are not yml.files they do not specify which packages must be installed by pip (all packages are assumed to be installed with conda) 

# %% [markdown] slideshow={"slide_type": "slide"}
# **Using multiple conda environment files to build one environment: Cont'd**
# - However, you can use multiple .yml files to  **sequentially** create an environment by running ```conda env create -f env1.myl``` and then use ```conda env update -f env2.yml``` to update the environment with a new .yml file. 
#     - This process is not efficient, because conda has to resolve the dependencies with each update.
#     - Moreover, as pointed out [here](https://github.com/amitbeka/conda-merge) this may reinstall package from the previous environment with a different version.
# - Alternatively, you can use [conda-merge](https://github.com/amitbeka/conda-merge) to **merge multiple .yml environment files into one .yml enviroment file** which can then be used with ```conda env create``` as follows
# ```
# conda merge env1.yml env2.yml > env.yml
# conda env create -f env.yml
# ```
#     - By defaulf, the name of the last environment is the environment name of the resulting .yml file
#     - To change the name you can use ```conda merge test1.yml test2.yml | sed 's/\(name:\).*/\1 new_name/'```, where new_name is the evnironment name of the environment file

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Updating an environment with a .yml file
# - See [here](https://stackoverflow.com/a/54825300) and [here](https://stackoverflow.com/a/54165945).

# %% [markdown] slideshow={"slide_type": "slide"}
# # Summary
# - Conda ist the best choice for package and environment management if you are doing data science.
# - Without further configuration, conda requires a license for commercial purposes.
# - Use [mambaforge](https://github.com/conda-forge/miniforge#mambaforge) to speed up conda and not require a license.
# - Try to use a separate environment for each project.
# - If possible, install all packages at once into the environment. 
# - Do not install packages with conda into an environment if you have already used pip to install packages.
# - Manually create an abstract .yml conda environment file for each environment. Concrete dependencies are only required if you put something into production.
# - To create an environment on the basis of multiple .yml environment files use conda-merge.
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Commands
# - Activate and deactivate an environment: ```conda activate env``` and ```conda deactivate env```
# - Creating an environment by hand: ```conda create -n env python=3.X packageA packageB```
# - Creating an environment from an environment file: ```conda env create -f environment.yml``` 
# - Installing packages: ```conda create -n env packageA packageB```
# - Creating a .yml environment file with concrete dependencies (including pip): ```conda env export```
# - Creating a .yml environment file with abstract dependencies (excluding pip): ```conda env export --from-history```
# - Use ```conda run``` to run executables in activated environments
# - Use ```conda activate --stack myenv``` to stack environments
# - Use ```conda merge test1.yml test2.yml | sed 's/\(name:\).*/\1 new_name/'``` to merge .yml environment files and name the environment to new_name
