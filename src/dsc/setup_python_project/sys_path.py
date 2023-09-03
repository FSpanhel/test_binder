import os
import sys
from dataclasses import dataclass
from sys import version_info as ver
from typing import List, Optional


@dataclass
class SysInfo:
    excluded_from_sys_path: Optional[List[str]] = None
    sys_path_without_excluded: Optional[List[str]] = None

    def __call__(self, print_: bool = True):
        self.excluded_from_sys_path = []
        self.sys_path_without_excluded = []
        match = [f"python{ver.major}.{ver.minor}", f"python{ver.major}{ver.minor}"]
        # Do not show the package that is on sys.path because of pip install -e .
        ends_with = "dsc/src"
        for folder in sys.path:
            cond_match = any([el in folder for el in match])
            cond_ends_with = folder.endswith(ends_with)
            if not cond_match and not cond_ends_with:
                self.sys_path_without_excluded.append(folder)
            else:
                self.excluded_from_sys_path.append(folder)
        if print_:
            print(
                " > Excluding folders which are always present on sys.path,"
                " the remaining entries of sys.path are"
            )
            print("  -", "\n  - ".join(self.sys_path_without_excluded))
            if "" in self.sys_path_without_excluded:
                print(
                    "> Note that an empty entry of sys.path corresponds to"
                    " the corresponding working directory"
                )
                print(" ", os.getcwd())
        return self


sys_info = SysInfo()


if __name__ == "__main__":
    print("> This file has been run as a Python program.")
else:
    print("> This file has been imported as a module.")

sys_info()
