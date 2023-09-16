- [Objectives](#objectives)
- [Structure](#structure)
  - [First part](#first-part)
  - [Second part](#second-part)
- [Examination requirements: ModA(0,6) + Präs(0,4)](#examination-requirements-moda06--präs04)
  - [Code](#code)
    - [Submission](#submission)
    - [Grading](#grading)
  - [Presentation](#presentation)
- [Git repo](#git-repo)
  - [Lecture notes](#lecture-notes)
- [Contact and office hours](#contact-and-office-hours)
- [Prerequisites](#prerequisites)
  - [Git resources](#git-resources)
- [Software and tools](#software-and-tools)


This file is the **central source of information** for this course.


# Objectives
Learn something for your (professional) life! &#128515;
- Learn some basics of **writing good code which is suitable for production** and usable by ML engineers.
- Learn tools and methods to **conduct reproducible data science experiments and to collaborate in a team**.
- Consolidate what you have learned through a **collaborative practice project**.

# Structure
This course consists of two parts.

## First part
- The **first part**, **which is expected to last until November 23**, consists of **prepared lectures**
with notes and tasks that you can tackle in the tutorials.
- We will cover
  - Source code and data version control.
  - Setting up and implementing a Python project (Virtual environments, project structure, creating a pip-installable package).
  - Good coding habits (Style, type hints, documentation, Git hooks).
  - Project management and collaborative coding using Git and GitLab.
  - ...
  <!-- - Model tracking with MlFlow and deployment. -->
- The first part is designed to prepare you to successfully master the following **project challenges** in the **second part**.
- It is expected that you **become familiar with the topics that we discuss in the first part before the second part starts**. Otherwise, you might run out of time in the second part!
- Moreover, I recommend that every student uses the first part to **investigate the data** for the projects so that they can make an informed decision about their project preferences that they tackle in the second part.

## Second part
- In the **second part**, **expected to start from November 24**, there will be no prepared lectures or tasks and you will be **working on your project challenge**  during the lecture and tutorial.
- You can **choose your project from 2 main projects** which are presented [here](lecture_notes/introduction_0/1_data_and_projects.ipynb).
- Each project should be worked on by about **4 people**.
- Each student has to submit his/her preference for the projects by no later than **Wednesday, November, 1**.
- For this purpose, write an eMail to spanhel@hm.edu with the subject '**dsc project preference**' which includes
    - Your **full name**.
    - The **number of your preferred project**.  
- Each student will then be assigned to a project by considering his/her preferences by no later than **Friday, November 3, 2022**.
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


# Examination requirements: ModA(0,6) + Präs(0,4)

In order to be graded, you have to **submit your project code** and then **give a presentation** about your project.

## Code
### Submission
- Before your project starts, you will be provided with a remote Git repo hosted on GitLab with the two branchens `main` and `submission`.
- The code of your collaborative project must be submitted <span style="color:red">**before**</span> **Sunday, January 14, 2023**.
- **Submitted means** that on 2023-01-14 00:00:00 an attempt will be made to merge all active merge requests whose target branch is `submission`.
- Your project will then be evaluated on the state of the `submission` branch after this attempt has been made.
- Note that merge requests that cannot be merged will not be considered and you as a team are responsible for ensuring that I can run your code.
- **The code submission should contain the following four components**:  
  1. **Notebooks** with exploratory analyses or findings.
  2. A **Python package** with functions and classes which are used in the notebooks and the scripts
  3. A **script for training a model** that can be called from the command line which  
      1. Loads a provided dataset
      2. Engineers the features
      3. Trains a model
      4. Stores the model, e.g., with MLflow
  4. A **script for predicting data** that can be called from the command line which
      1. Loads a model, e.g., by taking a registered model in Mlflow.
      2. Predicts data on the basis of the provided dataset
      3. Writes the predicted data to a file  
### Grading
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
  - To measure the individual performance, I consider his/her participation in the project work during the lecture and tutorial, his/her code commits/MRs and the quality of his/her written GitLab issues.


## Presentation
- The presentations will take place on **Friday, January 19, 2023,** in room R2.012 from **15:00-19:00**.
- Each group presents their work (task, approach, repo overview, problems, findings, results).
- **Each member of a group presents for about 10 minutes** and will be graded individually.
- You must attend every presentation, not just your own.

# Git repo
Please have a look at [README.md](README.md). There you can find also information about how to setup the environment.
## Lecture notes
Material for the lecture and the tutorial is provided in the folder [`lecture notes`](lecture_notes).

<!--
## Data
- Click [here](https://syncandshare.lrz.de/getlink/fiVWchss6RorJVL3LDR47D/dsc.db) to download the first version of the database that we use in this course (available until the end of this year).
- I recommend to save the database as `data/dsc.db` in the root folder of this project.
-->

# Contact and office hours
- Contact
    - You can always write an eMail to spanhel@hm.edu
    - However, I won't check my eMails on a daily basis and may need some time to respond...
- Office hours
    - I don't have a regular office hour
    - Just write me an eMail if you want to have a more detailed discussion before/after the lecture starts/tutorial ends

# Prerequisites
Basic knowledge of
- Unix shell, e.g., bash or zsh.
    - You should know the commands ```pwd, cd, ls, cp, mv``` and now how to access files and directories using ```.., .```
- Python3 and standard data science packages like pandas or scikitlearn.
- Juypter notebooks
    - Start a notebook from the terminal and viewing it with a browser.
    - Command/Edit mode.
    - Code and markdown cells.
- Git  
    - Adding and committing changes to Git.
    - Working with remotes, e.g., the difference between fetch and pull.
    - Working with branches, e.g., checkout branches and merging.
    - See [Git resources](#git-resources) for brushing up your Git skills.
- SQL: Simple queries with filters and joins

And a basic understanding of statics and machine learning (e.g., linear regression, boosting, trees...).

## Git resources
If you want to brush up your Git skills I recommend
- [One of best introductions to using Git](https://www.atlassian.com/git/tutorials/what-is-version-control)
- [Official website](https://git-scm.com/about)
- [The pro Git book](https://git-scm.com/book/en/v2)
- [A visual Git reference](https://marklodato.github.io/visual-git-guide/index-en.html)
- Interactive games:
    - [Oh my Git](https://ohmygit.org): Needs to be installed.
    - [Learn Git branching](https://learngitbranching.js.org): I recommend to play this at least once.
- [Cheat sheet](https://wac-cdn.atlassian.com/dam/jcr:e7e22f25-bba2-4ef1-a197-53f46b6df4a5/SWTM-2088_Atlassian-Git-Cheatsheet.pdf?cdnVersion=543)

# Software and tools
Click [here](https://davidadrian.cc/definitive-data-scientist-setup/) for general setup recommendations.

- I use [VSCode] as IDE and recommend to use this IDE for this course.
- For coding, I use a **Linux** distribution as **environment** via WSL on windows.
    - If you have a unix-based operating system, like Linux or MacOS you should be fine.
    - On Windows you should you use the Windows Subsystem for Linux ([WSL]) to run a Linux environment.
        - Otherwise, it might happen that some code of this repo does not run.
    - You can easily access [WSL] via [VSCode] using the [remote extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). Click [here](https://code.visualstudio.com/docs/remote/remote-overview) for more information.
- We will be using **Python3** for data manipulation and data modeling.
- [**Jupyter notebooks**](https://jupyter.org/) (in combination with [RISE](https://rise.readthedocs.io/en/stable/)) will be used for presenting the lecture notes.

- We use [**conda**](https://docs.conda.io/en/latest/miniconda.html)/[**mamba**](https://github.com/mamba-org/mamba) for package and environment management.
- We use **Git**, [**DVC**](https://dvc.org/) and **Gitlab** for version control.
- Gitlab will be used for collaboration and project management.
- We use [**DBeaver Community**](https://dbeaver.io/download/) as SQL client software.
- We use [**Google Drive**](https://www.google.com/intl/de/drive/) for remote data storage.
  <!-- or [**LRZ Sync+Share**](https://www.rz.hm.edu/studierende_4/lrz_sync___share_1/index.de.html) -->
- It's also helpful to have the command 'tree' available in your shell of choice.

The installation of these tools is documented in the chapter "Setting up the software" of the lecture [lecture_notes/0_introduction/0_intro.ipynb](lecture_notes/0_introduction/0_intro.ipynb)

**Please make sure that the software runs on your computer!**

[WSL]: https://learn.microsoft.com/en-us/windows/wsl/install
[VSCode]: https://code.visualstudio.com/
[projects]: lecture_notes/0_introduction/1_data_and_projects.ipynb#Projects
