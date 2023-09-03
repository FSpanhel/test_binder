""" Contains utility functions that are used for all lectures
    like embeding webpages into a Jupyter notebook.
    If run as a script, ~/.jupyter/nbconfig/notebook.json is set to
    nbconfig.json if it does not exist already.
"""
from IPython.display import IFrame

markdown = False


def embed_website(
    url: str, width: int = 900, height: int = 500, markdown: bool = markdown
) -> IFrame:
    """Embed a website into a Jupyter notebook code cell.
    If markdown is True set the figure height to 0.
    """
    if markdown:
        height = 0
    return IFrame(url, width, height)


if __name__ == "__main__":
    import os
    import shutil

    path = os.path.expanduser("~/.jupyter/nbconfig/notebook.json")
    if os.path.exists(path):
        raise FileExistsError(
            f"{path} already exists, please edit {path} manually to set the"
            " notebook extensions"
        )
    else:
        shutil.copy("nbconfig.json", path)
