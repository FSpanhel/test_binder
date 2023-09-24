# ---
# jupyter:
#   jupytext:
#     comment_magics: false
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% slideshow={"slide_type": "skip"}
from dsc.notebook import embed_website

# %% [markdown] slideshow={"slide_type": "slide"}
# # Agenda
# - This chapter we consider tools and guidelines that improve the quality of your Python code.
#     - Style
#     - Linters
#     - Formatters
#     - Type hints
#     - Git hooks
#     - Documentation

# %% [markdown] slideshow={"slide_type": "slide"}
# # Resources

# %% [markdown] slideshow={"slide_type": "-"}
# - Style
#     - [PEP8](https://peps.python.org/pep-0008)
#     - [Google Style](https://google.github.io/styleguide/pyguide.html)
# - Type hints
#     - [PEP 484 – Type Hints (for functions)](https://peps.python.org/pep-0484/)
#     - [PEP 526 – Syntax for Variable Annotations](https://peps.python.org/pep-0526/)
#     - [Cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
# - Code documentation
#     - Docstrings
#         - [Documenting python code](https://realpython.com/documenting-python-code/)
#         - [Docstrings](https://www.datacamp.com/tutorial/docstrings-python)
#         - [Google docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
#         - [Google and Numpy docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
#     - Sphinx
#         - [Support for Numpy and Google styles](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/)
#     - [Read the Docs: Hosts your docs for free](https://readthedocs.org/)
#     - [Reddit discussion about documentation tools](https://www.reddit.com/r/Python/comments/wq6tlc/whats_a_good_documentation_platform_that_you_guys/)
#     - [MkDocs Tutorial](https://realpython.com/python-project-documentation-with-mkdocs/)
# - Git hooks
#     - [Atlassian](https://www.atlassian.com/git/tutorials/git-hooks)
#     - [Pre-commit](https://pre-commit.com/)
#     - [Getting started with pre-commit](https://towardsdatascience.com/getting-started-with-python-pre-commit-hooks-28be2b2d09d5)

# %% [markdown] slideshow={"slide_type": "slide"}
# # The Zen of python
# - The Zen of Python are 19 guiding principles for writing computer programs and influence the design of the Python programming language

# %% slideshow={"slide_type": "-"}
import this

# %% [markdown] slideshow={"slide_type": "slide"}
# # Style

# %% [markdown] slideshow={"slide_type": "slide"}
# ## PEP 8
# - [PEP](https://peps.python.org/pep-0000/) stands for Python Enhancement Proposal.
# - Guido van Rossum, the creator of Python: “Code is read much more often than it is written.” 
# - Writing readable code is one of the guiding principles of the Python language (see also ["The Zen of Python"](#the-zen-of-python)).
# - [PEP 8](https://peps.python.org/pep-0008) is Python's Style Guide. It exists to improve the readability of Python code.
# - It provides
#     - Naming conventions
#         - In general, use lowercase words separated with underscores to name things, e.g., ```what_an_amazing_name```. 
#         - Use CamelCase for classes.
#         - Use descriptive names!
#     - Rules for code layout
#         - Limit all lines to a [maximum of 79 characters](https://stackoverflow.com/questions/88942/why-does-pep-8-specify-a-maximum-line-length-of-79-characters).
#         - Surround functions and classes with two blank lines. 
#         - Use 4 spaces per indentation level.
#         - Align idents.
#         - Prefer parentheses to wrap long lines over multiple lines instead of using a backslash.
#     - And much more...
# - Click [here]( https://realpython.com/python-pep8/) for a nice introduction

# %% slideshow={"slide_type": "-"}
embed_website("https://peps.python.org/pep-0008/")

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Google's Style Guide
# - Besides Python's style guide I recommend [Google's style guide for Python](https://google.github.io/styleguide/pyguide.html)
# - It provides language and style rules with pros and cons of a particular decision

# %% slideshow={"slide_type": "-"}
embed_website("https://google.github.io/styleguide/")

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Linters

