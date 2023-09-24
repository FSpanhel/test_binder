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
# # Working on a collaborative project with Git and a Git management application 

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Introduction
# - [Git](https://git-scm.com/) is commonly introduced as a tool to version source code.
# - However, due to its branching capatibilites Git is also a tool that helps to develop code.
# - **Together with Git management platforms like [GitHub](https://github.com) or [GitLab](https://gitlab.com/gitlab-org/gitlab), Git becomes the predominant choice for (collaborative) code development.**
# - As a result, our initial focus will be on Git in conjunction with a Git management platform, with a more detailed discussion of plain Git to follow later on.

# %% [markdown] slideshow={"slide_type": "slide"}
# - A **Git management application** is a hosting service for software development and Git version control.
# - Popular examples are 
#     - [GitHub](https://github.com): The largest source code host. Best for public repos. Owned by Microsoft.
#     - [GitLab](https://gitlab.com/gitlab-org/gitlab): Best for private repos.
#     - [BitBucket](https://bitbucket.org/product): From Atlassian with Jira integration. Best for private repos.
# - A Git management application **hosts remote Git repos** that you can use to perform pull and push operations.
# - Moreover, it **simplifies the collaboration using Git** and improves code developement by providing
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
# - In the following, you can use the [playground](https://gitlab.lrz.de/dsc/2023/playground) to get to know Gitlab and how it can be used for your project.

# %% [markdown] slideshow={"slide_type": "slide"}
# # [Issues](https://docs.gitlab.com/ee/user/project/issues/ )
# - Each fundamental change to the code should start with an issue that describes the task or feature.
# - By creating an issue you 
#     - Inform your team about what should be discussed or be done.
#     - Avoid that feature branches get too big because you have to think about the scope when writing the issue.
#     - Assign responsibilities. 
#     - Improve your workflow by
#         - Making use of the issue board to easily see what should be done and has be done. 
#         - Refering to it when making commit messages or merge/pull requests. 
# - Every issue should be addressed. You can also close them without modifying your code. In this case, the issue should contain information why it is not addressed (!)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Creating an issue
# - To create an issue click on `Issues` on the left sidebar of your Gitlab project and use the resulting site to create a new issue.
# - Click [here](https://gitlab.lrz.de/dsc/2023/playground/-/issues/1) to see an issue of the [playground](https://gitlab.lrz.de/dsc/2023/playground).
# - The issue title should describe the outcome of the issue. For instance, prefer "Cross validation should consider more than one fold" to "Cross validation considers only one fold".
# - Create a [label](https://docs.gitlab.com/ee/user/project/labels.html) for this issue, e.g., to create a corresponding column for the issue board.
# - When it is clear who should work on the issue, assign the issue to this person.
# - Create a branch for the issue from the main branch to work on it. 
# - For each issue there should be only one branch. But there can be one branch for several issues.
# - You can also use tasks to break the issue down into smaller parts or use a milestone to group several issues.
# - You can als create a pull/merge request from an issue.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Exercise: Create your first issue
# 1. Create an issue in the [playground](https://gitlab.lrz.de/dsc/2023/playground/-/issues/1) with the title `[name]: First task `, where [name] is your full name e.g., `Fabian Spanhel: First task`.
# 1. Insert the content of [first_task.md](first_task.md) as issue description.
# 1. Address the first point mentioned in the issue description.
# 1. Please check off an item if you have completed it.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## [Issue board](https://docs.gitlab.com/ee/user/project/issue_board.html)
# - With the issue board you can plan, organize, and visualize your workflow and manage your project.
# - It shows the issues your team is working on, the status of each issue and who the issue is assigned to.
# - You can use it as a [SCRUM](https://en.wikipedia.org/wiki/Scrum_(software_development) or [KANBAN](https://en.wikipedia.org/wiki/Kanban_(development) board. 
# - Regarding Data Science projects I recommend to use it as a KANBAN board.
# - You can create a new [list](https://docs.gitlab.com/ee/user/project/issue_board.html#issue-board-terminology) (a column on the issue board that displays issues matching certain attribute) by referrring to a [label](https://docs.gitlab.com/ee/user/project/labels.html)
# - You can also use multiple issue boards (e.g., one for data processing, one for modeling...).
# - Click [here](https://www.youtube.com/watch?v=vjccjHI7aGI&feature=youtu.be) to watch a video presentation of the issue board.
# - The issue board of the playground can be found [here](https://gitlab.lrz.de/dsc/2023/playground/-/boards)

# %% slideshow={"slide_type": "slide"}
embed_website("https://docs.gitlab.com/ee/user/project/issue_board.html")

