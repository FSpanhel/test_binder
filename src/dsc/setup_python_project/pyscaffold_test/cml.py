"""
Tools for writing command line interfaces.
"""
from argparse import ArgumentParser, RawDescriptionHelpFormatter


def make_docstring_help_description(__doc__: str):
    """
    Turns the docstring of a script into its command line description.

    Use this function in a script (the function should NOT be accessible if
    the script is imported as a module) to make the docstring of the script
    the description that is displayed when the script is executed with
    the -h flag, e.g., python3 my_script.py -h.

    Args:
        __doc__: The __doc__ attribute of a .py script.

    Returns:
        None.
    """
    ArgumentParser(
        description=__doc__,
        # required so that new lines and spaces are not removed
        formatter_class=RawDescriptionHelpFormatter,
    ).parse_args()
