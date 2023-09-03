- [Purpose](#purpose)
- [Grading aspects](#grading-aspects)
  - [Git commit history](#git-commit-history)
  - [Readme/Project description](#readmeproject-description)
  - [Scripts](#scripts)
    - [Training](#training)
    - [Prediction](#prediction)
  - [Issues and MR](#issues-and-mr)
  - [Code](#code)
  - [Methodology](#methodology)
- [Pushing a project as a branch of dsc\_private for grading](#pushing-a-project-as-a-branch-of-dsc_private-for-grading)
- [Pushing a project as a branch of dsc for sharing](#pushing-a-project-as-a-branch-of-dsc-for-sharing)


# Purpose
Use the following points to grade the student's project works.

# Grading aspects

## Git commit history
- [ ] Confusing because no rebase of feature branches that were branche off from another feature: [Yes|No]
- [ ] Formatting:
- [ ] Tidy because interactive rebase has been used:


## Readme/Project description
- Mentioning of
  - [ ] Project Description
  - [ ] Git
  - [ ] DVC
  - [ ] Environment
  - [ ] How to run scripts
    - [ ] From where need the scripts to be run
    - [ ] Arguments clear
    - [ ] Where is the prediction stored
    - [ ] --help possible

## Scripts
### Training
- [ ] Input/Output clear
- [ ] Script runs with default arguments
- [ ] Script runs with provided time period

### Prediction
- [ ] Input/Output clear
- [ ] Script runs with default arguments
- [ ] Script runs with provided time period

## Issues and MR
- Description
- Discussion

## Code
- [ ] Docstrings
- [ ] Type hints
- [ ] Readability/Structure of main and functions
- [ ] Style/Formatting: Was Black used
- [ ] PEP8 Style violations
- [ ] DRY


## Methodology
- [ ] Query: Are left joins used
- [ ] Project 1
    - [ ] Are all movies modeled and predicted
    - [ ] Consider PT correctly
    - [ ] Consider the right target group
    - [ ] Features
        - [ ] Use of last run?
- [ ] Project 2
    - [ ] Computation of Sehb and Market Share correct?
    - [ ] Consider the right target group
    - [ ] Which channels
    - [ ] Did they consider START_TIME_AGF correctly?

- [ ] Cross validation
- [ ] Do the predictions make sense?



# Pushing a project as a branch of dsc_private for grading
In order to check these points I
1. Create the folder dsc_projects.
2. Clone each project into this folder and cd into the folder.
3. Push each repo's main branch to the dsc_private remote using.
    ```
    # https://devconnected.com/how-to-push-git-branch-to-remote/
    git remote add dsc_private git@gitlab.lrz.de:fspanhel/dsc_private.git &&
    repo_name=$(basename "$PWD") &&
    git push dsc_private submission:$repo_name
    ```
4. Make a MR in dsc_private and add notes to the code using this MR.

# Pushing a project as a branch of dsc for sharing
In order to provide the project works to all students I
1. Create the folder dsc_projects.
2. Clone each project into this folder and cd into the folder.
3. Push each repo's main branch to the dsc branch of the hm remote using.
    ```
    # https://devconnected.com/how-to-push-git-branch-to-remote/
    git remote add dsc git@gitlab.lrz.de:fspanhel/dsc.git &&
    repo_name=$(basename "$PWD") &&
    git push dsc submission:$repo_name
    ```
4. Make a MR in dsc