# %% [markdown] slideshow={"slide_type": "slide"}
# # [Pull/merge requests](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
# - A **pull request (PR)** or **merge request (MR)** is the same concept. 
#     - GitHub and Bitbucket call this process a pull request because the first action is to pull the feature branch.
#     - GitLab call this process a merge request because the final action is to merge the feature branch.
# - A MR is a website to **discuss** and **review** code changes done in a feature branch and to **merge** it into another branch.
#     - Open a MR when you would like to **discuss** the work in progress or have **completed** your work on the feature branch.
#     - After discussion and review, the code of the branch of the MR can be **merged** into a target branch.
# - The underlying process of a MR is designed to **maintain code quality**, **prevent errors**, and ensure that the **changes align with the repo's goals and standards**.
# - Note that your feature branch is considered to be public when it is attached to a corresponding MR, so **be careful with rebasing the branch of a MR**

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Creating a MR
# - It's best to create a MR with corresponding branch directly from an [issue](https://gitlab.lrz.de/fspanhel/dsc_gitlab_playground/-/issues/1).
#     - It's fine if several issues can be resolved by a MR but there shouldn't be several MRs that resolve one issue.
# - To see the resulting MR click [here](https://gitlab.lrz.de/dsc/2023/playground/-/merge_requests/2).
# - When you create a MR, include in its description at least one of the following points
#     - A summary of the changes and what problem they solve.
#     - References to the corresponding issues.
#         - Gitab will then automatically refer to the MR in the reference issue.
#         - If you use [appropriate keywords](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically), the referenced issues will automatically be closed when the branch of the MR is merged to the default branch.
# - If you would like to have feedback or need help
#     - Start the title of the MR with "Draft: " to signal this and to prevent an unintended merge.
#     - Add general comments below the MR description or on specific lines of code, and alert persons by mentioning them using the "@" symbol followed by their alias, e.g. `@fspanhel`.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Exercise: Create a feature branch and the corresponding MR
# - Consider the issue in the [playground](https://gitlab.lrz.de/dsc/2023/playground/-/issues/1) with the title `[name]: First task`, where [name] is your full name, e.g., "Fabian Spanhel".
# - Address the second and third point.
# - Please check off an item if you have completed it.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Working on a MR
# - For simple commits that only involve one text file, you can use GitLab to edit the source code of the remote feature-branch.
# - However, in general, you edit the source code on your local copy of the remote feature-branch.
# -  In order to get this local copy
#     1. Run `git fetch` in your terminal.
#     1. Checkout the branch by running `git checkout feature-branch` in your terminal.
#     1. You can now commit changes to your local feature-branch.
# - Push the changes to the remote using `git push -u origin feature-branch`.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Exercise: Work on your MR
# - Consider the issue in the [playground](https://gitlab.lrz.de/dsc/2023/playground/-/issues/1) with the title `[name]: First task`, where [name] is your full name, e.g., "Fabian Spanhel".
# - Address the points 4 to 11.
# - Please check off an item if you have completed it.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## [Discussing and reviewing](https://gitlab.lrz.de/help/user/project/merge_requests/reviews/index.md#checkout-merge-requests-locally-through-the-head-ref)
# - You can use comments and threads below the MR for a general discussion.
# - Resolve a thread when the discussion about it is finished.
# - If you want to point something out you can add comments directly on specific lines of changed files or start an review which bundles comments
#     - Note that the comments are not viewable by others if the review is not finished (!).
# - If you want a review for this MR, select a reviewer on the right sidebar who can approve and merge the MR.
# - Conversely, reviewers can comment on the whole MR or add comments to specific lines to ask questions or provide suggestions.
#
# - Note: If you are an reviewer and want to check whether the code of the MR is running you can fetch and then checkout the corresponding feature branch, e.g., `git fetch && git checkout feature-branch`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Updating
# - If a discussion or review reveals shortcomings, anyone can commit and push a fix. However, the person to do this is isually the creator of the MR.
# - If new commits are added to the branch of an open MR, the MR is updated accordingly. 
# - If the merged request has been closed, updates on the branch will not be considered in the merge request.
# - New commits or other updates in the MR (such as comments) are displayed at the bottom of the MR overview in the activity section.
# - Besides adding a commit directly with Git, you can also use comments in the browser user interface to make direct [suggestions](https://docs.gitlab.com/ee/user/project/merge_requests/reviews/suggestions.html).
#     - This is especially useful for small commits, e.g., typos, or when you are not the creator of the MR.
# - When you resolve one comment with a commit, you should refer to the comment link in the body of the commit message.
# - If you resolve a comment with a commit you should mention the corresponding commit hash, e.g, "Resolved by [commit hash]".

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Approving
# - The assigned reviewers can approve the MR.
# - Depending on the settings, approval might be required so that the merge of the MR can be performed.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Exercise: Discussion and reviewing of the MR
# - Consider the issue in the [playground](https://gitlab.lrz.de/dsc/2023/playground/-/issues/1) with the title `[name]: First task`, where [name] is your full name, e.g., "Fabian Spanhel".
# - Address the points 12 to 15.
# - Please check off an item if you have completed it.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Merging
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
# ### Exercise: Merge the MR
# - Consider the issue in the [playground](https://gitlab.lrz.de/dsc/2023/playground/-/issues/1) with the title `First task of [insert name]`, e.g., `First task of Fabian Spanhel`.
# - Address the remaining points.
# - Please check off an item if you have completed it.

# %% [markdown] slideshow={"slide_type": "slide"}
# Let's have a look at the [issue board](https://gitlab.lrz.de/dsc/2023/playground/-/boards) again.
