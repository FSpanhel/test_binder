import logging
import os
import sys

from dsc.notebook import git_root
from dsc.shell import RunCMDError, list_files, run_cmd

# source_branch = "13-push-first-version-of-the-course"
source_branch = "main"
target_branch = "hm_2023_dev"

log_file = os.path.join(git_root(), "_organization", f"{target_branch}.log")
logging.basicConfig(filename=log_file, force=True, level=logging.INFO)
logger = logging.getLogger(__name__)

# %% setup

if False:
    list_files(
        exclude_pattern=[
            # r"^(?:_[\w/]*\/)*_[\w/]*$"
            r"^_(?!_)",
            r"/_(?!_)",
            r"src/dsc/[a-z]",
            r"data/(?!.+\.dvc|\.gitignore)",
        ],
        exclude_files_unknown_to_git=True,
    )


class IncludeFiles:
    # TODO: Put this into the dsc package and exclude it

    def __init__(self, exclude_pattern: list[str] | None = None):
        if exclude_pattern is None:
            dot_folders = [
                # "^.dvc", Need this? I think so
                # "^.git", Unknown to Git: Need this? Hm I think this is ignored by Git in any case, so I cannot checkout this  # noqa
                # ".egg-info"  # Unknown to Git: Should not be versioned with Git
            ]
            folders = [
                # So that data/dvc.db.dvc and .gitignore is included
                r"data/(?!.+\.dvc|\.gitignore)",
                "docs",  # Because this should be build later
            ]
            folders.extend(dot_folders)
            files = [
                # files/folders starting with _
                # (?!_) next character should not be another underscore, because
                # we have files like __init__.py
                r"^_(?!_)",
                # files/folders starting with _ in a subdirectory
                r"/_(?!_)",
            ]
            exclude_pattern = folders + files
        self.exclude_pattern = exclude_pattern

    def list(self):
        return list_files(
            folder=".",
            exclude_pattern=self.exclude_pattern,
            exclude_files_unknown_to_git=True,
        )


class IncludeFilesForHM(IncludeFiles):
    def __init__(self, commit_number: int):
        super().__init__()

        general = [
            "lecture_notes/3_code/debugging.ipynb",
            "lecture_notes/3_code/illustrate_debugging.py",
        ]

        commit_specific = {
            0: [".*"],
            1: [
                "lecture_notes",
                "src/dsc/[a-z]+",  # so that __init__ exists
                "src/dsc/__main__",
                "docs",
                "install_mambaforge.sh",
                # Add the two lines later after pre-commit has been introduced
                ".isort.cfg",
                ".pre-commit-config.yaml",
                # Provide this file to the students after jupytext has been introduced
                "jupytext.toml",
            ],
            # lecture_notes/0
            2: [
                "lecture_notes/[1-9]",
                "src/dsc/setup_python_project",
                "src/dsc/version_control",
                "lecture_notes/0_introduction/2_exercise_solution.ipynb",
                # Add the two lines later after pre-commit has been introduced
                ".isort.cfg",
                ".pre-commit-config.yaml",
                # Provide this file to the students after jupytext has been introduced
                "jupytext.toml",
            ],
            # Solution to lecture_notes/0
            3: [
                "lecture_notes/[1-9]",
                "src/dsc/version_control",
                "src/dsc/setup_python_project",
                # Add the two lines later after pre-commit has been introduced
                ".isort.cfg",
                ".pre-commit-config.yaml",
                # Provide this file to the students after jupytext has been introduced
                "jupytext.toml",
            ],
            # lecture_notes/1
            4: [
                "lecture_notes/[2-9]",
                "src/dsc/version_control",
                "src/dsc/setup_python_project",
                # Add the two lines later after pre-commit has been introduced
                ".isort.cfg",
                ".pre-commit-config.yaml",
                # Provide this file to the students after jupytext has been introduced
                "jupytext.toml",
            ],
            # lecture_notes/2
            5: [
                "lecture_notes/[3-9]",
                "lecture_notes/2_version_control/3_exercise_solution.ipynb",
                "src/dsc/setup_python_project",
                # Add the two lines later after pre-commit has been introduced
                ".isort.cfg",
                ".pre-commit-config.yaml",
                # Provide this file to the students after jupytext has been introduced
                "jupytext.toml",
            ],
            # Solution to lecture_notes/2
            6: [
                "lecture_notes/[3-9]",
                "src/dsc/setup_python_project",
                # Add the two lines later after pre-commit has been introduced
                ".isort.cfg",
                ".pre-commit-config.yaml",
            ],
        }

        self.exclude_pattern.extend(general)
        if commit_number in commit_specific.keys():
            self.exclude_pattern.extend(commit_specific[commit_number])
        else:
            raise ValueError("Key not defined")


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

    def _checkout_files_from_source_and_commit_to_target(
        self, files: list[str], commit_message: None | str = None
    ) -> None:
        # self.commands.append("git stash")
        self.commands.append(f"git checkout {self.target_branch} || true")

        # Do an empty commit if files is empty
        if commit_message is None:
            commit_message = f"Add the files of the '{self.source_branch}' branch"
        if len(files) == 0:
            self.commands.append(
                f"git commit --no-verify --allow-empty '{commit_message}'"
            )
        else:
            self.commands.append(
                f"git checkout {self.source_branch} -- {' '.join(files)}"
            )
            self.commands.append(f"git commit --no-verify -m '{commit_message}'")

    def checkout_to_target(self):
        self.commands.append(f"git checkout {self.target_branch} || true")

    def checkout_files_from_source(
        self,
        files: list[str],
    ) -> None:
        self.commands.append(f"git checkout {self.source_branch} -- {' '.join(files)}")

    def commit_to_target(self, commit_message: None | str = None):
        # Do an empty commit if files is empty
        if commit_message is None:
            commit_message = f"Add the files of the '{self.source_branch}' branch"
        self.commands.append(f"git commit --no-verify -m '{commit_message}'")

    def push_target_as_main_its_remote(self, remote: str) -> None:
        self.commands.append(f"git push -f {remote} {target_branch}:main")

    def checkout_source(self) -> None:
        self.commands.append(f"git checkout {self.source_branch} || true")

    def checkout_source_and_delete_target(self) -> None:
        self.commands.append(f"git checkout {self.source_branch}")
        self.commands.append(f"git branch -D {self.target_branch} || true")

    # TODO: This should be a property
    def _command(self) -> str:
        command = " &&\n".join(self.commands)
        command = command  # + "\n"
        return command

    def run(self):
        # Need shell=True because of &&
        return run_cmd(f"{self._command()}", shell=True)

    def clear_commands(self):
        self.commands = []

    def build_doc(self):
        self.commands.append(
            "pdoc -d google -o docs --footer-text 'Data Science Challenge' src/dsc"
        )
        self.commands.append("git add docs")


