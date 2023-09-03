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

# %% slideshow={"slide_type": "notes"}
from dsc.notebook import embed_website


# %% [markdown] slideshow={"slide_type": "slide"}
# # Good Git commit messages

# %% [markdown] slideshow={"slide_type": "-"}
# - Recall that using Git alone does not result in good version control...
# <div align="left">
# <img src="./figures/vc_intro_commitstrip.png" alt="VC" width=700/>
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# - You don't need to care about the content of your commits and their messages if you 
#     - Never look back.
#     - Don't use ```git log```.
#     - Don't collaborate.
# - However, if you are interested in why something happened and want to maintain a project over a long period of time, you should definitely try to make [atomic commits](https://www.freshconsulting.com/insights/blog/atomic-commits/), use rebase to tidy up your commit history, and try to write good commit messages.  
# - Writing good commit messages is hard and often neglected. 
# - [How to Write a Git Commit Message](https://cbea.ms/git-commit/): "A well-crafted Git commit message is the best way to communicate context about a change to fellow developers (and indeed to their future selves). A diff will tell you what changed, but only the commit message can properly tell you why."
# - [Peter Hutterer](http://who-t.blogspot.com/2009/12/on-commit-messages.html): "A commit message shows whether a developer is a good collaborator".
# - Writing descriptive commit messages is useful for code reviews and future development.

# %% [markdown] slideshow={"slide_type": "slide"}
# - Similar to source code, there are some [style guidelines](https://cbea.ms/git-commit/) that you should consider when writing a commit message.
# - Separate the subject from the (optional) body with a blank line
# - The subject line should be
#     - Capitalized
#     - Limited to 50 characters (72 is the hard limit)
#     - Not be ended with a period
#     - Written in the imperative (which is Git's convention, e.g., ```Merge branch x into y```)
# - Wrap the body at 72 characters
# - If required, use the body to explain
#     - What is done in the commit.
#     - Why it is done.
#     - Why you chose this way and no other.  
# - Do not explain how the update was done. This is documented by the commit itself.
# - If possible, refer to a pull/merge request, issue, or comment that explains the commit.

