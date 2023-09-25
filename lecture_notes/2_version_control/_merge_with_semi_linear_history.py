"""
This should illustrate
https://gitlab.lrz.de/help/user/project/merge_requests/methods/index.md#merge-commit

This file might be unfinished...
"""
from dsc.version_control.git import Git

# -- merge without rebase
git = Git()
git.checkout("_main")
git.checkout("_feature").commit("f1.py", "1", "add")
git.checkout("_main").commit("m1.py", "1", "add")
git.integrate("_feature", "merge  --no-edit --log -m 'Default merge'")
# .execute()


# -- merge with rebase and no-ff = merge with semi-linear history, see This should illustrate https://gitlab.lrz.de/help/user/project/merge_requests/methods/index.md#merge-commit  # noqa
# git.commands = []
git.checkout("_main")
git.checkout("_feature").commit("f2.py", "2", "add")
git.checkout("_main").commit("m2.py", "2", "add")
git.checkout("_feature").integrate("_main", "rebase")
git.checkout("_main").integrate(
    "_feature", "merge --no-ff --no-edit --log -m 'Merge with semi linear history'"
)
# .execute()

# -- merge with rebase and ff
# git.commands = []
git.checkout("_main")
git.checkout("_feature").commit("f3.py", "3", "add")
git.checkout("_main").commit("m3.py", "3", "add")
git.checkout("_feature").integrate("_main", "rebase")
git.checkout("_main").integrate("_feature", "merge --log --no-edit")

git.execute()


# reset
Git().reset().execute()