# %%
if len(sys.argv) == 1:
    commit = 1  # TODO: should be renamed to commit
else:
    commit = int(sys.argv[1])

git = GitSyncer(target_branch, source_branch)

commit_messages = {
    # 0: # not required because the initial commit is the initial commit on main
    1: "Add general project files",
    2: "Add files for the lecture on 2023-10-06",
    3: "Add lecture_notes/0_introduction/2_exercise_solution.ipynb",
    4: "Add lecture_notes/1_collaboration_and_project_management",
    5: "Add lecture_notes/2_version_control",
    6: "Add lecture_notes/2_version_control/3_exercise_solution.ipynb",
}


def assert_wd_clean():
    conditions = [
        "nothing to commit, working tree clean",
        'nothing added to commit but untracked files present (use "git add" to track)',
    ]
    if run_cmd("git status")[-1] not in conditions:
        raise Exception("Git working directory is not clean")


# for lecture in [-1, 0, 1, 2]:


def create_commit(git: GitSyncer, commit: int):
    if commit == -1:
        git.checkout_source_and_delete_target()

    elif commit == 0:
        git.create_target_branch_from_initial_commit()

    else:
        files = IncludeFilesForHM(commit).list()
        git.checkout_to_target()
        git.checkout_files_from_source(files)
        git.build_doc()
        git.commit_to_target(commit_messages[commit])
        git.checkout_source()

    newline = "\n"

    print(f"Logging to {log_file}")

    logging.info(f">>>>>> Executing create_commit for commit = {commit}")
    logging.info(f"The git command that will be run is:{newline}{git._command()}")
    try:
        logging.info(f"The output of the git command is: {newline.join(git.run())}")
    except RunCMDError as e:
        logging.error(str(e), exc_info=1)
        raise e


if __name__ == "__main__":
    # This is required because otherwise it may not be possible to checkout a branch
    # Stashing might be an alternative
    assert_wd_clean()

    conda_env = os.environ["CONDA_PREFIX"].rsplit("/", -1)[-1]
    if conda_env != "dsc_dev":
        raise Exception(
            "Env must be dsc_dev so that pdoc is available but is {conda_env}"
        )

    create_commit(git, commit)
