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

# %% active="ipynb" hide_input=false slideshow={"slide_type": "notes"} tags=["active-ipynb"]
# from dsc.notebook import embed_website

# %% [markdown] slideshow={"slide_type": "slide"}
# <div align="center" style="font-size:70px;">
# WELCOME TO THE DATA SCIENCE CHALLENGE!
# <div/>
#     
# <div align="left" style="font-size:16px;">
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# # Agenda
# - Introduction
#     - About me
#     - Information about this course
#         - Motivation
#         - Structure & organization
#         - Examination requirements
#         - Prerequisites and tools
# - Data and project presentation
#     - Data description
#     - How to access the data
#     - Project description
# - Tutorial

# %% [markdown] slideshow={"slide_type": "slide"}
# # About me

# %% [markdown] cell_style="split" hide_input=false slideshow={"slide_type": "-"}
# <div align="center">
# <img src="./figures/0_me.png" alt="Dr. Fabian Spanhel" width="500"/>
# </div>
#
# <div align="left" style="font-size:16px;">
# <div/>

# %% [markdown] cell_style="split" slideshow={"slide_type": "-"}
# <br>
#
# <div align="center" style="font-size:40px;">
# Dr. Fabian Spanhel
# <div/>
#     
# <div align="left" style="font-size:32px;">
# <div/>
# <br>
#
# - Studied economics with a focus on econometrics & statistics
# - PhD in statistics
# - Since November 2016 working as a Data Scientist at ProSiebenSat.1
# - Aquarius, [INTJ](https://www.16personalities.com/), likes doing sports
# - Social media:
#     - https://www.linkedin.com/in/fspanhel/
#     - https://vm.tiktok.com/ZMFJFtD7y/

# %% [markdown] slideshow={"slide_type": "slide"}
# # Motivation: Is data scientist still the sexiest job of the 21st century?
# The article titled ["**Data Scientist: The Sexiest Job of the 21st Century**"](https://hbr.org/2012/10/data-scientist-the-sexiest-job-of-the-21st-century) published in 2012 is a very popular article that contributed to popularize data science. 

# %% [markdown] slideshow={"slide_type": "fragment"}
# At this time:
#
# - The role data scientist "was relatively new, but as more companies attempted to make sense of **big data**, 
# they realized they needed people who could **combine programming, analytics, and experimentation skills**."
# - The were assumed be **unicorns** and do all required tasks — from conceptualizing the use case, to 
# interfacing with business and technology stakeholders, to developing the algorithm and deploying it into production.
# -"Because there wasn’t yet a well-defined career path for people who could program with and
# analyze such data, **data scientists had diverse educational backgrounds**."
# - "Most had **PhDs** in some scientific field, were exceptional at math, and knew how to code. Given the **absence of tools and processes**."
# - To "perform their roles, they were also good at **experimentation and invention**."
#

# %% [markdown] slideshow={"slide_type": "slide"}
# The article titled ["**Is Data Scientist Still the Sexiest Job of the 21st Century?**"](https://hbr.org/2022/07/is-data-scientist-still-the-sexiest-job-of-the-21st-century) is the follow up of the previous mentioned article. 
#
# - A decade later, **AI is increasingly popular** in business and the job is more in demand than ever.
# <!-- Nevertheless, there are issues: -->
# <!--   - Much time of data scientist is spent cleaning and wrangling data. -->
# <!--    - Many organizations don’t have data-driven cultures and don’t take advantage of the insights provided by data scientists. -->
# <!--    - Many algorithms are never deployed. -->
# - Now there are **hundreds of degree programs** in data science or the related fields of analytics and AI.
# - **No data science unicorns anymore** but there are related jobs to handle many of those tasks, e.g., **machine learning engineers**, **data engineers**, **advanced analytics**, and **data oriented product managers**. 
# -  "We expect to see **continued differentiation of responsibilities** and
#     roles that all once fell under the data scientist category".
# - **Automated machine learning** might dim the demand of data scientists who primarily do model fitting for prediction.
# - **MLOps** (Machine learning operations) which establishes best practices and tools to facilitate development and operationalization of AI becomes more important.
# - "Most importantly, data scientists must contribute towards appropriate collection
# of data, responsible analysis, and **translating business issues and requirements into fully-deployed models**, and successful business outcomes".