# %% [markdown] slideshow={"slide_type": "slide"}
# - Linters are programs that analyze code for programmtic and stylistic errors.
# - They provide errors and provide provide suggestions on how to fix the error. 
# - Linters are particularly useful when installed as extensions to your text editor, 
# as they flag errors and stylistic problems while you write.
# - As a result, you can catch programming errors before you actually run run the program.
# - Popular Python linters that mainly check the style according to PEP 8 are
#     - [flake8](https://github.com/PyCQA/flake8): Glues together pycodestyle, pyflakes, mccabe, and third-party plugins.
#     - [pylint](https://www.pylint.org/): A static code analysis tool. Stricter than flake8. Recommended by Google.
#     - [Flake8 vs Pylint](https://www.reddit.com/r/Python/comments/82hgzm/any_advantages_of_flake8_over_pylint/)
# - Popular Python linters that perfrom static type checking.
#     - [mypy](https://mypy.readthedocs.io/en/stable/)
#     - [pyright](https://github.com/microsoft/pyright): Developed by Microsoft.
# - Related [tools that help while your coding](https://code.visualstudio.com/docs/editor/intellisense):
#     - [Jedi](https://jedi.readthedocs.io/en/latest/)
#     - [Pylance for VsCode](https://devblogs.microsoft.com/python/announcing-pylance-fast-feature-rich-language-support-for-python-in-visual-studio-code/)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Exercise
# - Install flake8 into your pyscaffold_test environment
# - Consider your scripts and analyze the code of a script using ```flake8 script.py```
# - Read about [Python Linting in VsCode](https://code.visualstudio.com/docs/python/linting) and activate flake8 in VSCode.
# - Open a script and see whether flake8 indicates some problems with your script.
# - If required, fix the warnings and errors.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Formatters
# - Formatters automatically refactor your code to be conform with PEP 8 or/and to be consistent throughout different files and projects, which improves the code quality.
# - People are opinionated about style. By using a formatter before you commit code you skip discussions about code style. 
# - Popular Python code formatters are
#     - [autopep8](https://github.com/hhatto/autopep8): One of the oldest Python code formatter. Rather tries to make your code compliant with PEP 8 than formatting your code. 
#     - [black](https://github.com/psf/black): The uncompromising Python code formatter.
#     - [prettier](https://github.com/prettier/prettier): Opinionated code formatter.
#     - [yapf](https://github.com/google/yapf): Python code formatter developed by Google. Configurable in a lot of ways.
# - For a comparions of these formatters click [here](https://www.kevinpeters.net/auto-formatters-for-python).
# - In this course, we focus on black.
#     - Applies the rules stated in PEP 8 with the exeception being a maximal line length of 88 characters instead of 79.
#     - Configuration is severly limited by design. There should be only one way how code is formatted.
#     - By using it you loose control over your code format. In return, you don't have to worry about formatting and different code styles in a project. 
#     
#

# %% slideshow={"slide_type": "slide"}
embed_website("https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html")

# %% [markdown] slideshow={"slide_type": "slide"}
# - To format script.py with black execute ```black script.py```.
# - Note that black doesn't reformat lines that end with ```# fmt: skip``` or blocks that are enclosed by 
# ```# fmt: off``` and ```# fmt: on```.
# - Although black does its job pretty well, there are [issues]("https://github.com/psf/black/issues/2279") with formatting [call-chains](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#call-chains) and you might have to excluded call-chains lines manually from formatting.
# - Moreover, if you like to apply the ["single quotes for data, double quotes for human-readable strings"](https://stackoverflow.com/questions/56011/single-quotes-vs-double-quotes-in-python/56190#56190) philosophy for formatting strings, you can click [here](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#strings ) how to enables this in black
#
#

# %% [markdown]
# ### Exercise
# - Install black.
# - Run black on some files.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Import order

# %% [markdown] slideshow={"slide_type": "-"}
# - According to PEP8, Imports should be grouped in the following order:
#     - Standard library imports.
#     - Related third party imports.
#     - Local application/library specific imports.
# - [isort](https://github.com/PyCQA/isort) is a little tool that sorts your imports accordingly and by type (in-built, third-party, project-specific modules).
# - It can be combined with black.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Type hints/annotations
# - Type hints are described in 
#     - [PEP 484 – Type Hints (for functions)](https://peps.python.org/pep-0484/)
#     - [PEP 526 – Syntax for Variable Annotations](https://peps.python.org/pep-0526/)
# - With type hints you can annotate the type of the object(s) you're using.
# - For instance, without type hints a function might look as follows
# ```python3
# def my_very_complex_function(arg1_ls, arg2_dc, number, column_fun, df):
#     ... 
# ```

