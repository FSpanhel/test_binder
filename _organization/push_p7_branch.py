from dsc.shell import (
    checkout_branch_on_the_basis_of_the_initial_commit,
    list_files,
    run_cmd,
)

# %% setup


class IncludeFiles:
    # TODO: Put this into the dsc package and exclude it

    def __init__(self, exclude_pattern: list[str] | None = None):
        if exclude_pattern is None:
            dot_folders = ["^.dvc", "^.git", ".egg-info"]
            folders = [
                "^data",
                "_cache",
                "^_",
                "^docs",
            ]
            folders.extend(dot_folders)
            files = [
                "/_",
                "-checkpoint",
                "^.gitignore_hm"
            ]
            exclude_pattern = folders + files
        self.exclude_pattern = exclude_pattern

    def list(self):
        return list_files(
            exclude_pattern=self.exclude_pattern,
            exclude_files_unknown_to_git=True,
        )


class IncludeFilesForP7(IncludeFiles):
    """
    Returns the files that should be pushed to
    https://gitlab.p7s1.io/ent-bi-data-science/dsc_2022.
    """
    def __init__(self):
        super().__init__()

        general = [
            "lecture_notes/0_introduction"
        ]

        self.exclude_pattern.extend(general)


target_branch = "p7"
exists = False
source_branch = "main"


# %% Build command
# This is required because otherwise it may not be possible to checkout a branch
# Stashing might be an alternative


def assert_wd_clean():
    conditions = [
        "nothing to commit, working tree clean",
        'nothing added to commit but untracked files present (use "git add" to track)'
    ]
    if run_cmd("git status")[-1] not in conditions:
        raise Exception("Git working directory is not clean")


assert_wd_clean()

files = IncludeFilesForP7().list()
commands: list[str] = []
commands.append(
    checkout_branch_on_the_basis_of_the_initial_commit(target_branch, exists)
)
commands.append(f"git checkout {source_branch} -- {files}")
commands.append(
    f"git commit --no-verify -m \"Add the files of the '{source_branch}' branch\""
)
commands.append(f"git push -f p7 {target_branch}:main")
commands.append(f"git checkout {source_branch}")
commands.append(f"git branch -D {target_branch}")

command = " &&\n".join(commands)
command = command + "\n"

# %% Run command
run_cmd(f"{command}", shell=True)  # need shell=True because of &&