# %% [markdown] slideshow={"slide_type": "slide"}
# <img src="./figures/0_hierarchy.png" alt="The Data Science Hierarchy of Needs" width="1200"/>
# <br>
#
# [Source](https://www.reddit.com/r/datascience/comments/wi2gil/the_data_science_hierarchy_of_needs)

# %% [markdown] slideshow={"slide_type": "slide"}
# # Course objectives
# - Learn something for your professional life
# - Learn some the basics of **writing good code which is suitable for production** and usable by ml engineers 
# - Learn tools and methods to **conduct reproducible data science experiments and to collaborate in a team**
# - Learn how to model data where the **time dimension** is important
# - Consolidate what you have learned through a **collaborative practice project**
#

# %% [markdown] slideshow={"slide_type": "slide"}
# # Structure of this course
#
#

# %% [markdown] slideshow={"slide_type": "-"}
# ## First part
# - The **first part** of this course, **which lasts until November 24**, consists of **prepared lectures**
# with notes and tasks that you can tackle in the tutorials.
# - We will cover 
#   - Version control
#   - Setting up a Python project
#   - Good coding habits
#   - Project management and collaborative coding
#   - ...
#   - Model tracking with Mlflow and deployment
# - The first part is designed to prepare you to successfully master your following **project challenges**.
# - It is expected that you **have a detailed look at the topics that we discuss in the first part before the second part starts**. Otherwise, you might run out of time in the second part!
# - Moreover, I recommend that every student uses the first part to **familiarize themselves with the data** for the projects so that they can make an informed decision about their project preferences in the second part.
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Second part
# - In the **second part**, **starting from November 25**, there will be no prepared lectures or task and you will be **working on your project challenge**  during the lecture and tutorial.
# - You can **choose your project from 3 main [projects]**.
# - Each project should be worked on by about **4 people**. 
# - Each student has to submit his/her preference for the projects in November by no later than **Wednesday, November 23, 2022**.
# - For this purpose, write an eMail to spanhel@hm.edu with the subject 'dsc project preference' which includes your full name and an enumerated list containing the numbers of **all** [projects] that is **sorted by your preference**.
# - Each student will then be assigned to a project by considering his/her preferences by no later than **Friday, November 25, 2022**. 
#   - If there is more than one group for a project, the assignment of students to a group will be random.
# [projects]: 1_data_and_projects.ipynb#Projects

# %% [markdown] slideshow={"slide_type": "slide"}
# - I will support you during the second part by **answering questions and providing suggestions** during the lecture and tutorial.
# - Moreover, I will have a look at your code and **approve merge requests** for the main
# branch of your project.
# - I **highly recommend** that we discuss your work on the following topics on the following dates
#     - December 2: Setup, data import and basic feature building.
#     - December 9: Setting up cross-validation for a benchmark model and estimating the prediction error.
#     - December 16: Optimization of feature creation, model fitting, and cross-validation.
#     - December 23: Code modularization and creation of scripts.
#     - January 13: Final discussion on open points.
# - I also recommend that **you have already worked on the topics** that we discuss on a date so that I can provide feedback and suggest further steps. This way you can get the most out of it.
# - Therefore, you should start your project work from November 25, 2022. 
# - I will be able to talk to each group for at least (90 * 2) / [number of groups] minutes during the lecture/tutorial. If a group requires less time, the available time for other groups will increase correspondingly. 