# %% [markdown] slideshow={"slide_type": "fragment"}
# - Using type hints, the function definition might be
# ```python3
# def my_very_complex_function(
#     arg1_ls: List[str], 
#     arg2_dc: Dict[str, List[float]], 
#     number: int, 
#     column_fun: Callable,
#     df: pd.DataFrame
# ) -> Dict[str, float]:
#     ...
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# - Type hinting is and will ever be optional in Python.
# - But I strongly recommend to use type hints (whenever possible) because
#     - It improves the documentation.
#     - Type checkers can verify whether the inputs and outputs of a function have the required type.
#     - IDEs suggesting more appropriate methods and functions.
#     - Especially in a larger project, your code becomes more predictable.  
# - For an introduction to type hints, you can click [here](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) and [here](https://realpython.com/lessons/type-hinting/).

# %%
embed_website("https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html")

# %% [markdown] slideshow={"slide_type": "slide"}
# - If your write a class, then the first line of your code should be ```from __future__ import annotations``` so that the return type of a method can be the class itself, e.g.,
#     ```python
#     from __future__ import annotations
#
#     class A:
#         def return_instance(self) -> A:
#         return self
#     ```
# - 

# %%
## Type annotations
- mypy 
- https://github.com/microsoft/pyright 

# %% [markdown]
# ## Exercise
# - Install mypy in your pyscaffold_test environment.
# - Read about [Python Linting in VsCode](https://code.visualstudio.com/docs/python/linting) and activate mypy in VsCode.
# - To use multiple linters together in VSCode, use the command palette to oepn ```Preferences: Open Settings (JSON)``` and, e.g., write the following lines in settings.json
# ```
#     "python.linting.flake8Enabled": true,
#     "python.linting.mypyEnabled": true,
#     "python.linting.pylintEnabled": false,
# ```
# - Open the modules of your pyscaffold_test package and check whether mypy complains finds any issues.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Git hooks and Pre-commit

# %% [markdown] slideshow={"slide_type": "-"}
# ## Git hooks
# - [Git hooks](https://www.atlassian.com/git/tutorials/git-hooks) are custom scripts that are automatically executed before or after a specific event (e.g., a commit or rebase) occurs in a Git repository. 
# - With Git hooks you can improve and standardize your code developement.
# - Common use cases.
#     - Inspect the files that about to be committed and adjust them and/or the commit message before applying the commit (e.g., remove trailing whitespace, format code, ...)
#     - Reject commits that don’t meet specified requirements (file is too large, bad style, syntax errors, failed tests, ...)
#     - Pointing out issues before a code review, which improves the code review process.
#     - Changing the project environment based on repository status.
#     - Implement continuous integration workflows.
# - There are two groups of hooks
#     - Client-side: Specified in the local repo and triggered by operations such as commit and merging.
#     - Server-side: Triggered by network operations such as receiving push commits.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Pre-commit

# %% [markdown] slideshow={"slide_type": "-"}
# - In the following, we only consider the pre-commit script.
# - This script is executed every time before Git git creates a commit.
# - In order that a pre-commit script runs, you have create it and install required dependencies (e.g., linters) in the corresponding environment 
# - [pre-commit](https://pre-commit.com/) is a framework for managing and maintaining multi-language pre-commit hooks (that are locally executed).
#     - You only have to specify the url of a Git repository that contains hooks and pre-commit manages the 
# installation and execution of these hooks before every commit
# - **Please install pre-commit in your pyscaffold_test environment (!)**.
# - To use pre-commit you have to set up its configuration .pre-commit-config.yaml in the root of your project.
# - Luckily, PyScaffold has already taken care of that :) 

