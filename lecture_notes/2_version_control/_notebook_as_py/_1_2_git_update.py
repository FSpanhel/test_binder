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
#     display_name: Python [conda env:dsc_2022] *
#     language: python
#     name: conda-env-dsc_2022-py
# ---

# %% [markdown]
# This notebook contains content that hasn't been integrated into 1_git.ipynb yet

# %% [markdown]
# # Squash commit

# %% [markdown]
# - https://www.google.de/search?q=git+merge+squash&source=hp&ei=26t_Y53QOcSX8gLFwoaoBg&iflsig=AJiK0e8AAAAAY3-56_TKIJBnr79Xm5te0WsrmSvXvEWK&ved=0ahUKEwjdqfPgrcf7AhXEi1wKHUWhAWUQ4dUDCAo&uact=5&oq=git+merge+squash&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46EQguEIAEELEDEIMBEMcBENEDOgsIABCABBCxAxCDAToICC4QsQMQgwE6CwguEIAEEMcBEK8BOggILhCABBCxAzoOCC4QgAQQsQMQgwEQ1AI6BQguEIAEOggIABCABBCxAzoOCC4QgAQQsQMQxwEQrwE6BwgAEIAEEBM6CQgAEIAEEAoQEzoICAAQFhAeEBM6CggAEBYQHhAKEBNQAFjiG2DTHmgEcAB4AIABiwKIAeMRkgEGNS4xMi4xmAEAoAEB&sclient=gws-wiz
# - https://stackoverflow.com/questions/5308816/how-can-i-merge-multiple-commits-onto-another-branch-as-a-single-squashed-commit
# - https://levelup.gitconnected.com/do-you-know-how-to-use-git-merge-squash-7d96c1191fd5
# - https://blog.mergify.com/what-is-the-difference-between-a-merge-commit-a-squash/
# - https://stackoverflow.com/questions/9599411/differences-between-git-merge-squash-and-no-commit?noredirect=1&lq=1
# - Note that GitLab [does the following when using a squash merge](https://docs.gitlab.com/ee/user/project/merge_requests/methods/)
# ```
# git checkout `git merge-base <source-branch> <target-branch>`
# git merge --squash <source-branch>
# SOURCE_SHA=`git rev-parse HEAD`
# git checkout <target-branch>
# git merge --no-ff $SOURCE_SHA
# ```
# So this is different from ```git merge --squash```?

# %% [markdown]
#