# %% [markdown] slideshow={"slide_type": "slide"}
# # Examination requirements: ModA(0,6) + Präs(0,4)
#
# In order to be graded, you have to 
# 1. **Submit your project code** 
# 2. **Give a presentation** about your project.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Code submission
# - Before you project starts, you will be provided with a remote Git repo hosted on GitLab with the two branchens `main` and `submission`.
# - The code of your collaborative project must be submitted <span style="color:red">**before (!)**</span> **Sunday, January 15th, 2023**.
# - **Submitted means** that at 2023-01-15 00:00:00 an attempt will be made to merge all active merge requests whose target branch is `submission`.
# - Your project will then be evaluated on the state of the `submission` branch after this attempt has been made.
# - Note that merge requests that cannot be merged will not be considered and you as a team are responsible for ensuring that I can run your code.
# - **The code submission should contain the following four components**:  
#   1. **Notebooks** with exploratory analyses or findings.
#   2. A **Python package** with functions and classes which are used in the notebooks and the scripts
#   3. A **script for training a model** that can be called from the command line which    
#       1. Loads a provided dataset
#       2. Engineers the features
#       3. Trains a model
#       4. Stores the model, e.g., with Mlflow
#   4. A **script for predicting data** that can be called from the command line which 
#       1. Loads a model, e.g., by taking a registered model in Mlflow.
#       2. Predicts data on the basis of the provided dataset
#       3. Writes the predicted data to a file   

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Code Grading
# - **The grading of the code submission focusses on the following points**:
#   - How was your **organization** as a team? 
#     - Did you communicate well and approach the challenge in a structured way?
#     - How did you use GitLab and Git to organizate your tasks and document your working steps? For instance, did you create good issues and merge requests?
#   - To what extent did you **address the challenges of the project**? 
#   - How is the **overall code structure**?
#     - How long do I need to understand what you have done?
#     - Is it pleasant or rather akward to work with your code?
#   - Did you apply **best practices** that we discussed in this course, e.g.,
#     - Usage of reproducible virtual environments.
#     - Version control (Source code and data).
#     - Setting up a Python project (Folder structure, documentation, prototying in notebooks, structuring library code into modules and packages).
#     - Readable code (PEP8 compliant, modularized and understandable, no [spaghetti code](https://en.wikipedia.org/wiki/Spaghetti_code)).
#     - The best practices that I suggest are suggestions. You are free to apply other/additional best practices. 
#   - Is the **code functional**?
#     - Can the model be trained on new data?
#     - Can the model use new data for predictions?
#     - Are there some rather obvious problems with your code? For instance, does it break when I want to change an input that should be modifiable?
#   - Is the training of your model and the estimation of its prediction performance **methodologically sound**? 
#     - How well does your cross validation mimic the use case? 
#     - Did you consider relevant features?
#     - It is not important that your model generates top notch predictions. Keep it simple.
# - The grading for a student takes its **individual performance and the team performance** into account.
#   - To measure the individual performance, I consider his/her participation in the project work during the lecture and tutorial, his/her code commits/PRs and the quality of his/her written GitLab issues.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Presentation
# - The presentations will take place on **Friday, January 20th, 2023,** in room R2.012 from **15:00-19:00**.
# - Each group presents their work (task, approach, repo overview, problems, findings, results).
# - **Each member of a group presents for about 10 minutes** and will be graded individually.
# - You must attend every presentation, not just your own.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Organization
# - The Git repository `https://gitlab.lrz.de/fspanhel/dsc`
#     - Information about the repo, e.g., how to clone it and setup the environment can be found in [README.md](../../README.md).
#     - The file [COURSE.md](../../COURSE.md) is the **central source of information** for this course.
#         - Organizational updates in the repo will be mentioned in this file.
#         - It will be updated regularly.
#     - Material for the lecture and the tutorial will be provided at [/lecture notes](../lecture_notes).
# - Data
#     - Click [here](https://syncandshare.lrz.de/getlink/fiVWchss6RorJVL3LDR47D/dsc.db) to download the first version of the database that we use in this course.
#     - I recommend to save the database as data/dsc.db in this project (meaning that the parent folder of data is the root of this Git repo)
# - Contact
#     - You can always write an eMail to spanhel@hm.edu
#     - However, I won't check my eMails on a daily basis and may need some time to respond...
# - Office hours
#     - I don't have a regular office hour.
#     - Just write me an eMail if you want to have a more detailed discussion before/after the lecture starts/tutorial ends.
# - Moodle
#     - Do we need a moodle course? 
#     

