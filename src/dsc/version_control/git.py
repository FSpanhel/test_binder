"""
Provides a very basic Git API that is used in `lecture_notes/2_version_control`.
The main program can be used to reproduce the corresponding commits in
`lecture_notes/2_version_control/1_git.ipynb`

Usage:
- `python3 -m dsc.version_control.git` reproduces the commits in section 2.4
    before the _target branch is merged into _messy_branch for the first time
- `python3 -m dsc.version_control.git reset` undos all commits done by this program
- `python3 -m dsc.version_control.git cmd1 cmd2`, where cmd1 and cmd2 are
    git commands that integrate one branch into another, i.e., merge or rebase
    - `python3 -m dsc.version_control.git merge merge`  reproduces the commits in
        section 2.4
    - `python3 -m dsc.version_control.git rebase merge`  uses rebase for the first
        integration
    - `python3 -m dsc.version_control.git rebase "merge --no-ff"`  uses rebase
    for the first integration and then an explicit 3-way merge
    - `python3 -m dsc.version_control.git "rebase -i" "merge"`
    - `python3 -m dsc.version_control.git "rebase -i" "merge --no-ff"`

Note for students:
The Git class and the main program just get the job done and
can be improved...but https://youtu.be/zGxwbhkDjZM?t=25.
"""
from __future__ import annotations

import os
import sys
from typing import List

newline = "\n"


class Git:
    """
    Provides a simple Python API for Git that is used in
    lecture_notes/1_version_control.

    Note: The documentation of attributes and methods is not done yet.
    """

    def __init__(self):
        self.branch = None
        self.branches = []
        self.commands = []
        self.commit_messages = []

    def _get_branches_from_file(self) -> List[str]:
        if os.path.exists("_branches.txt"):
            with open("_branches.txt", "r") as file:
                branches = file.read().splitlines()
        else:
            branches = []
        return branches

    def _add_branch_to_file(self, branch: str) -> None:
        branches = self._get_branches_from_file()
        if branch not in branches:
            with open("_branches.txt", "a") as file:
                file.write(f"{branch}{newline}")

    def _add_branch_to_self(self, branch: str) -> None:
        if branch not in self.branches:
            self.branches.append(branch)

    def _add_new_branch(self, branch: str) -> None:
        self._add_branch_to_self(branch)
        self._add_branch_to_file(branch)

    def _clear_branches(self) -> None:
        self.branches = []
        if os.path.exists("_branches.txt"):
            os.remove("_branches.txt")

    def commit(
        self, path2file: str, content: str, msg: str, append: bool = False
    ) -> Git:
        if not append:
            if os.path.exists(path2file):
                create = f"rm {path2file} && echo '{content}' > {path2file}"
            else:
                create = f"echo '{content}' > {path2file}"
        else:
            create = f"echo '{content}' >> {path2file}"
        self.commands.append(create)
        self.commands.append(f"git add {path2file}")
        self.commands.append(f"git commit --no-verify -m '{msg} {path2file}'")
        self.commit_messages.append(f"on branch {self.branch}: {msg}")
        return self

    def checkout(self, branch: str) -> Git:
        branches = self._get_branches_from_file()
        if branch not in branches:
            command = f"git checkout -b {branch}"
            self._add_new_branch(branch)
        else:
            command = f"git checkout {branch}"
        self.branch = branch
        self.commands.append(command)
        return self

    def integrate(self, target: str, how: str) -> Git:
        command = f"git {how} {target}"
        self.commands.append(command)
        return self

    def delete(self, branch: str) -> Git:
        # Note: branch is not deleted from _branches.txt...
        command = f"git branch -D {branch}"
        self.commands.append(command)
        return self

    def reset(self) -> Git:
        """Checkout to main and delete `branches`."""
        self.commands.append("git checkout main")
        branches = self._get_branches_from_file()
        for branch in branches:
            self.commands.append(f"git branch -f {branch} && git branch -D {branch}")
        self._clear_branches()
        return self

    def execute(self, dry_run: bool = False) -> Git:
        if dry_run:
            print(self.commands)
        else:
            os.system(f" &&{newline}".join(self.commands))
        return self


if __name__ == "__main__":
    args = sys.argv[1:]
    git = Git().reset()

    if len(args) == 1 and args[0] == "reset":
        pass
    else:
        # setup
        (
            git.checkout("_target")  # setup _target
            .commit("main.py", "print(1)", "add")
            .checkout("_messy_branch")  # setup _messy
            .commit("module_a.py", 'print("this is the frist line")', "add")
            .commit(
                "module_a.py",
                'print("this is the first line")',
                "fix spelling error in",
            )
            .commit(
                "module_a.py",
                'print("this is the second line")',
                "add more details to",
                append=True,
            )
            .checkout("_target")  # meanwhile on _target
            .commit("main.py", "print(2)", "update", append=True)
            .checkout("_messy_branch")
        )

        if len(args) == 0:
            pass

        elif len(args) in [1, 2]:
            # integrating changes from _target to _messy_branch
            git.integrate("_target", args[0])

            # finish
            if len(args) == 2:
                (
                    git.commit(
                        "module_a.py",
                        'print("this is the third line")',
                        "consider update of main.py in",
                        append=True,
                    ).checkout("_target")
                )

                git.integrate("_messy_branch", args[1])
                git.delete("_messy_branch")

        else:
            raise ValueError("At most two arguments are allowed")

    git.execute()
