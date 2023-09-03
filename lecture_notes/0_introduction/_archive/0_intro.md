```python
from dsc.notebook import embed_website
```

<div align="center" style="font-size:70px;">
WELCOME TO THE DATA SCIENCE CHALLENGE!
<div/>

<div align="left" style="font-size:16px;">
<div/>

# Outline of the introduction
- About me
- Motivation
- Information about this course
    - Structure & organization
    - Examination requirements
    - Prerequisites and tools

# About me

<div align="center">
<img src="./figures/0_me.png" alt="Dr. Fabian Spanhel" width="500"/>
</div>

<div align="left" style="font-size:16px;">
<div/>

<div align="center" style="font-size:20px;">
Dr. Fabian Spanhel
<div/>

<div align="left" style="font-size:14px;">
<div/>
<br>

- Studied economics with a focus on econometrics & statistics
- PhD in statistics
- Since November 2016 working as a Data Scientist at ProSiebenSat.1
- Aquarius, INTJ, likes doing sports
- Social media:
    - https://www.linkedin.com/in/fspanhel/
    - https://vm.tiktok.com/ZMFJFtD7y/

# Motivation: Is data scientist still the sexiest job of the 21st century?
The article titled ["**Data Scientist: The Sexiest Job of the 21st Century**"](https://hbr.org/2012/10/data-scientist-the-sexiest-job-of-the-21st-century) published in 2012 is a very popular article that contributed to popularize data science.

At this time:

- The role data scientist "was relatively new, but as more companies attempted to make sense of **big data**,
they realized they needed people who could **combine programming, analytics, and experimentation skills**."
- The were assumed be **unicorns** and do all required tasks — from conceptualizing the use case, to
interfacing with business and technology stakeholders, to developing the algorithm and deploying it into production.
-"Because there wasn’t yet a well-defined career path for people who could program with and
analyze such data, **data scientists had diverse educational backgrounds**."
- "Most had **PhDs** in some scientific field, were exceptional at math, and knew how to code. Given the **absence of tools and processes**."
- To "perform their roles, they were also good at **experimentation and invention**."


The article titled ["**Is Data Scientist Still the Sexiest Job of the 21st Century?**"](https://hbr.org/2022/07/is-data-scientist-still-the-sexiest-job-of-the-21st-century) is the follow up of the previous mentioned article.

- A decade later, **AI is increasingly popular** in business and the job is more in demand than ever.
<!-- Nevertheless, there are issues: -->
<!--   - Much time of data scientist is spent cleaning and wrangling data. -->
<!--    - Many organizations don’t have data-driven cultures and don’t take advantage of the insights provided by data scientists. -->
<!--    - Many algorithms are never deployed. -->
- Now there are **hundreds of degree programs** in data science or the related fields of analytics and AI.
- **No data science unicorns anymore** but there are related jobs to handle many of those tasks, e.g., machine learning engineers, data engineers, advanced analytics, and data oriented product managers.
-  "We expect to see **continued differentiation of responsibilities** and
    roles that all once fell under the data scientist category".
- **Automated machine learning** might dim the demand of data scientists who primarily do model fitting for prediction.
- **MLOps** (Machine learning operations) which establishes best practices and tools to facilitate development and operationalization of AI becomes more important.
- "Most importantly, data scientists must contribute towards appropriate collection
of data, responsible analysis, and **translating business issues and requirements into fully-deployed models**, and successful business outcomes".

<img src="./figures/0_hierarchy.png" alt="The Data Science Hierarchy of Needs" width="1200"/>
<br>

[Source](https://www.reddit.com/r/datascience/comments/wi2gil/the_data_science_hierarchy_of_needs)

# Course objectives
- Learn something for your (professional) life
- Learn some the basics of writing good code which is suitable for production and usable by ml engineers
- Learn tools and methods to conduct reproducible data science and experiments and to collaborate in a team
- Learn how to model data where the time dimension is important
- Consolidate what you have learned through a collaborative practice project


**Revisiting old code**

Source: Taken from https://www.reddit.com/r/ProgrammerHumor/comments/vkz1sf/returning_to_an_old_project/


```python
embed_website("https://preview.redd.it/hcpdw2c62x791.gif?format=mp4&s=fe0549df40464566ea48e6b9659a582c7d8a9d20")
```





<iframe
    width="900"
    height="0"
    src="https://preview.redd.it/hcpdw2c62x791.gif?format=mp4&s=fe0549df40464566ea48e6b9659a582c7d8a9d20"
    frameborder="0"
    allowfullscreen

></iframe>




## What is good Data Science code?

1. Correct: The code should do what it is supposed to do.
2. Readable and Understandable: [More time is spent reading code than writing.](https://bayrhammer-klaus.medium.com/you-spend-much-more-time-reading-code-than-writing-code-bc953376fe19)
3. Reproducible: In order that Data Science experiments are reproducible we have to version code, data and models.
4. Portability, Scalability and Reusability: Code should be runnable in different environments (e.g., no hard-coded paths), adding new features should be possible, components should be resuable.
5. Executes fast.
6. Elegant.


**Good coding practices**
- KISS
- DRY
- ..

## Data with a time dimension
- The (possibly) **time dimension of data is often neglected** in academia and in practice
- In some cases, the time dimension has no effect on the Data Science task
- However, a lot of data is inherently temporal, e.g., a time series of observations
- **Disregarding this fact can result in false conclusions or suboptimal modeling**
- The collaborative practice projects all are based on data with a time dimension and should make you aware of this issue

# Structure of this course



## First part
The **first part** of this course (**October - November**) consists of **prepared lectures**
with notes and structured tasks that you can tackle in the tutorials.
We will cover
- Version control
- Setting up a Python project
- Good coding habits
- Project management and collaborative coding
- ...
- Model tracking with Mlflow and deployment

The **first part** should prepare you for successfully master your following **project challenges**.

## Second part
In the **second part**, starting in December, there will be no prepared lectures and you
will be **working on your project challenge** in the lecture and tutorial.

- You can **choose your project from 3 main projects**.
- Each project should be worked on by about **3 people**.
- The projects will be presented in the first lecture.
- Each student has to submit his/her preference for the projects in November (more details will follow).
- Each student will then be assigned to a project by considering his/her preferences.

I will support you by **answering questions and providing suggestions**.

Moreover, I will be having a look at your code and **approve pull requests** for the main
branch of your project.

# Examination requirements: ModA(0,6) + Präs(0,4)

In order to be graded, you have to
1. **Submit your project code**
2. **Give a presentation** about your project.

## Code submission
The code of your collaborative project must be submitted in the middle of January before the presentation (exact deadline will follow).
**The code submission should contain the following four components**:
1. **Notebooks** with exploratory analyses or findings.
2. A **Python package** with functions and classes which are used in the notebooks and the scripts
3. A **script for training a model** that can be called from the command line which
    1. loads a provided dataset
    1. engineers the features
    1. trains a model
    1. tracks the model with Mlflow
4. A **script for predicting data** that can be called from the command line which
    1. takes a registered model in mlflow
    1. predicts data on the basis of the provided dataset
    1. writes the predicted data to a file

Each member of a group will be graded according to his/her code commits/PRs and the quality of his/her written issues.

More details will follow during the course.

## Presentation
- Each group presents their work (task, approach, problems, findings, results) **after submitting their code** (exact dates will follow)
- **Each member of a group presents for about 10 minutes** and will be graded individually.

# Organization
- The Git repository https://gitlab.lrz.de/fspanhel/dsc_2022
    - The file [COURSE.md](../../COURSE.md) is the **central source of information** for this course.
        - Organizational updates in the repo will be mentioned in this file.
        - It will be updated regularly.
    - Material for the lecture and the tutorial will be provided at [/lecture notes](../lecture_notes).
    - Information about the repo, e.g., how to setup the environment can be found in [README.md](../../README.md).
- Contact
    - You can always write an eMail to spanhel@hm.edu
    - However, I won't check my eMails on a daily basis and may need some time to respond...
- Office hours
    - I don't have a regular office hour
    - Just write me an eMail if you want to have a more detailed discussion before/after the lecture starts/tutorial ends.
- Moodle
    - Do we need a moodle course?


# Prerequisites
Basic knowledge of
- Unix shell, e.g., bash or zsh
- Python3 (basic built-ins, pandas, scikitlearn)
- Juypter notebooks
- Git
    - Adding and committing changes to Git
    - Working with remotes, e.g., the difference between fetch and pull
    - Working with branches, e.g., checkout branches and merging
    - See [Git resources](COURSE.md) for brushing up your Git skills
- Sql (simple queries with filters and joins)

and
a basic understanding of statics and machine learning (e.g., linear regression, boosting, trees...).

# Software and Tools

- For coding, I use a **linux** distribution as **operating systems** via WSL on windows.
    - Using MacOS should be no problem
    - Using Windows should also be no problem if you can emulate a unix shell like bash, e.g., [Git For Windows](https://gitforwindows.org/) or use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
- We will be using **Python3** for data manipulation and data modeling.
- [**Jupyter notebooks**](https://jupyter.org/) (in combination with [RISE](https://rise.readthedocs.io/en/stable/)) will be used for the lecture notes
- I use [**VSCode**](https://code.visualstudio.com/) for coding but you can use any IDE (e.g., [PyCharm](https://www.jetbrains.com/de-de/pycharm/)) you want.
    - If you want to use VSCode without tracking check these [free release binaries](https://github.com/VSCodium/vscodium/blob/master/README.md#supported-os)
    - The following VSCode extensions are useful for this course:
        - Python
        - Pylance
        - GitLens
        - GitGraph

**Sofware and Tools Cont'd**:

- We will be using [**conda**](https://docs.conda.io/en/latest/miniconda.html) (or [mamba](https://github.com/mamba-org/mamba)) for package management and environment management
- We will be using **Git**, [**DVC**](https://dvc.org/) and **Gitlab** for version control
- Gitlab will be used for collaboration and project management
- We will be using [**DBeaver**](https://dbeaver.com/edition/) as SQL client software
- We will be using [**Google Drive**](https://www.google.com/intl/de/drive/) or [**LRZ Sync+Share**](https://www.rz.hm.edu/studierende_4/lrz_sync___share_1/index.de.html) for remote data storage. For each project there will be one remote data storage.
- For **instant-messaging** you could use [**RocketChat**](https://de.rocket.chat/), [**Slack**](https://slack.com/intl/de-de/) or alternatives...
- It's also helpful to have the command 'tree' available in your shell of choice.

**Please make sure that the software runs on your computer**

# Ask questions and share impressions
You can ask questions verbally at any time directly in this course.

In addition, you can use an **interactive room** provided by https://particify.de/ to
- Ask and upvote questions -> Q & A.
- Give live feedback.
- Answer questions that help me set priorities for the course and get to know you better.

From the next week on, I will be posting the link to the corresponding interactive room at the beginning ot the lecture.

At the **beginning of each exercise**, I will **unlock questions that relate to the following week's material**.

Today is the exception and we start with some general questions that are already unlocked.

Please use https://partici.fi/83687465, or scan the QR code below, to join the interactive room.

<div align="center">
<img src="./figures/0_p.png" alt="drawing" width="1200"/>
</div>

<div align="left" style="font-size:16px;">
<div/>
