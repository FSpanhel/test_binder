""" Usage:
    python3 lecture_notes/1_version_control/rebase.py arg,
    where arg is given in the section join commands.

    Use python3 lecture_notes/1_version_control/rebase.py reset
    before running python3 lecture_notes/1_version_control/rebase.py arg again!

    Note for students: This script just gets the job done and is not
    a blue print for good code.
    A class would be better but I have no time...
"""


import os
import sys
from typing import List

# %% individual commands
before_merge_ = {}
# commits on _target
before_merge_[
    "init_target"
] = """
# commits on _target
git checkout -b _target &&
echo "import os; print(os.getcwd())" > main.py &&
git add main.py && git commit -m "add main.py"
"""

# branch _messy_branch from _target and commit
before_merge_[
    "init_messy"
] = """
# branch _messy_branch from _target and commit
git checkout -b _messy_branch &&
echo "this is the frist line" > module_a.py &&
git add module_a.py && git commit -m "add module_a.py" &&
rm module_a.py &&
echo -e "this is the first line" > module_a.py &&
git add module_a.py && git commit -m "fix spelling error in module_a.py" &&
echo "this is the second line" >> module_a.py &&
git add module_a.py && git commit -m "add more details to module_a.py"
"""

# meanwhile on _target
before_merge_[
    "update_target"
] = """
# meanwhile on _target
git checkout _target &&
echo "import os; print(os.getcwd(), print(os.getlogin()))" >> main.py &&
git add main.py && git commit -m "update main.py"
"""

# merge the changes on _target to _messy_branch because you need them for your work
merge_target = """
# merge the changes on _target to _messy_branch
git checkout _messy_branch &&
git merge _target --no-edit
"""

# git rebase _messy_branch on _target so that ff-merge is possible
rebase_messy = """
# git rebase _messy_branch on _target so that ff-merge is possible
git checkout _messy_branch &&
git rebase _target &&
sleep 5
"""

# start interactive rebase
i_rebase_messy = """
# start interactive rebase
git checkout _messy_branch &&
git rebase -i _target
"""

# finish changes on _messy_branch and merge into _target
finish = """
# finish changes on _messy_branch and merge into _target
echo "this is the third line" >> module_a.py &&
git add module_a.py && git commit -m "consider update of main.py in module_a.py" &&
git checkout _target &&
git merge _messy_branch &&
git branch -d _messy_branch
"""

# finish changes on _messy_branch and merge into _target with explicit 3-way merge
finish_no_ff = """
# finish changes on _messy_branch and merge into _target with explicit 3-way merge
echo "this is the third line" >> module_a.py &&
git add module_a.py && git commit -m "consider update of main.py in module_a.py" &&
git checkout _target &&
git merge _messy_branch  --no-edit --no-ff
git branch -d _messy_branch
"""

# finish changes on _messy_branch and merge into _target
finish_with_squash = """
# finish changes on _messy_branch and merge into _target
echo "this is the third line" >> module_a.py &&
git add module_a.py && git commit -m "consider update of main.py in module_a.py" &&
git rebase -i _target &&
git checkout _target &&
git merge _messy_branch  --no-edit
git branch -d _messy_branch
"""

finish_with_squash_no_ff = """
# finish changes on _messy_branch and merge into _target
echo "this is the third line" >> module_a.py &&
git add module_a.py && git commit -m "consider update of main.py in module_a.py" &&
git rebase -i _target &&
git checkout _target &&
git merge _messy_branch  --no-edit --no-ff
git branch -d _messy_branch
"""

# clean_up
reset = """
git checkout main;
git branch -D _target;
git branch -D _messy_branch;
"""


# %% join commands
def join_commands(ls: List[str]) -> str:  # noqa
    return "sleep 2 &&\n".join(ls)


before_merge = join_commands(list(before_merge_.values()))
messy = join_commands([before_merge, merge_target, finish])
rebased = join_commands([before_merge, rebase_messy, finish])
rebased_no_ff = join_commands([before_merge, rebase_messy, finish_no_ff])
interactive_rebase_before_1st_merge = join_commands(
    [before_merge, i_rebase_messy, finish]
)
interactive_rebase_before_1st_merge_no_ff = join_commands(
    [before_merge, i_rebase_messy, finish_no_ff]
)
squash = join_commands([before_merge, i_rebase_messy, finish_with_squash])
squash_no_ff = join_commands([before_merge, i_rebase_messy, finish_with_squash_no_ff])

interactive_rebase = join_commands([before_merge, i_rebase_messy])
continue_after_interactive_rebase = join_commands([merge_target, finish])
continue_after_interactive_rebase_no_ff = join_commands([merge_target, finish_no_ff])


# %% run
def run(command: str):
    os.system("sleep 1")
    os.system(command)


# && main
if __name__ == "__main__":
    args = sys.argv[1:]
    for arg in args:
        run(eval(arg))
