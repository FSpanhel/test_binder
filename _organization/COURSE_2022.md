# Course overview

This file is the **central source of information** for this course and will be updated on a regular basis. Check [Updates](#updates) occasionally to see what has changed.

## Updates
- 2022-10-03: Add project setup and information about this course. Please have a look at this document and [README.md](README.md). Alternatively you can use a browser to view the [Documentation](./docs/_build/html/index.html).
- 2022-10-07
    - Add lecture_notes/0_introduction/
- 2022-10-14
    - In lecture_notes/0_introduction the following updates have been done:
        - 1_data.ipynb was renamed into 1_data_and_projects.ipynb.
        - A final slide to 1_data_and_projects.ipynb was added which contains some general remarks on the project work which were also discussed in the lecture.
        - Information about the relation between RUN_ID and B_ID was added to the section Mapping_gfk_cdm of 1_data_and_projects.ipynb
        - 2_excercise.ipynb was updated with more questions.
    - Database
      - The field C_HIGHEST_NUMBER_OF_VISITORS_GERMANY i now an integer.
      - Please [download](https://syncandshare.lrz.de/getlink/fiVWchss6RorJVL3LDR47D/dsc.db) the database again.
      - The fields C_SERIES_ID, C_SERIES were added and are explained in  1_data_and_projects.ipynb.
    - Add lecture_notes/1_version_control
- 2022-10-15
    - [README.md](README.md)
      - Add more explanations
        - How to set up the conda environment.
        - How to start a Jupyter notebook server.
        - How to set Jupyter notebook extensions.
      - You can now use ```python3 -m dsc.notebook``` to set the notebook extensions, see also [README.md](README.md).
- 2020-10-22
  - Update lecture_notes/1_version_control/3_exercise.ipynb and add solutions
- 2020-10-28
  - Add lecture_notes/2_setup_python_project
- 2020-11-04
  - Update lecture_notes/2_setup_python_project
    - Update 2_python_project.ipynb
    - Add code_structure/0_messy_notebook.ipynb
- 2020-11-12
  - **Fix deadlines for the code submission and the presentation, see [code submission](#submission) and [presentation](#presentation)**.
  - Provide [information](#grading) how the code submission is graded.
  - Add more [information](#second-part) about the project work and how to submit your project preferences.
  - Update leture_notes/0_introduction/0_intro.ipynb accordingly.
- 2022-12-23
  - Update the Git workflow in lecture_notes/4_collaboration_and_project_management/collaboration_and_project_management.iypnb

## Objectives
- Learn something for your (professional) life.
- Learn some basics of writing good code which is suitable for production and usable by ML engineers.
- Learn tools and methods to conduct reproducible data science experiments and to collaborate in a team.
- Learn how to model data where the time dimension is important.
- Consolidate what you have learned through a collaborative practice project.

## Structure
This course consists of two parts.

### First part
- The **first part** of this course, **which lasts until November 24**, consists of **prepared lectures**
with notes and tasks that you can tackle in the tutorials.
- We will cover
  - Version control
  - Setting up a Python project
  - Good coding habits
  - Project management and collaborative coding
  - ...
  - Model tracking with Mlflow and deployment
- The first part is designed to prepare you to successfully master your following **project challenges**.
- It is expected that you **have a detailed look at the topics that we discuss in the first part before the second part starts**. Otherwise, you might run out of time in the second part!
- Moreover, I recommend that every student uses the first part to **familiarize themselves with the data** for the projects so that they can make an informed decision about their project preferences in the second part.

### Second part
- In the **second part**, **starting from November 25**, there will be no prepared lectures or task and you will be **working on your project challenge**  during the lecture and tutorial.
- You can **choose your project from 3 main [projects]**.
- Each project should be worked on by about **4 people**.
- Each student has to submit his/her preference for the projects in November by no later than **Wednesday, November 23, 2022**.
- For this purpose, write an eMail to spanhel@hm.edu with the subject 'dsc project preference' which includes your full name and an enumerated list containing the numbers of **all** [projects] that is **sorted by your preference**.
- Each student will then be assigned to a project by considering his/her preferences by no later than **Friday, November 25, 2022**.
  - If there is more than one group for a project, the assignment of students to a group will be random.
- I will support you during the second part by **answering questions and providing suggestions** during the lecture and tutorial.
- Moreover, I will have a look at your code and **approve merge requests** for the main
branch of your project.
- I **highly recommend** that we discuss your work on the following topics on the following dates
    - December 2: Setup, data import and basic feature building.
    - December 9: Setting up cross-validation for a benchmark model and estimating the prediction error.
    - December 16: Optimization of feature creation, model fitting, and cross-validation.
    - December 23: Code modularization and creation of scripts.
    - January 13: Final discussion on open points.
- I also recommend that **you have already worked on the topics that we discuss** on a date so that I can provide feedback and suggest further steps. This way you can get the most out of it.
- Therefore, you should start your project work from November 25, 2022.
- I will be able to talk to each group for at least (90 * 2) / [number of groups] minutes during the lecture/tutorial. If a group requires less time, the available time for other groups will increase correspondingly.


## Examination requirements: ModA(0,6) + Präs(0,4)

In order to be graded, you have to **submit your project code** and then **give a presentation** about your project.

### Code
#### Submission
- Before you project starts, you will be provided with a remote Git repo hosted on GitLab with the two branchens `main` and `submission`.
- The code of your collaborative project must be submitted <span style="color:red">**before (!)**</span> **Sunday, January 15th, 2023**.
- **Submitted means** that at 2023-01-15 00:00:00 an attempt will be made to merge all active merge requests whose target branch is `submission`.
- Your project will then be evaluated on the state of the `submission` branch after this attempt has been made.
- Note that merge requests that cannot be merged will not be considered and you as a team are responsible for ensuring that I can run your code.
- **The code submission should contain the following four components**:  
  1. **Notebooks** with exploratory analyses or findings.
  2. A **Python package** with functions and classes which are used in the notebooks and the scripts
  3. A **script for training a model** that can be called from the command line which  
      1. Loads a provided dataset
      2. Engineers the features
      3. Trains a model
      4. Stores the model, e.g., with Mlflow
  4. A **script for predicting data** that can be called from the command line which
      1. Loads a model, e.g., by taking a registered model in Mlflow.
      2. Predicts data on the basis of the provided dataset
      3. Writes the predicted data to a file  
#### Grading
- **The grading of the code submission focusses on the following points**:
  - How was your **organization** as a team?
    - Did you communicate well and approach the challenge in a structured way?
    - How did you use GitLab and Git to organizate your tasks and document your working steps? For instance, did you create good issues and merge requests?
  - To what extent did you **address the challenges of the project**?
  - How is the **overall code structure**?
    - How long do I need to understand what you have done?
    - Is it pleasant or rather akward to work with your code?
  - Did you apply **best practices** that we discussed in this course, e.g.,
    - Usage of reproducible virtual environments.
    - Version control (Source code and data).
    - Setting up a Python project (Folder structure, documentation, prototying in notebooks, structuring library code into modules and packages).
    - Readable code (PEP8 compliant, modularized and understandable, no [spaghetti code](https://en.wikipedia.org/wiki/Spaghetti_code)).
    - The best practices that I suggest are suggestions. You are free to apply other/additional best practices.
  - Is the **code functional**?
    - Can the model be trained on new data?
    - Can the model use new data for predictions?
    - Are there some rather obvious problems with your code? For instance, does it break when I want to change an input that should be modifiable?
  - Is the training of your model and the estimation of its prediction performance **methodologically sound**?
    - How well does your cross validation mimic the use case?
    - Did you consider relevant features?
    - It is not important that your model generates top notch predictions. Keep it simple.
- The grading for a student takes its **individual performance and the team performance** into account.
  - To measure the individual performance, I consider his/her participation in the project work during the lecture and tutorial, his/her code commits/PRs and the quality of his/her written GitLab issues.


### Presentation
- The presentations will take place on **Friday, January 20th, 2023,** in room R2.012 from **15:00-19:00**.
- Each group presents their work (task, approach, repo overview, problems, findings, results).
- **Each member of a group presents for about 10 minutes** and will be graded individually.
- You must attend every presentation, not just your own.

## Lecture notes
Material for the lecture and the tutorial is provided in the folder [`lecture notes`/](/lecture_notes).

## Git repo
Please have a look at [README.md](README.md). There you can find also information about how to setup a corresponding environment.

## Data
- Click [here](https://syncandshare.lrz.de/getlink/fiVWchss6RorJVL3LDR47D/dsc.db) to download the first version of the database that we use in this course (available until the end of this year).
- I recommend to save the database as `data/dsc.db` in the root folder of this project.

## Contact and office hours
- Contact
    - You can always write an eMail to spanhel@hm.edu
    - However, I won't check my eMails on a daily basis and may need some time to respond...
- Office hours
    - I don't have a regular office hour
    - Just write me an eMail if you want to have a more detailed discussion before/after the lecture starts/tutorial ends

## Prerequisites
Basic knowledge of
- Unix shell, e.g., bash or zsh
  - - You should know the commands ```pwd, cd, ls, cp, mv``` and now how to access files and directories using ```.., .```.
- Python3 (basic built-ins, pandas, scikitlearn)
- Juypter notebooks
    - Starting a notebook from the terminal and viewing it with a browser
    - Command/Edit mode.
    - Code and markdown cells.
- Git
    - Adding and committing changes to Git
    - Working with remotes, e.g., the difference between fetch and pull
    - Working with branches, e.g., checkout branches and merging
    - See [Git resources](#git-resources) for brushing up your Git skills
- Sql (simple queries with filters and joins)

and
a basic understanding of statics and machine learning (e.g., linear regression, boosting, trees...).

### Git resources
If you want to brush up your Git skills I recommend:
- [One of best introductions to using Git](https://www.atlassian.com/git/tutorials/what-is-version-control)
- [Official website](https://git-scm.com/about)
- [The pro Git book](https://git-scm.com/book/en/v2)
- [A visual Git reference](https://marklodato.github.io/visual-git-guide/index-en.html)
- Interactive games:
    - [Oh my Git](https://ohmygit.org): Needs to be installed.
    - [Learn Git branching](https://learngitbranching.js.org): I recommend to play this at least once.
- [Cheat sheet](https://wac-cdn.atlassian.com/dam/jcr:e7e22f25-bba2-4ef1-a197-53f46b6df4a5/SWTM-2088_Atlassian-Git-Cheatsheet.pdf?cdnVersion=543)

## Software and tools
Click [here](https://davidadrian.cc/definitive-data-scientist-setup/) for general setup recommendations.

- For coding, I use a **Linux** distribution as **operating systems** via WSL on windows.
    - Using MacOS should be no problem
    - Using Windows should also be no problem if you can emulate a unix shell like bash, e.g., [Git For Windows](https://gitforwindows.org/) or use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
      - I highly recommend to use [WSL].
      - You can easily access [WSL] via [VSCode] using the [remote extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack).
      - Click [here](https://code.visualstudio.com/docs/remote/remote-overview) for more information.
- We will be using **Python3** for data manipulation and data modeling.
- [**Jupyter notebooks**](https://jupyter.org/) (in combination with [RISE](https://rise.readthedocs.io/en/stable/)) will be used for the lecture notes
- I use [**VSCode**](https://code.visualstudio.com/) for coding but you can use any IDE (e.g., [PyCharm](https://www.jetbrains.com/de-de/pycharm/)) you want.
    - If you want to use VSCode without tracking check these [free release binaries](https://github.com/VSCodium/vscodium/blob/master/README.md#supported-os)
    - The following VSCode extensions are useful for this course:
        - Python
        - Pylance
        - GitLens
        - GitGraph
- We will be using [**conda**](https://repo.anaconda.com/miniconda/) (or [mamba](https://github.com/mamba-org/mamba)) for package management and environment management
- We will be using **Git**, [**DVC**](https://dvc.org/) and **Gitlab** for version control and collaboration. Gitlab will also be used for issue tracking and project management (?)
- We will be using [**DBeaver**](https://dbeaver.com/edition/) as SQL client software
- We will be using [Google Drive](https://www.google.com/intl/de/drive/) or [LRZ Sync+Share](https://www.rz.hm.edu/studierende_4/lrz_sync___share_1/index.de.html) for remote data storage. For each project there will be one remote data storage.
- For **instant-messaging** you could use [RocketChat](https://de.rocket.chat/), [Slack](https://slack.com/intl/de-de/) or alternatives...
- It's also helpful to have the command 'tree' available in your shell of choice.

Please make sure that the software runs on your computer (!).

[WSL]: https://learn.microsoft.com/en-us/windows/wsl/install
[VSCode]: https://code.visualstudio.com/
[projects]: lecture_notes/0_introduction/1_data_and_projects.ipynb#Projects
