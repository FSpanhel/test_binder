from __future__ import annotations

import os
import sys
from typing import List, Optional, Tuple

import nbformat

# install the package dsc in the env dsc and use this


class NotebookParser:
    def __init__(self, path) -> None:
        self.path = path
        self.nb = nbformat.read(path, nbformat.NO_CONVERT)
        print(f"> Read {path} into NotebookParser")

    def write(self, path: str) -> None:
        nbformat.write(self.nb, path)
        self._delete_py_script(path)
        print(f"> Created {path}")

    def write_without_solution(  # could also subclass here
        self,
        remove_all_code_cells: bool = True,
        remove_md_cells_with_comment: bool = True,
        remove_cells_with_tags: Optional[List[str]] = ["solution"],
    ) -> None:
        self.remove_cells(
            remove_all_code_cells, remove_md_cells_with_comment, remove_cells_with_tags
        )
        path = self._get_path_for_parsing_without_solution()
        self.write(path)
        print(
            f"> {remove_all_code_cells = }, {remove_md_cells_with_comment = },"
            f" {remove_cells_with_tags = }"
        )

    def _get_path_for_parsing_without_solution(self) -> str:
        dir, name, _ = self._get_dir_name_ext(self.path)
        assert "solution" in name
        name_without_solution = name.rsplit("_", 1)[0]
        new_name = f"{name_without_solution}.ipynb"
        path = os.path.join(dir, new_name)
        return path

    def _get_dir_name_ext(self, path: str) -> Tuple[str, str, str]:
        dir = os.path.dirname(path)
        name, ext = os.path.basename(path).rsplit(".", 1)
        return dir, name, ext

    def _delete_py_script(self, path: str, py_script_folder: str = "notebook_as_py"):
        # delete the modified script
        dir, name, _ = self._get_dir_name_ext(path)
        path = os.path.join(dir, py_script_folder, f"{name}.py")
        if os.path.exists(path):
            os.remove(path)
            print(f"> Removed {path}")

    def remove_cells(
        self,
        remove_all_code_cells: bool = True,
        remove_md_cells_with_comment: bool = True,
        remove_cells_with_tags: Optional[List[str]] = None,
    ) -> NotebookParser:
        if remove_cells_with_tags is None:
            remove_cells_with_tags = []

        nb_cells = []
        for cell in self.nb.cells:
            append = True
            cell_tags = cell.metadata.get("tags")
            if remove_all_code_cells:
                if cell["cell_type"] == "code":
                    append = False
            if cell_tags and append:
                for tag in remove_cells_with_tags:
                    if tag in cell_tags:
                        append = False
                        break
            if (cell["cell_type"] == "markdown") and append:
                if remove_md_cells_with_comment:
                    if "[//]: <> (" in cell["source"]:
                        append = False
            """ this matches for the nbextension exercise/exercise2, however
                this extension fucks up rise so don't use it
                if (
                    'solution' in cell['metadata']
                    and 'solution_first' not in cell['metadata']
                ):
                append = False
            """
            if append:
                nb_cells.append(cell)

        self.nb.cells = nb_cells

        return self

    def make_slides(self) -> NotebookParser:
        """If there is no slideshow metadata, i.e., cell['metadata']['slideshow']
        does not exist, set the slideshow of a cell to
          - 'slide' if the cell is markdown and starts with a heading
          - '-' otherwise.
        """
        for cell in self.nb.cells:
            slideshow = cell.get("metadata", {}).get("slideshow", None)
            if not slideshow:
                if cell["cell_type"] == "markdown":
                    if cell["source"].startswith("#"):
                        cell["metadata"]["slideshow"] = {"slide_type": "slide"}
                else:
                    cell["metadata"]["slideshow"] = {"slide_type": "-"}
        return self


if __name__ == "__main__":
    args = sys.argv[1:]
    path = args[0]
    remove_all_code_cells = True
    if len(args) > 1:
        remove_all_code_cells = eval(args[1])
    NotebookParser(path).write_without_solution(
        remove_all_code_cells=remove_all_code_cells
    )