# %% [markdown] slideshow={"slide_type": "subslide"}
# - An example:
#     
# ```
# Add load and store functions to the data module
#
# If we modularize the notebook into scripts, we need functions that
# store and load processed data.
# The pyscaffold_test.data module has been extended by these functions
# so that
# - scripts/fit.py stores the data that it processes.
# - scripts/predict.py loads the processed data.
#
# Resolves: #4
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# - When writing commit messages with a body, you should use ```git commit``` to open the text editor and not ```git commit -m```
# - The subject line of a commit is displayed in GitHub/GitLab or if you use ```git log --oneline```
# - There are also some [VsCode extensions](https://zhauniarovich.com/post/2020/2020-03-using-vscode-as-git-editor/) that help to formate a commit message.
# - To assign a commit to an author it is important that you configure Git in your project repo to use 
#     - As ```user.email``` your @hm.edu eMail.
#     - As ```user.name``` your first name followed by your last name, e.g, Fabian Spanhel. The ``user.name``` should be identical to your profile name on GitLab.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Working on a collaborative project with a Git management application 

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Motivation
# - A Git management application is a hosting service for software development and Git version control.
# - Popular examples are 
#     - [GitHub](https://github.com): The largest source code host. Best for public repos. Owned by Microsoft.
#     - [GitLab](https://gitlab.com/gitlab-org/gitlab): Must be self-hosted (?). Best for private repos.
#     - [BitBucket](https://bitbucket.org/product): From Atlassian with Jira integration. Best for private repos.
# - A Git management application hosts remote Git repos that you can use to perform pull and push operations.
# - Moreover, it simplifies the collaboration using Git and improves code developement by providing
#     - Access control.
#     - Issues to describe and discuss code changes and their tracking.
#     - Merge/Pull requests to discuss, review and approve code changes.
#     - Wikis for documentation.
#     - An easy way to fork repos.
#     - CI/CD.
# - We will discuss issues and merge/pull requests later in detail.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Workflow overview
# - Each fundamental change to the code should start with an **issue** that describes the task or feature.
# - Such an **issue** can be created in the browser user interface of the Git management application.
# - An issue is assigned to someone to work on it. 
# - Every code change related to this issue is done in a specifc **feature branch**.
# - A a **merge/pull request** is submitted by the developer if he/she wants to discuss or has finished his/her work on the feature.
# - A merge/pull request is a browser user interface provided by the Git management application to discuss, review, and integrate code changes.
# - When the code changes on the feature branch are completed, a reviewer is assigned.
# - If the reviewer agrees that the code is finished, the browser user interface can be used to merge the feature branch into the target branch.
# - Click [here](https://docs.gitlab.com/ee/topics/gitlab_flow.html) for a more detailed overview of how to use GitLab for collaboration.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Playground
# - In the following, you can use the [playground](https://gitlab.lrz.de/fspanhel/dsc_gitlab_playground) to get to know Gitlab and how it can be used for your project.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## [Issues](https://docs.gitlab.com/ee/user/project/issues/ )
# - Each fundamental change to the code should start with an issue that describes the task or feature.
# - By creating an issue you 
#     - Inform your team about what should be discussed or be done.
#     - Avoid that feature branches get too big because you have to think about the scope when writing the issue.
#     - Assign responsibilities. 
#     - Improve your workflow by
#         - Making use of the issue board to easily see what should be done and has be done. 
#         - Refering to it when making commit messages or merge/pull requests. 
# - It is necessary that every issue is addressed. You can also close them without modifying your code. In this case, the issue should contain information why it is not addressed.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Creating an issue
# - To create an issue click on `Issues` on the left sidebar of your Gitlab project and use the resulting site to create a new issue.
# - Click [here](https://gitlab.lrz.de/fspanhel/dsc_gitlab_playground/-/issues/1) to see an issue of the [playground](https://gitlab.lrz.de/fspanhel/dsc_gitlab_playground).
# - The issue title should describe the outcome of the issue. For instance, prefer "Cross validation should consider more than one fold" to "Cross validation considers only one fold".
# - Create a [label](https://docs.gitlab.com/ee/user/project/labels.html) for this issue, e.g., to create a corresponding column for the issue board.
# - When it is clear who should work on the issue, assign the issue to this person.
# - Create a branch for the issue from the main branch to work on it. 
# - For each issue there should be only one branch. But there can be one branch for several issues.
# - You can also use tasks to break the issue down into smaller parts or use a milestone to group several issues.
# - You can als create a pull/merge request from an issue.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## [Issue board](https://docs.gitlab.com/ee/user/project/issue_board.html)
# - With the issue board you can plan, organize, and visualize your workflow and manage your project.
# - It shows the issues your team is working on, the status of each issue and who the issue is assigned to.
# - You can use it as a [SCRUM](https://en.wikipedia.org/wiki/Scrum_(software_development) or [KANBAN](https://en.wikipedia.org/wiki/Kanban_(development) board. 
# - Regarding Data Science projects I recommend to use it as a KANBAN board.
# - You can create a new [list](https://docs.gitlab.com/ee/user/project/issue_board.html#issue-board-terminology) (a column on the issue board that displays issues matching certain attribute) by referrring to a [label](https://docs.gitlab.com/ee/user/project/labels.html)
# - You can also use multiple issue boards (e.g., one for data processing, one for modeling...).
# - Click [here](https://www.youtube.com/watch?v=vjccjHI7aGI&feature=youtu.be) to watch a video presentation of the issue board.

# %% slideshow={"slide_type": "slide"}
embed_website("https://docs.gitlab.com/ee/user/project/issue_board.html")

