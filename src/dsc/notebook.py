"""
Contains utility functions that are used for all lectures
like embeding webpages into a Jupyter notebook.
If run as a script, the
[nb extensions](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions)
are configured according to `.jupyter/nbconfig`. In particular, since the sidebar of
toc2 does not work anymore in recent versions, it is disabled and the floating
toc window is used to imitate it.
"""  # noqa


import logging
import os

from IPython.display import IFrame  # type: ignore

from dsc.shell import RunCMDError, run_cmd

markdown = False
"""The default value of *markdown* for `embed_website`."""
default_folder = "."
"""The default value of *folder* for `git_root`."""


def embed_website(
    url: str, width: int = 900, height: int = 500, markdown: bool = markdown
) -> IFrame:
    """
    Embeds a website into a Jupyter notebook code cell with given *width* and
    *height*.

    If *markdown* is True sets the figure height to 0.
    """
    if markdown:
        height = 0
    return IFrame(url, width, height)


def git_root(folder: str = default_folder) -> str:
    """
    Returns the absolute path of the Git repo root or the Git submodule.

    Args:
        folder: The path of a folder of a Git repo. Defaults to `default_folder`.

    Raises:
        `dsc.shell.RunCMDError`: If `folder` is not within a Git repo.

    Note:
        Displays the root directory of the submodule and not the parent
        repo if folder is within a Git submodule.

    Returns:
        The absolute path of the Git repo root.

    Example:
        ```python
        import traceback
        from ds.shell import RunCMDError
        from ds.inspect import git_root

        git_root()  # e.g., '/home/spa0001f/git_repos/teach/dsc'

        # Not within a Git repo (assuming /home is not a Git repo)
        try:
            git_root(folder="/home")
        except RunCMDError:
            traceback.print_exc()
        ```
    """
    try:
        return run_cmd("git rev-parse --show-toplevel", folder, False)[0]
    except RunCMDError as e:
        raise Exception(f"CWD = {os.getcwd()}") from e


def set_wd() -> None:
    """
    Sets the working directory of the notebook to the root of the Git repo.
    """
    project_root = git_root()
    if os.getcwd() != project_root:
        os.chdir(project_root)


if __name__ == "__main__":
    # Set .jupyter as JUPYTER_CONFIG_DIR so that .jupyter/nbconfig/notebook.json
    # is considered by
    # https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions

    logging.basicConfig(level=logging.INFO, force=True)
    logger = logging.getLogger(__name__)

    config_dir = f"{git_root()}/.jupyter"

    logger.info(f"Setting JUPYTER_CONFIG_DIR={config_dir}")

    # If the OS is unix-based, we could also use
    # https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html#macos-and-linux  # noqa
    # for the next step
    run_cmd(f"conda env config vars set -n dsc JUPYTER_CONFIG_DIR={config_dir}")

    # Need to reactivate the environment
    env_path = run_cmd("echo $CONDA_PREFIX", shell=True)[0]
    if os.path.basename(env_path) == "dsc":
        run_cmd("mamba deactivate && mamba activate dsc")
