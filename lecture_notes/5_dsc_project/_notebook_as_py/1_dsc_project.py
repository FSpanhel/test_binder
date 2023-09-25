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
#     display_name: Python [conda env:dsc_dev] *
#     language: python
#     name: conda-env-dsc_dev-py
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# # The data science challenge project

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Information about the GitLab project

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Branches and permissons
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
# ### The Git workflow
# [#TODO Needs update]
# - For data science projects which focus on analyses and experimentation, I think that the a simple feature branch workflow is adequate.
# - The Git workflow for your project is a simple feature branch workflow with an additional branch to which you submit your code for grading.
#
#     1. In general, you create a feature branch from the (up-to-date) branch `main`.
#     1. When a feature branch is completed, create a MR with the target being `main` and **assign @Fabian Spanhel as reviewer** (!).
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
# ### Merge requests
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
# ## Working with GitLab
# ### Branches
# - First of all, create a milestone which can then be divided into several issues.
# - In general, create an issue for each significant feature. Then create the branch and the MR.
#     - You can shorten the name of the feature branch as long as it starts with the issue number.
#     - Use [kebab case](https://en.wikipedia.org/wiki/Letter_case#Kebab_case) for formatting branch names. 
# - Ideally, one person should work on one branch.
# - Rather use short-lived branches which focus on one feature than developing several features on one branch.
#     - Reduces the likelihood of merge conflicts.
#     - I can give feedback more frequently. 

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Merge requests
# <!-- Use merge requests for significant changes instead of pushing directly to `main` so that code can be discussed during development and a code review is possible when the branch is finished.  -->
# - Use merge requests for discussion and code reviews.
# - **I only know what you are doing if you create an issue or a MR where I am mentioned/assigned**.
# - Besides me, let each merge request be approved from at least one person who was not involved in the development of the feature branch (the author of the MR cannot approve but people who have added commits can).
# - You can also refer to me in the MR description or in the comment if you want feedback during a merge request for `main`.
# - You can leave the MR description empty if it refers to an issue that explains everything. GitLab will automatically refer to this issue.

# %% [markdown] slideshow={"slide_type": "slide"}
# [#TODO update link]
# - [This merge request](https://gitlab.lrz.de/fspanhel/dsc_gitlab_playground/-/merge_requests/1) illustrates how a merge request with a referenced issue should look like  
#
# <div>
# <img src="./figures/mr_form.png" alt="MR" width=900/>
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# - If you use a MR in your code review process, don't use git rebase after creating the MR unless you have discussed this with your colleagues.
# - As soon as you make the MR, other developers will be investigating your commits, which means that it’s a public branch. 
# - Re-writing its history will make it impossible for Git and your teammates to track any follow-up commits
# - However, before you perform the merge of the MR, you could discuss whether you rebase the feature branch on the main branch to tidy up. At this point, a rebase is fine if no further commits are done on the feature branch.