# %% slideshow={"slide_type": "slide"}
!cat ../../../pyscaffold_test/.pre-commit-config.yaml

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Note that you don't have to install a package into your environment if you want to use it with pre-commit (that's the main reason why Pre-commit was created!)
# - The repo key tells pre-commit where to find the code for the hook.
# - For an explanation of the configuration see the corresponding [section](https://pre-commit.com/#pre-commit-configyaml---top-level) in the official docs.
# - Note that I would not recommend to add a hook for checking type annotations, e.g., [mypy](https://github.com/pre-commit/mirrors-mypy), because it can be difficult to satisfy them (but you should user a linter for checking type annotations)
# - Investigate the first hook https://github.com/pre-commit/pre-commit-hooks

# %% [markdown] slideshow={"slide_type": "slide"}
# - Run ```pre-commit install``` to set up the Git hook scripts.
# - Thereafter, run ```pre-commit autoupdate``` to update your hooks to the latest version.
# - Pre-commit will now run whenever you want to apply a Git commit.
#     - All unstaged files are stashed by Git before the pre-commit script is run. These files are restored when the script terminates. 
#     - If you use a GUI to apply a commit you might observe some funny behavior because most GUIs do not support pre-commit (directly)
#         - I recommend to to run ```git commit``` in the terminal when using hooks.
#     - Files that should be committed might be changed by the pre-commit script. 
#     - The commit is aborted if the pre-commit script does not terminate with exit status 0.
#         - In this case, modification to files due to running the pre-commit script are not automatically staged.
#         - I recommend to stage these changes before your run pre-commit scripts again.
#     - You can bypass the pre-commit script by adding the flag no-verify, i.e., ```git commit --no-verify```
# - If you have already committed files to Git before pre-commit was installed you should run the hooks
#   for all 
# It is usually a good idea to run the hooks for all files when new hooks are added (usually pre-commit is run only for the changed files during git hooks). / Run pre-commit run --all-files if there are file that were committed before adding the git hooks.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Exercise
# - Set up pre-commit taking into account the information on the previous slides.
# - Create the following script ```pyscaffold_test/scripts/pre_commit.py``` with the following content
#
# ```python
# """
# Demontrates the effects of using pre-commit. 
# """
# import pandas as pd
# import os
# import numpy as np
#
# newline = "\n"
#
# def i_am_a_function_that_returns_the_absolute_path_of_the_folder_of_this_file(before: str = '', after: str = '') -> str:
#     path = os.path.abspath(os.path.basename(__file__))
#     return f"{before}{newline}{path}{newline}{after}"
#
# df = pd.DataFrame([1, 2, 3])
#
# output = i_am_a_function_that_returns_the_absolute_path_of_the_folder_of_this_file(before="Hello from", after="Nice to meet you!")
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# - Commit ```pyscaffold_test/scripts/pre_commit.py``` using the terminal.
# - Observe the output of the terminal when the pre-commit hooks are executed. What do you observe?
# - Investigate the changes done by the pre-commit hooks.
# - Add the changes to the staging are.
# - Commit ```pyscaffold_test/scripts/pre_commit.py``` again.
# - If the commit has not succeeded, perform the required steps so that a commit is accepted and commit ```pyscaffold_test/scripts/pre_commit.py```.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Code documentation
# - Documentation is crucial for any software project, but often neglected. 
# - Why documenting your code is important
#     - Code is more often read than written.
#     - If you are writing software and the documentation is not good enough, people will not use it (including yourself).
# - Commenting vs Documenting 
#     - Use comments to describe your code for developers and explain explain non-obvious parts or decisions.
#     - Use documenting to describing the use and functionality of your software to users.
# - In this course we focus on documentating the API of your package that you use for your project.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Docstrings and Docstrings formats

# %% [markdown] slideshow={"slide_type": "-"}
# - Python uses docstrings to document code. 
# - The docstring of a function, class, module, script, or (the ```__init__.py``` of) a package, is the string directly below the object, e.g.,
# ```python
# def fun():
#     """
#     I am the docstring
#     
#     I rock!
#     """
# ```
# - [PEP 257](https://peps.python.org/pep-0257/) describes docstring conventions. 
# <!-- Docstrings should always use triple-double quotes """, slinge-line and multi-line docstrings -->
# - Please click [here](https://realpython.com/documenting-python-code/#docstring-types) to learn more about how to write docstrings for different objects.
# - To access the docstring of a function, class or module use ```help(object)```.
# - If you are using IPython (e.g., a Jupyter notebook with an IPython kernel) you can also use ```object?```
# - Note that the doc string of an object is also contained in its attribute ```__doc__```, e.g., ```print(getattr(1, '__doc__')```, which can be modified at runtime if the object is not built-in
# - You can also investigate the documentation of ```<name>``` using ```python3 -m pydoc <name>```, where name can be a module, package and much more ( ```python3 -m pydoc -h```), e.g., ```python3 -m pydoc pyscaffold_test.data```
# - You can even start a server to see the documentation in the browser using ```python -m pydoc -p <port>``` (pretty, isn't it?)

