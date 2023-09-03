- [Purpose](#purpose)
- [Create groups and repos](#create-groups-and-repos)
- [Configure repo](#configure-repo)
- [Possibly reset submission to the initial commit of the main branch](#possibly-reset-submission-to-the-initial-commit-of-the-main-branch)


# Purpose
Everything that I need to setup that the student's can begin with their project work.

#TODO: Is the submission branch necessary? Can I just use main? When I use submission should I set it to the default?

# Create groups and repos
1. Create gitlab group and assign members (including me)
2. Create repo and assign the team

# Configure repo
- Create dsc_project_template
  - Add a new branch called `submission` which is protected
  - In Setting/Repository/Protected branches (changes are automatically saved)
    - protect `submission` with:
      - allowed to merge: maintainer
      - allowed to push: no one
      - allowed to force push: no
    - protect `main` (default) with:
      - allowed to merge: maintainer + dev
      - allowed to push: no one
      - allowed to force push: no
  - In Settings/Merge requests/Merge requests
    - Enable "Delete source branch" option by default -> Uncheck
    - Squash commits when merging -> Require
    - Click on "save changes"
- Export dsc_project_template using Settings
- Import this repo using https://stackoverflow.com/a/55278088
- Settings/Repository/Protected branches & Settings/Merge requests/Merge requests have to be edited again :(
- But at least the branches remain...
- Set my profile to private so that students can't see what I am doing https://gitlab.lrz.de/help/user/profile/index.md#make-your-user-profile-page-private
- Nur 10 Projekte auf GitLab verfügbar, siehe auch https://doku.lrz.de/display/PUBLIC/GitLab#GitLab-Speicherplatz, ich sollte für meine privaten Repos eine Gruppe erstellen

# Possibly reset submission to the initial commit of the main branch
```
git checkout main &&
ic=$(git rev-list --max-parents=0 --abbrev-commit HEAD) # initial commit
git checkout submission &&
git reset --hard $ic
git push -f
```