# %% [markdown] slideshow={"slide_type": "slide"}
# ## [Pull/merge requests](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
# - A **pull request (PR)** or **merge request (MR)** is the same concept. 
#     - GitHub and Bitbucket call this process a pull request because the first action is to pull the feature branch.
#     - GitLab call this process a merge request because the final action is to merge the feature branch.
# - A MR is a website to **discuss** and **review** code changes done in a feature branch and to **merge** it into another branch.
#     - Open a MR when you would like to **discuss** the work in progress or have **completed** your work on the feature branch.
#     - After discussion and review, the code of the branch of the MR can be **merged** into a target branch.
# - The underlying process of a MR is designed to **maintain code quality**, **prevent errors**, and ensure that the **changes align with the repo's goals and standards**.
# - Note that your feature branch is considered to be public when it is attached to a corresponding MR, so **be careful with rebasing the branch of a MR**

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Creating a MR
# - It's best to create a MR with corresponding branch directly from an [issue](https://gitlab.lrz.de/fspanhel/dsc_gitlab_playground/-/issues/1).
#     - It's fine if several issues can be resolved by a MR but there shouldn't be several MRs that resolve one issue.
# - To see the resulting MR click [here](https://gitlab.lrz.de/fspanhel/dsc_gitlab_playground/-/merge_requests/1).
# - When you create a MR, include in its description 
#     - A summary of the changes and what problem they solve. 
#     - References to the corresponding issues.
#         - Gitab will then automatically refer to the MR in the reference issue.
#         - If you use [appropriate keywords](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically), the referenced issues will automatically be closed when the branch of the MR is merged to the default branch.
# - If you would like to have feedback or need help
#     - Start the title of the MR with "Draft: " to signal this and to prevent an unintended merge.
#     - Add general comments below the MR description or on specific lines of code, and alert persons by mentioning them using the "@" symbol followed by their alias, e.g. `@fspanhel`.
# - If you want a review for this MR, select a reviewer on the right sidebar who can approve and merge the MR.

