from dsc.shell import (
    checkout_branch_on_the_basis_of_the_initial_commit,
    list_files,
    run_cmd,
)


def get_files_for_p7():
    """
    Returns the files that should be pushed to
    https://gitlab.p7s1.io/ent-bi-data-science/dsc_2022.
    """
    return " ".join(
        list_files(
            ".",
            exclude_folder_pattern,
            exclude_file_pattern,
            exclude_files_unknown_to_git=True,
        )
    )


dot_folders = ["^.dvc", "^.git", ".egg-info"]

exclude_folder_pattern = [
    "^data",
    "_cache",  # ruff and mypy
    "^_",
    "/_",
    "^docs",
]

exclude_folder_pattern.extend(dot_folders)
exclude_folder_pattern.extend(["lecture_notes/0_introduction"])

exclude_file_pattern = [
    "^_",
    "-checkpoint",
    ".gitignore_hm",
]


target_branch = "p7"
exists = False
source_branch = "main"

# %% Build command
commands: list[str] = []
commands.append(
    checkout_branch_on_the_basis_of_the_initial_commit(target_branch, exists)
)
commands.append(f"git checkout {source_branch} -- {get_files_for_p7()}")
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