# %% [markdown] slideshow={"slide_type": "slide"}
# - The top 3 most popular Python docstrings formats are
#     - [reSt (reStructuredText)](https://docutils.sourceforge.io/rst.html): [Official Python documentation standard](https://peps.python.org/pep-0287/), verbose and some learning-curve.
#     - [Google docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings): Simple to write and to read.
#     - [NumPy/SciPy docstrings](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard): Combination of reST and Google Docstrings.
# - I recommend to use [Google docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html), due to simplicity, which look as follows for a function
#
# ```python
# """
# Computes the answer to the ultimate question of life, the universe, and everything.
#
# Args:
#     the_question: The ultimate question of life, the universe, and everything.
#     verbose: A flag used to print the estimated completion time during 
#         computation (default is False)
#
# Returns:
#     int: 42
# """
# ```
# - Note that you don't have to specify the type of the arguments and the return value if you use type hints.
# - Click [here](https://google.github.io/styleguide/pyguide.html#doc-function-raises) for a more advanced example.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Auto-generating a (html) API documentation from docstrings
# - There are several tools that you can use to create much of your API documentation automatically.
# - [Sphinx](https://www.sphinx-doc.org/): Powerful but also a bit difficult to use.  
#     - Developed for documenting Python. Popular libraries (NumPy, SciPy, Pandas, Matplotlib...) uses Sphinx. 
#     - The Linux kernel also uses Sphinx.
#     - With the [Autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) extension you can generate documentation automatically from docstrings. 
# - [pdoc](https://pdoc.dev/): Simple and easy to use. Only Python API documentation. 
# - [MkDocs](https://www.mkdocs.org/): A rather simple tool for project documentation.
#     - Used for [pydantic](https://pydantic-docs.helpmanual.io/). 
#     - For API documentation one can use [mkdocstrings](https://mkdocstrings.github.io/) to automatically generate documentation from docstrings.
# - And many more!

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Using PyScaffold to create a Sphinx documentation
# - PyScaffold will prepare a docs directory that contains everything that you need to write your documentation with Sphinx.
# - Moreover, the Numpy and Google style docstrings are activated by default (Otherwise you would have to use reST in the docstrings).
# <!-- - Sphinx can only parse reSt, but [current versions](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) can now parse NumPy and Google style docstrings and convert them to reSt before Sphinx parses them. -->
# - The DS extension of PyScaffold enables the use of a Markdown README.md file (and not a reST README.rst) which is included into the documentation.
# - To build a Sphinx documentation for a project that has been set up with PyScaffold we can use
#     - ```make -C docs html``` (requires that make is installed in the activated environment, you probably also have to install Linkify)
#     - ```tox -e docs``` (requires that tox is installed in the activated environment and that [tox.ini](tox.ini) is available)
#         - Moreover, in setup.cfg you have to add the dependencies of your pyscaffold_test package as follows
#         ```
#         install_requires =
#             importlib-metadata; python_version<"3.8"
#             pandas
#             matplotlib
#         ```
# <!-- Alternative:
#     - Add the dependencies of the project package to ```project_root/docs/requirements.txt```
#                 - Note that the dependencies of your project package is often smaller than the dependencies of the project
#                 - In the case of the pyscaffold_project package, the dependencies are pandas and matplotlib
#             - Need a tox.ini
# -->
# matplotlib
#             add the site-packages directory of your environment manually to 
#         ```python
#         # If extensions (or modules to document with autodoc) are in another directory,
#         # add these directories to sys.path here. If the directory is relative to the
#         # documentation root, use os.path.abspath to make it absolute, like shown here.
#         ```
#         sys.path.append('/home/spa0001f/programs/miniconda3/envs/pyscaffold_test/lib/python3.10/site-packages')
#         - Note that adjusting install_requires in setup.cfg has no effect here
# - After the docs are successfully created, you can use a browser to open the starting page ```docs/_build/html/index.html```
# - I suggest to change add the flag ```--module-first``` to ```sphinx-apidoc --implicit-namespaces -f -o {output_dir} {module_dir}``` in docs/conf.py to [put the module documentation before the submodule documentation](https://stackoverflow.com/a/66365397) 