# %% [markdown] slideshow={"slide_type": "slide"}
# # Prerequisites
# Basic knowledge of 
# - Unix shell, e.g., bash or zsh
#     - You should know the commands ```pwd, cd, ls, cp, mv``` and now how to access files and directories using ```.., .```
# - Python3 (basic built-ins, pandas, scikitlearn)
# - Juypter notebooks
#     - Starting a notebook from the terminal and viewing it with a browser
#     - Command/Edit mode. Code and markdown cells.
# - Git    
#     - Adding and committing changes to Git
#     - Working with remotes, e.g., the difference between fetch and pull
#     - Working with branches, e.g., checkout branches and merging
#     - See [Git resources](COURSE.md) for brushing up your Git skills
# - Sql (simple queries with filters and joins)
#
# and
# a basic understanding of statics and machine learning (e.g., linear regression, boosting, trees...).

# %% [markdown] slideshow={"slide_type": "slide"}
# # Software and Tools

# %% [markdown] slideshow={"slide_type": "-"}
# Click [here](https://davidadrian.cc/definitive-data-scientist-setup/) for general setup recommendations.
#
# - For coding, I use a **linux** distribution as **operating systems** via WSL on windows.
#     - Using MacOS should be no problem
#     - Using Windows should also be no problem if you can emulate a unix shell like bash, e.g., [WSL] or [Git For Windows](https://gitforwindows.org/)
#         - I highly recommend to use [WSL]. 
#         - You can easily access [WSL] via [VSCode] using the [remote extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). 
#         - Click [here](https://code.visualstudio.com/docs/remote/remote-overview) for more information.
# - We will be using **Python3** for data manipulation and data modeling.
# - [**Jupyter notebooks**](https://jupyter.org/) (in combination with [RISE](https://rise.readthedocs.io/en/stable/)) will be used for presenting the lecture notes
# - I use [VSCode] for coding but you can use any IDE (e.g., [PyCharm](https://www.jetbrains.com/de-de/pycharm/)) you want.
#     - If you want to use VSCode without tracking check these [free release binaries](https://github.com/VSCodium/vscodium/blob/master/README.md#supported-os)
#     - The following VSCode extensions are useful for this course:
#         - Python
#         - Pylance
#         - GitLens
#         - GitGraph
#
# [WSL]: (https://learn.microsoft.com/en-us/windows/wsl/install)
# [VSCode]: (https://code.visualstudio.com/)

# %% [markdown] slideshow={"slide_type": "slide"}
# **Sofware and Tools Cont'd**:
#     
# - We will be using [**conda**](https://docs.conda.io/en/latest/miniconda.html) (or [mamba](https://github.com/mamba-org/mamba)) for package and environment management
# - We will be using **Git**, [**DVC**](https://dvc.org/) and **Gitlab** for version control
# - Gitlab will be used for collaboration and project management
# - We will be using [**DBeaver**](https://dbeaver.com/edition/) as SQL client software -> **please download DBeaver now!**
# - We will be using [**Google Drive**](https://www.google.com/intl/de/drive/) or [**LRZ Sync+Share**](https://www.rz.hm.edu/studierende_4/lrz_sync___share_1/index.de.html) for remote data storage. For each project there will be one remote data storage.
# - For **instant-messaging** you could use [**RocketChat**](https://de.rocket.chat/), [**Slack**](https://slack.com/intl/de-de/) or alternatives...
# - It's also helpful to have the command 'tree' available in your shell of choice.
#
# **Please make sure that the software runs on your computer!**

# %% [markdown]
# # Setting up the repo