# %% [markdown] slideshow={"slide_type": "slide"}
# An example pull request from the [GitHub docs](https://docs.github.com/assets/cb-155985/images/help/pull_requests/pull-request-body.png):
# <div align="left">
# <img src="https://docs.github.com/assets/cb-155985/images/help/pull_requests/pull-request-body.png" alt="PR example" width=1000/>
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### [Discussing and reviewing](https://gitlab.lrz.de/help/user/project/merge_requests/reviews/index.md#checkout-merge-requests-locally-through-the-head-ref)
# - You can use comments/threads below the MR for a general discussion.
# - If you want to point something out you can add comments directly on specific lines of changed files. 
#
# <div align="left">
# <img src="https://docs.github.com/assets/cb-37772/images/help/pull_requests/pull-request-comment.png" alt="Comment example" width=1000/>
# <div/>
#
# - Conversely, reviewers can comment on the whole MR or add comments to specific lines to ask questions or provide suggestions.
# - When commenting you can choose to start a review which bundles commits. 
# - Resolve a thread when the discussion about it is finished.
# - Note: In order to check whether the code of the MR is running you can fetch and then checkout the corresponding remote feature branch, e.g., ```git fetch --all && git checkout origin/feature_branch```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Updating
# - If a discussion or review reveals shortcomings, anyone can commit and push a fix. However, the person to do this is isually the creator of the MR.
# - If new commits are added to the branch of an open MR, the MR is updated accordingly. 
# - If the merged request has been closed, updates on the branch will not be considered in the merge request.
# - New commits or other updates in the MR (such as comments) are displayed at the bottom of the MR overview in the activity section.
# - Besides adding a commit directly with Git, you can also use comments in the browser user interface to make direct [suggestions](https://docs.gitlab.com/ee/user/project/merge_requests/reviews/suggestions.html).
#     - This is especially useful for small commits, e.g., typos, or when you are not the creator of the MR.
# - When you resolve one comment with a commit, you should refer to the comment link in the body of the commit message.
# - If you resolve a comment with a commit you should mention the corresponding commit hash, e.g, "Resolve by [commit hash]".

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Approving
# - The assigned reviewers can approve the MR.
# - Depending on the settings, approval might be required so that the merge of the MR can be performed.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Merging
# - After each comment has been resolved or approval has been given, the code of the feature branch can be integrated into the target branch. 
# - The decision on who merges a MR depends on the project's structure, size, and guidelines.
#     - In open source projects, it is typical that only repo maintainers can perform merges.
#     - In smaller projects, creators of the MR can merge after.
# - Depending on the settings, GitLab uses different [strategies](https://gitlab.lrz.de/help/user/project/merge_requests/methods/index.md) to merge the branches. 
# - By default, a merge commit is always created, even if a fast-forward merge is possible. 
# - It is also possible to [squash merges](https://gitlab.lrz.de/help/user/project/merge_requests/squash_and_merge.md) and delete the feature branch automatically. 
# - In general, you should delete the feature branch when it is no longer needed.
#     - By default, the remote feature branch is automatically deleted by GitLab after the merge.
#     - However, a corresponding local feature branch must be deleted manually, e.g., using `git branch -d feature-branch`.
#     - Note that deleted remote branches are still visible in Git unless you fetch with the flag `--prune`.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Code reviews
# - [Google's best practicses for good reviews](https://github.com/google/eng-practices/blob/master/review/index.md)
#     - Design: Is the code well-designed and appropriate for your system?
#     - Functionality: Does the code behave as the author likely intended? Is the way the code behaves good for its users?
#     - Complexity: Could the code be made simpler? Would another developer be able to easily understand and use this code when they come across it in the future?
#     - Tests: Does the code have correct and well-designed automated tests?
#     - Naming: Did the developer choose clear names for variables, classes, methods, etc.?
#     - Comments: Are the comments clear and useful?
#     - Style: Does the code follow our style guides?
#     - Documentation: Did the developer also update relevant documentation?

# %% [markdown] slideshow={"slide_type": "slide"}
# # Git workflows
#

