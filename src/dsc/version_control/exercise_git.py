"""
Helper for the Git exercises in
lecture_notes/1_version_control/3_exercise.ipynb.

Program should be run from the root directory of the project using
python3 -m dsc.version_control.exercise_git [<arg>],
where arg is in ['first', 'second', 'third', 'reset'].
"""
import sys

from dsc.version_control.git import Git

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 1:
        git = Git().reset()

        if args[0] == "reset":
            pass
        elif args[0] in ["first", "second"]:
            git.checkout("_target", True).commit("a.py", "123", "Add")
            git.checkout("main")
            git.checkout("_source", True).commit("b.py", "123", "Add")
        elif args[0] in ["third"]:
            git.checkout("_target", True)
            (
                git.checkout("_source", True)
                .commit("text.md", "abc", "Add abc to the first line of")
                .commit("text.md", "def", "Add def to the second line of", True)
                .commit("text.md", "ghi", "Add ghi to the third line of", True)
                .commit("text.md", "jkl", "Add jkl to the fourth line of", True)
            )

        git.execute()
    else:
        raise Exception("Provide no argument or 'reset'")
