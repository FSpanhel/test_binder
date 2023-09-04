from dsc.shell import (
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
                "_cache",  # ruff and mpy
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


class IncludeFilesForHM(IncludeFiles):
    def __init__(self, lecture_number: int):
        super().__init__()

        general = [
            "lecture_notes/3_code/debugging.ipynb",
            "lecture_notes/3_code/illustrate_debugging.py",
        ]

        lecture_specific = {
            0: [".*"],
            1: [
                "lecture_notes/",
                "src/dsc/introduction/",
                "src/dsc/setup_python_project/",
                "src/dsc/version_control/",
                # Add the two lines later after pre-commit has been introduced
                ".isort.cfg",
                ".pre-commit-config.yaml",
                # Provide this file to the students after jupytext has been introduced
                "jupytext.toml",
            ],
            2: [
                "lecture_notes/[1-9]",
                "src/dsc/setup_python_project/",
                "src/dsc/version_control/",
                "lecture_notes/0_introduction/2_exercise_solution.ipynb",
                # Add the two lines later after pre-commit has been introduced
                ".isort.cfg",
                ".pre-commit-config.yaml",
                # Provide this file to the students after jupytext has been introduced
                "jupytext.toml",
            ]
        }

        self.exclude_pattern.extend(general)
        if lecture_number in lecture_specific.keys():
            self.exclude_pattern.extend(lecture_specific[lecture_number])
        else:
            raise ValueError("Key not defined")


target_branch = "hm_2023"
exists = False
source_branch = "main"


class GitSyncer:
    """
    Integrates files from one branch into another one use a checkout of the
    files.

    This is useful if a branch should only contain a subset of files.
    """
    def __init__(self, target_branch: str, source_branch: str = "main"):
        self.target_branch = target_branch
        self.source_branch = source_branch
        self.commands: list[str] = []

    def create_target_branch_from_initial_commit(self) -> None:
        hash_of_initial_commit = run_cmd("git rev-list --max-parents=0 HEAD")[0]
        self.commands.append(
            f"git branch {self.target_branch} {hash_of_initial_commit}"
        )

    def stash(self) -> None:
        self.commands.append("git stash")

    def pop_stash(self) -> None:
        self.commands.append("git stash pop")

    def checkout_files_from_source_and_commit_to_target(
            self,
            files: list[str],
            commit_message: None | str = None
    ) -> None:
        self.commands.append("git stash")
        self.commands.append(f"git checkout {self.target_branch} || true")

        # Do an empty commit if files is empty
        if commit_message is None:
            commit_message = f"Add the files of the '{self.source_branch}' branch"
        if len(files) == 0:
            self.commands.append(
                f"git commit --no-verify --allow-empty '{commit_message}'")
        else:
            self.commands.append(
                f"git checkout {self.source_branch} -- {' '.join(files)}"
            )
            self.commands.append(
                f"git commit --no-verify -m '{commit_message}'"
            )

    def push_target_as_main_its_remote(self, remote: str) -> None:
        self.commands.append(f"git push -f {remote} {target_branch}:main")

    def checkout_source(self) -> None:
        self.commands.append(f"git checkout {self.source_branch}")

    def checkout_source_and_delete_target(self) -> None:
        self.commands.append(f"git checkout {self.source_branch}")
        self.commands.append(f"git branch -D {self.target_branch} || true")

    # TODO: This should be a property
    def _command(self) -> str:
        command = " &&\n".join(self.commands)
        command = command + "\n"
        return command

    def run(self):
        # Need shell=True because of &&
        return run_cmd(f"{self._command()}", shell=True)

    def clear_commands(self):
        self.commands = []


# %%
lecture = 0

git = GitSyncer(target_branch, source_branch)

commit_messages = {
    # 0: # not required because the initial commit is the initial commit on main
    1: 'Add general project files for the first lecture',
    2: "Add files for the lecture on 2023-10-15"
}

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

for lecture in [-1, 0, 1, 2]:
    git.clear_commands()

    if lecture == -1:
        git.checkout_source_and_delete_target()

    elif lecture == 0:
        git.create_target_branch_from_initial_commit()

    else:
        files = IncludeFilesForHM(lecture).list()
        git.checkout_files_from_source_and_commit_to_target(
            files=files,
            commit_message=commit_messages[lecture],
        )
        git.checkout_source()

    print(
        "\n>>>>>> Executing",
        git._command(),
        "\n".join(git.run()),
        sep="\n")