# %% [markdown] slideshow={"slide_type": "slide"}
# - Git does not dictate how to interact with it but offers a high degree of freedom in how it can be used.
# - If your team has no convention how to work with Git, working with Git may be more cumbersome than it should be.
# - A Git workflow is a guideline how to use Git consistently and efficiently.
# - In particular, it often provides guidance for managing, creating, and combining branches.
# - There is no workflow that works best for all teams and projects.
# - As a result, may workflows have been proposed.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## [Archetypical flows](https://www.atlassian.com/git/tutorials/comparing-workflows)
# - [Centralized workflow](https://www.atlassian.com/git/tutorials/comparing-workflows#centralized-workflow)
#     - One central remote repo.
#     - There are not branches and everybody pushes to the main branch.
# - [Feature branch workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow): (read this at least once!)
#     - Uses one central remote repo and multiple branches.
#     - The main branch is the official project history in which all relevent changes eventually get merged into and which should never contain broken code. 
# <!-- This is the project repository at GitHub, GitLab, ... -->
#     - The development of each feature should be encapsulated in a corresponding feature branch that is branched off from the main branch.
#     - Feature branchs are developed locally and pushed to the corresponding feature branch of the remote repo.
#     - A pull/merge request is then submitted to integrate the feature branch into the main branch.e main branch.
# - [Forking workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow)
#     - Each developer has its own remote repo. 
#     - Often used for open-source projects. 
#     - A developer forks the official remote repo of the project maintainer, i.e., (s)he, or a Git hosting service, creates a own copy of the remote repo on a remote, and pushes changes to his/her private remote repo. 
#     - Pull/merge requests are used to integrate changes from a forked repo into the official remote repo.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## [Concrete flows](https://www.gitkraken.com/learn/git/best-practices/git-branch-strategy)
# - [Git flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow): Sophisticated feature branch workflow. 
#     - The first popular workflow. 
#     - Assigns specific roles to different branches and how and when they should interact. 
#     - May result in merge hell. 
#     - Click [here](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) and [here](https://www.youtube.com/watch?v=_w6TwnLCFwA) for more information.
# - [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow): Proposes to fork a repo before working on it with the feature branch workflow. 
# - [Atlassian flow](https://www.atlassian.com/blog/git/simple-git-workflow-is-simple): Like GitHub flow but rebases feature branches before merging so that the actual merge commit is just a marker for the feature branch and does not include any changed files.
# - [GitLab flow](https://docs.gitlab.com/ee/topics/gitlab_flow.html#mergepull-requests-with-gitlab-flow): Click [here](https://www.youtube.com/watch?v=InKNIvky2KE&feature=youtu.be) for a video.
# - [Trunk-based flow](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development). Feature branch workflow with very short-lived branches that are integrated into the main branch potentially several times a day. 
#     - Common practice among DevOps teams who use [CI/CD](https://www.atlassian.com/continuous-delivery).
#     - Click [here](https://cloud.google.com/architecture/devops/devops-tech-trunk-based-development) for more information.
# -  Click [here](https://docs.gitlab.com/ee/topics/gitlab_flow.html) and  [here](https://www.gitkraken.com/learn/git/best-practices/git-branch-strategy) for a comparions of some flows.
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Git flow
# - Uses two main branches to record the history of the project
#     - The branch `main` is the official release history and contains the production-ready code.
#     - The `dev` branch contains additional development changes for the next release.
# - The other branches have a limited life time, since they will be merged into `main` and `dev` and removed eventually and are categorized as
#     - Feature branches: Branches off from and is integrated back into `dev`.
#     - Release branches: Branches off from `dev`, is integrated back into `main`.
#     - Hotfix branches: Branches off from `main`, is integrated back into `main` and `dev`.
# - Note:
#     - If `dev`is considered to be the main branch, then the feature branch workflow is used for `dev` and the feature branches.
#     - If something is merged into `main` it must also be merged into `dev. 
# - See [here](https://nvie.com/posts/a-successful-git-branching-model) and [here](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) for more details.

# %% [markdown] slideshow={"slide_type": "slide"}
# Source: http://nvie.com/posts/a-succesful-git-branching-model
# <div>
# <img src="./figures/gitflow.png" alt="Git flow" width=700/>
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# # Your data science challenge project

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Branches and permissons
# - Each student has a developer role.
# - I am the maintainer of the project repo.
# - Each project repo starts with the branches `main` and `submission` and the following permissions
# <br>
# <div>
# <img src="./figures/permission.png" alt="Permissions" width=700/>
# <div/>
# <br>
#
# - That is, you can only integrate changes on `main` and `submission` by creating a MR. 
#     - You can perform the merge into `main`.
#     - Only I can perform the merge into `submission`.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## The Git workflow