# %% [markdown]
# - setup.cfg
# ```yaml
# - install_requires =
#     pandas
#     matplotlib
# ```
#     - if pandas is excluded, then
#     ```python
#     Traceback (most recent call last):
#       File "/home/spa0001f/github/teach/pyscaffold_test/.tox/docs/lib/python3.10/site-packages/sphinx/config.py", line 350, in eval_config_file
#         exec(code, namespace)
#       File "/home/spa0001f/github/teach/pyscaffold_test/docs/conf.py", line 27, in <module>
#         import pandas as pd
#     ModuleNotFoundError: No module named 'pandas'
#     ```
# - tox.ini
#
#

# %% [markdown]
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Exercise
# - Write docstrings for your pscaffold_test package
#     - Module doctring.
#     - Function docstring.
# - Use Sphinx to make a documentation for your pscaffold_test package.
# - Note: If you don't like the look of your Sphinx documentation, you can search the web how to change the theme.

# %% [markdown]
# # Code reviews: Zu Collaboration?

# %% [markdown]
# https://github.com/google/eng-practices

# %% [markdown]
# # Writing code

# %% [markdown]
# # Redable Code: Überschnitt mit 0_general. how to resolve?
# def dispatch(arg, value):
#     if arg == 'optionA':
#         function_a(value)
#     elif arg == 'optionB':
#         function_b(value)
#     elif arg == 'optionC':
#         function_c(value)
#     else:
#         default(value)
# What we actually want to say is that each argument maps to a function which is then called with a certain value like
#
# dispatch = {'optionA': function_a,
#             'optionB': function_b,
#             'optionC': function_c}
# dispatch.get(arg, default)(value)
#
# pd.loc[a & b & c , ] replace by cond
#
#
# insteand of
# c = 0
# for i in object:
#     c = c + 1
#     pass
# for c, i in enumerate(object):
#     pass

# %% [markdown]
# ## pure functions

# %% [markdown]
# ## Debugging

# %%
Note: if your script does not run you can use python3 -m pdb [<script>] to debug the script or use vscode
    
https://www.codementor.io/@stevek/advanced-python-debugging-with-pdb-g56gvmpfa
    
In Jupyter notebooks you can use the magic command %debug

# %% [markdown]
# ## Helpful python built-ins
# getattr, setattr
# vars, dir 

# %%
import builtins
dir(builtins)

# %% [markdown]
# ## Dataclasses, pydantic, attrs

# %% [markdown]
#

# %% [markdown] heading_collapsed=true
# ## Logging
# https://www.reddit.com/r/Python/comments/vrrb0t/comment/iexa3ww/?utm_source=share&utm_medium=ios_app&utm_name=iossmf&context=3 -> https://gitlab.com/danielquinn/majel-orchestrator/-/blob/feature/initial/majel/logger.py
#

# %% [markdown]
# ## Input/Output: TODO

# %% [markdown]
# Pickle? Csv. Parquet?
#
# - pickle: 
#     - not human-readable
#     - not portable between different Python versions!
#     - not cross-platform https://mail.python.org/pipermail/tutor/2010-May/075980.html
#     - can also save non-data objects 
# Pickle is not secure, so you don't want to use that for sharing data. It can also have compatability issues between systems/versions, so for long term storage it's also not ideal. But for saving stuff short term on your own computer it's fine.
# - json:
# - csv:
#     - human-readaable
# While CSV might mangle your data types, often that's not really an issue, and its easy to debug as the data is stored as plain text. So usually if you want to share data, especially with non-programmers, CSV isn't all that bad.
# Csv is for human readable/editable data.
# - looses type info of columns
# - parquet:
# - feather: 

# %% [markdown]
# ## Classes

# %% [markdown]
# ## Decorators