# %% [markdown]
# ## Cloning
# - To copy this remote repository to a local repository you need [Git] which should already be installed if you are using a unix-based OS. 
#
# - If your OS is Windows you can use [WSL] or [Git For Windows]. 
#     - I highly recommend to use [WSL]. 
#     - You can easily access [WSL] via [VSCode] using the [remote extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). 
#     - Click [here](https://code.visualstudio.com/docs/remote/remote-overview) for more information.
#
# - To clone the repo with SSH, run the following command in the terminal.
#
#     ```
#     git clone git@gitlab.lrz.de:fspanhel/dsc.git
#     ```
#
# - Clike [here](https://docs.gitlab.com/ee/user/ssh.html) how to use SSH keys to communicate with GitLab.
#
# - Alternatively, you can clone with HTTPS using
#
#     ```
#     git clone https://gitlab.lrz.de/fspanhel/dsc.git
#     ```
# [Git]: https://git-scm.com/
# [Git for Windows]: https://gitforwindows.org/
# [WSL]: https://learn.microsoft.com/en-us/windows/wsl/install
# [VSCode]: https://code.visualstudio.com/

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Setting up the environment

# %% [markdown] slideshow={"slide_type": "slide"}
# In order to set up the necessary environment you need [(mini)conda](https://docs.conda.io/en/latest/miniconda.html) (or [mamba]).
#
# ### Installing miniconda on linux
# - Run
# ```wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh``` in the terminal to download miniconda.
# - Run ```bash Miniconda3-latest-Linux-x86_64.sh``` to install miniconda. Press space to scroll down when you read the terms and agree to them by typing 'yes'.
# - Close the terminal or run ```source ~/.bashrc```.
# - You should now be able to activate conda by typing ```conda activate```.
# - If not, try ```conda init''' and then ```conda activate``` again.
# [mamba]: https://github.com/mamba-org/mamba

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Creating the environment
# - From the root directory of the cloned git repo, you can create the 'dsc' environment by running  ```conda env create -f environment.yml``` in the terminal.
# - Setting up the environment takes a while (mamba is much faster).
# - You can activate the environment using ```conda activate dsc```.  
#
# - You should always activate the environment when you are working with this Git repo.
# - If you are using VS Code you can find [here](https://code.visualstudio.com/docs/python/environments#_work-with-python-interpreters) instructions how to automatically activate the environment when you open the `dsc` folder with VS Code.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Starting notebook servers
# In the terminal, run ```jupyter notebook``` to start a notebook server which can be accessed via a browser.
# - To set the notebook extensions, run ```python3 -m dsc.notebook``` in the terminal. 
#   - If ~/.jupyter/nbconfig/notebook.json exists already, please edit ~/.jupyter/nbconfig/notebook.json by considering nbconfig.json accordingly.
#   - Note that the notebook extensions are only considered the next time you launch a Juypter notebook server.
# - To present notebooks located in /lecture_notes as slides press alt + r (on Windows). You might need to zoom out so that everything is visible on a slide. 

# %% [markdown] slideshow={"slide_type": "slide"}
# # Ask questions and share impressions
# You can ask questions verbally at any time directly in this course. 
#
# In addition, you can use an **interactive room** provided by https://particify.de/ to
# - Ask and upvote questions -> Q & A.
# - Give live feedback.
# - Answer questions that help me set priorities for the course and get to know you better.
#
# From the next week on, I will be posting the link to the corresponding interactive room at the beginning ot the lecture.
#
# At the **beginning of each exercise**, I will **unlock questions that relate to the following week's material**.

# %% [markdown] slideshow={"slide_type": "slide"}
# Today is the exception and we start with some general questions that are already unlocked.
#
# Please use https://partici.fi/83687465, or scan the QR code below, to join the interactive room.

# %% [markdown] slideshow={"slide_type": "-"}
# <div align="center">
# <img src="./figures/0_p.png" alt="drawing" width="1200"/>
# </div>
#
# <div align="left" style="font-size:16px;">
# <div/>