# %% [markdown] slideshow={"slide_type": "slide"}
# - For data science projects which focus on analyses and experimentation, I think that the a simple feature branch workflow is adequate.
# - The Git workflow for your project is a simple feature branch workflow with an additional branch to which you submit your code for grading.
#
#     1. In general, you create a feature branch from the (up-to-date) branch `main`.
#     1. When a feature branch is completed, create a MR with the target beeing `main` and **assign @Fabian Spanhel as reviewer** (!).
#         1. If you don't assign me, I will not be notified and may not see this MR.
#         2. If have reviewed the MR I will add approve the MR.
#         3. You don't have to wait for my review before you merge. You can merge whenever you want. 
#         4. I might give you feedback on the MR after it has been merged.
#             1. If a change is required, I will open an issue and you can consider the change in a different MR.
#         5. If you just want feedback to an MR which is work-in-progress, do not assign me as a reviewer but refer to @Fabian Spanhel in a comment
#     1. You close the MR by performing the merge into `main` and deleting the feature branch (enabled by default).
#     1. Whenever you feel ready, you can create a MR of `main` into `submission` to submit your work.
#         1. Note that only I can perform the merge.
#         1. You should create all MRs with the target beeing `submission` before Sunday, January 15th, 2023, see [COURSE.md](../../COURSE.md#submission) for details.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Merge requests
# - The project uses the a [merge commit with semi-linear history](https://gitlab.lrz.de/help/user/project/merge_requests/methods/index.md#merge-commit-with-semi-linear-history) as merge method.
# - Moreover, squashing of commits is not possible.
# - I recommend to create a branch and a MR via the corresponding issue because then the issue and MR are linked.
#     - As a result, the issue is directly close when the merge of the MR is performed.
# - If you first create a branch directly, you should use the terminal to (interactively) rebase your (local) branch on `main` and then push it to the remote before you create the MR. 
# - In the MR, it may happen that you see the following note  
#
# <div align="left">
# <img src="./figures/merge_blocked.png" alt="Merge blocked" width=700/>
# <div/>
#
# - You can then rebase the (remote) branch on `main` by clicking on `Rebase` or `Rebase without pipeline`.
#     - However, if there are any merge conflicts you have to rebase your (local) branch using the terminal.
# - Note that an explicit merge commit is always created even when a fast-forward merge is possible.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Recommendations

# %% [markdown] slideshow={"slide_type": "-"}
# ### General 
# - Make use of all the tools that we have discussed in this course.
# - Start with a very simple model and focus on getting results.
# - You can always iterate and improve later but it is important that the basic structure is in place.
# - Ask questions and discuss.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Branches
# - First, create an issue for each significant feature. Then create the branch and the MR.
# - You don't have to create an issue if you are just doing a tiny change and this is evident from the MR.
# - Ideally, one person should work on one branch.
# - Rather use short-lived branches which focus on one feature than developing several features on one branch.
#     - Reduces the likelihood of merge conflicts.
#     - I can give feedback more frequently. 
# - Refer to issues in the merge commit message. 
# - Rebase private feature branches to tidy the commit history so that each commit contains an isolated and complete change.
# - Never ever rebase `main` or other public branches.
# - Use descriptive names for feature branches, like ```<author>__<branch-name>``` or ```<author>_#<issue-number>```.
#     - Click [here](https://stackoverflow.com/a/11886179) if you want to describe branches locally. However, referring to issues in the MR is a better way.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Merge requests
# <!-- Use merge requests for significant changes instead of pushing directly to `main` so that code can be discussed during development and a code review is possible when the branch is finished.  -->
# - Use merge requests for discussion and code reviews.
# - I only know what you are doing if you create an issue or a MR where I am mentioned/assigned.
# - Besides me, let each merge request be approved from at least one person who was not involved in the development of the feature branch (the author of the MR cannot approve but people who have added commits can).
# - You can also refer to me in the MR description or in the comment if you want feedback during a merge request for `main`.
# - You can leave the MR description empty if it refers to an issue that explains everything. GitLab will automatically refer to this issue.

# %% [markdown] slideshow={"slide_type": "slide"}
# - [This merge request](https://gitlab.lrz.de/fspanhel/dsc_gitlab_playground/-/merge_requests/1) illustrates how a merge request with a referenced issue should look like  
#
# <div>
# <img src="./figures/mr_form.png" alt="MR" width=900/>
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# - If you use a MR in your code review process, don't use git rebase after creating the MR.
# - As soon as you make the MR, other developers will be investigating your commits, which means that it’s a public branch. 
# - Re-writing its history will make it impossible for Git and your teammates to track any follow-up commits
# - However, before you perform the merge of the MR, you could discuss whether you rebase the feature branch on the main branch to tidy up. At this point, a rebase is fine if no further commits are done on the feature branch.
