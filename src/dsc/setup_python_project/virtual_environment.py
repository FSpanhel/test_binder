import os
import shutil
import sys
from site import getsitepackages


def get_path_of_conda_env():
    """Returns the path of the currently activated conda env."""
    path2python = shutil.which("python")  # could also use sys.executable
    parent = os.path.dirname(path2python)
    dsc_env = os.path.dirname(parent)
    return dsc_env


def get_path():
    path = os.getenv("PATH").split(":")
    return path


conda_env = get_path_of_conda_env()
site_packages = getsitepackages()[0]
python = sys.executable
pandas = os.path.join(site_packages, "pandas")
path = get_path()
