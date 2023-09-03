import os
import re

# import shutil
import sys
from os.path import join
from shutil import copyfile, copytree, ignore_patterns
from typing import List, Optional, Tuple


def copy_folder(
    source: str, destination: str, ignore: Optional[List[str]] = None
) -> None:
    if ignore is None:
        ignore = []
    if not os.path.exists(source):
        os.mkdir(source)
    copytree(
        source,
        destination,
        ignore=ignore_patterns(*ignore),
        dirs_exist_ok=True,
    )


def re_sub(folder, subs: List[Tuple[str, str]]) -> None:
    for file in os.listdir(folder):
        path = join(folder, file)
        if os.path.isfile(path):
            with open(path, "r") as _file:
                data = _file.read()
                for sub in subs:
                    data = re.sub(sub[0], sub[1], data)
            with open(path, "w") as _file:
                _file.write(data)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        destination_root = "../pyscaffold_test"
    elif len(sys.argv) == 2:
        destination_root = sys.argv[1]
    else:
        raise Exception("Must provide at most one argument")

    package_source = "src/dsc/setup_python_project/pyscaffold_test"
    package_destination = join(destination_root, "src/pyscaffold_test_fs")

    # copy data base
    if not os.path.exists(join(destination_root, "data/raw/dsc.db")):
        copyfile("data/dsc.db", join(destination_root, "data/raw/dsc.db"))

    # -- copy package
    copy_folder(package_source, package_destination, ["__pycache__", "__init__.py"])

    # -- copy notebooks
    notebooks_source = "lecture_notes/2_setup_python_project/code_structure"
    notebooks_destination = join(destination_root, "notebooks")
    copy_folder(
        notebooks_source,
        notebooks_destination,
        ["__pycache__", ".ipynb_checkpoints", "notebook_as_py"],
    )

    # -- rename notebooks and companion file
    possible_notebooks = os.listdir(notebooks_destination)
    for name in possible_notebooks:
        if name.endswith(".ipynb"):  # rename 1_notebook.ipynb to 1_fs_notebook.ipynb
            new_name = re.sub(r"(\d)(.*)", r"\1_fs\2", name)  # fmt: skip
        elif name == "companion_module.py":
            new_name = f"fs_{name}"
        else:
            continue
        os.rename(
            join(notebooks_destination, name), join(notebooks_destination, new_name)
        )

    # -- copy scripts
    scripts_source = "lecture_notes/2_setup_python_project/scripts"
    scripts_destination = join(destination_root, "scripts_fs")
    copy_folder(scripts_source, scripts_destination, ["__pycache__"])

    # -- copy figures
    copy_folder(
        "lecture_notes/2_setup_python_project/figures",
        join(destination_root, "notebooks", "figures"),
    )

    # -- create folder model/predictions
    os.makedirs(join(destination_root, "models", "predictions"), exist_ok=True)
    os.makedirs(join(destination_root, "models", "models"), exist_ok=True)

    # -- adjust notebooks
    notebook_subs = [
        ("../../../data/dsc.db", "../data/raw/dsc.db"),
        ("prediction.csv", "../models/predictions/prediction.csv"),
        ("models.pkl", "../models/models/model.pkl"),
        ("companion_module", "fs_companion_module"),
        ("../figures", "figures"),
        ("dsc.setup_python_project.pyscaffold_test", "pyscaffold_test_fs"),
    ]
    re_sub(notebooks_destination, notebook_subs)

    # -- adjust package
    package_subs = [("dsc.setup_python_project.pyscaffold_test", "pyscaffold_test_fs")]
    re_sub(package_destination, package_subs)

    scripts_subs = [
        ("dsc.setup_python_project.pyscaffold_test", "pyscaffold_test_fs"),
        ("data/dsc.db", "data/raw/dsc.db"),
        ("model.pkl", "models/models/model.pkl"),
        ("prediction.csv", "models/predictions/prediction.csv"),
    ]
    re_sub(scripts_destination, scripts_subs)
