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
#     display_name: Python [conda env:ds_with_types]
#     language: python
#     name: conda-env-ds_with_types-py
# ---

# %% [markdown] toc=true
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Debugging-and-Python-debuggers" data-toc-modified-id="Debugging-and-Python-debuggers-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Debugging and Python debuggers</a></span><ul class="toc-item"><li><span><a href="#Resources" data-toc-modified-id="Resources-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Resources</a></span></li><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Introduction</a></span><ul class="toc-item"><li><span><a href="#What-is-debugging?" data-toc-modified-id="What-is-debugging?-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>What is debugging?</a></span></li><li><span><a href="#How-can-I-see-what-my-code-is-doing-(to-find-and-resolve-bugs)?" data-toc-modified-id="How-can-I-see-what-my-code-is-doing-(to-find-and-resolve-bugs)?-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>How can I see what my code is doing (to find and resolve bugs)?</a></span></li><li><span><a href="#What-is-a-debugger?" data-toc-modified-id="What-is-a-debugger?-1.2.3"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>What is a debugger?</a></span></li><li><span><a href="#Why-and-when-should-I-use-a-debugger?" data-toc-modified-id="Why-and-when-should-I-use-a-debugger?-1.2.4"><span class="toc-item-num">1.2.4&nbsp;&nbsp;</span>Why and when should I use a debugger?</a></span></li></ul></li><li><span><a href="#With-what-tools-can-you-debug-in-Python?" data-toc-modified-id="With-what-tools-can-you-debug-in-Python?-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>With what tools can you debug in Python?</a></span></li><li><span><a href="#How-to-start-a-debugger" data-toc-modified-id="How-to-start-a-debugger-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>How to start a debugger</a></span></li><li><span><a href="#Using-VS-Code-to-debug-a-script" data-toc-modified-id="Using-VS-Code-to-debug-a-script-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Using VS Code to debug a script</a></span><ul class="toc-item"><li><span><a href="#Starting-the-debugger" data-toc-modified-id="Starting-the-debugger-1.5.1"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>Starting the debugger</a></span></li><li><span><a href="#Set-up-a-debugger-configuration" data-toc-modified-id="Set-up-a-debugger-configuration-1.5.2"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>Set up a debugger configuration</a></span><ul class="toc-item"><li><span><a href="#Launch-and-attach-configurations" data-toc-modified-id="Launch-and-attach-configurations-1.5.2.1"><span class="toc-item-num">1.5.2.1&nbsp;&nbsp;</span><a href="https://code.visualstudio.com/docs/editor/debugging#_launch-versus-attach-configurations" rel="nofollow" target="_blank">Launch and attach configurations</a></a></span></li></ul></li><li><span><a href="#Interacting-with-the-debugger" data-toc-modified-id="Interacting-with-the-debugger-1.5.3"><span class="toc-item-num">1.5.3&nbsp;&nbsp;</span>Interacting with the debugger</a></span><ul class="toc-item"><li><span><a href="#Mutating-state" data-toc-modified-id="Mutating-state-1.5.3.1"><span class="toc-item-num">1.5.3.1&nbsp;&nbsp;</span>Mutating state</a></span></li><li><span><a href="#Log-points" data-toc-modified-id="Log-points-1.5.3.2"><span class="toc-item-num">1.5.3.2&nbsp;&nbsp;</span><a href="https://code.visualstudio.com/docs/editor/debugging#_logpoints" rel="nofollow" target="_blank">Log points</a></a></span></li><li><span><a href="#Watching-variables" data-toc-modified-id="Watching-variables-1.5.3.3"><span class="toc-item-num">1.5.3.3&nbsp;&nbsp;</span>Watching variables</a></span></li><li><span><a href="#Conditional-breakpoints" data-toc-modified-id="Conditional-breakpoints-1.5.3.4"><span class="toc-item-num">1.5.3.4&nbsp;&nbsp;</span>Conditional breakpoints</a></span></li><li><span><a href="#Functions-breakpoints" data-toc-modified-id="Functions-breakpoints-1.5.3.5"><span class="toc-item-num">1.5.3.5&nbsp;&nbsp;</span>Functions breakpoints</a></span></li></ul></li><li><span><a href="#Debugging-from-the-command-line" data-toc-modified-id="Debugging-from-the-command-line-1.5.4"><span class="toc-item-num">1.5.4&nbsp;&nbsp;</span><a href="https://code.visualstudio.com/docs/python/debugging#_command-line-debugging" rel="nofollow" target="_blank">Debugging from the command line</a></a></span><ul class="toc-item"><li><span><a href="#Providing-command-line-arguments-to-a-program-that-should-be-debugged" data-toc-modified-id="Providing-command-line-arguments-to-a-program-that-should-be-debugged-1.5.4.1"><span class="toc-item-num">1.5.4.1&nbsp;&nbsp;</span>Providing command line arguments to a program that should be debugged</a></span></li></ul></li></ul></li><li><span><a href="#Using-VS-Code-to-debug-a-notebook" data-toc-modified-id="Using-VS-Code-to-debug-a-notebook-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Using VS Code to debug a notebook</a></span></li><li><span><a href="#Real-case-example:-Debugging-https://gitlab.p7s1.io/ent-bi-data-science/ga_vs_walle_report/-/issues/21" data-toc-modified-id="Real-case-example:-Debugging-https://gitlab.p7s1.io/ent-bi-data-science/ga_vs_walle_report/-/issues/21-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Real case example: Debugging <a href="https://gitlab.p7s1.io/ent-bi-data-science/ga_vs_walle_report/-/issues/21" rel="nofollow" target="_blank">https://gitlab.p7s1.io/ent-bi-data-science/ga_vs_walle_report/-/issues/21</a></a></span></li></ul></li><li><span><a href="#Unfinished" data-toc-modified-id="Unfinished-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Unfinished</a></span><ul class="toc-item"><li><span><a href="#Using-pdb" data-toc-modified-id="Using-pdb-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Using pdb</a></span><ul class="toc-item"><li><span><a href="#Interactive-IPython/Jupyter-sessions" data-toc-modified-id="Interactive-IPython/Jupyter-sessions-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Interactive IPython/Jupyter sessions</a></span><ul class="toc-item"><li><span><a href="#Post-mortem" data-toc-modified-id="Post-mortem-2.1.1.1"><span class="toc-item-num">2.1.1.1&nbsp;&nbsp;</span>Post mortem</a></span></li></ul></li></ul></li><li><span><a href="#How-to-debug?" data-toc-modified-id="How-to-debug?-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>How to debug?</a></span></li></ul></li><li><span><a href="#Debugger" data-toc-modified-id="Debugger-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Debugger</a></span><ul class="toc-item"><li><span><a href="#Enter-the-debugger-at-a-specifc-line" data-toc-modified-id="Enter-the-debugger-at-a-specifc-line-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Enter the debugger at a specifc line</a></span></li><li><span><a href="#interact-and-embed" data-toc-modified-id="interact-and-embed-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>interact and embed</a></span></li></ul></li></ul></div>

# %% [markdown]
# This notebook contains everything related to package development.

# %% [markdown]
# # Debugging and Python debuggers

# %% [markdown]
# ## Resources
# - How to debug in Python using `pdb`
#     - [GeeksForGeeks](https://www.geeksforgeeks.org/debugging-in-python-with-pdb/): Concise but comprehensive overview with good examples
#     - [CodeMentor](https://www.codementor.io/@stevek/advanced-python-debugging-with-pdb-g56gvmpfa)
#     - [RealPython](https://realpython.com/python-debugging-pdb/)
# - [Overview of Python debuggers](https://wiki.python.org/moin/PythonDebuggingTools#Debuggers)
# - VS Code
#     - Official docs
#         - [General debugging](https://code.visualstudio.com/docs/editor/debugging)
#         - [Python debugging intro](https://code.visualstudio.com/docs/python/python-tutorial#_configure-and-run-the-debugger)
#         - [Python debugging](https://code.visualstudio.com/docs/python/debugging)
#     - [Python debugging video](https://www.youtube.com/watch?v=oCcTiRGPogQ)
#     - [How to view pd.DataFrames](https://stackoverflow.com/questions/60097076/view-dataframe-while-debugging-in-vs-code)
# - Determine which commit introduced a particular bug using `git bisect`
#     - https://www.metaltoad.com/blog/beginners-guide-git-bisect-process-elimination
#     - https://stackoverflow.com/questions/4713088/how-to-use-git-bisect

# %% [markdown]
# ## Introduction

# %% [markdown]
# ### What is debugging?
# [Wikipedia](https://en.wikipedia.org/wiki/Debugging):
#
# - In computer programming and software development, debugging is the process of **finding and resolving bugs** (defects or problems that prevent correct operation) within computer programs, software, or systems.
# - Debugging tactics can involve **interactive debugging, control flow analysis, unit testing, integration testing, log file analysis**, monitoring at the application or system level, memory dumps, and profiling. 
# - Many programming languages and software development tools also offer programs to aid in debugging, known as **debuggers**.

# %% [markdown]
# ### How can I see what my code is doing (to find and resolve bugs)?
#
# 1. Using a **[REPL/interactive (I)Python or Jupyter session](https://realpython.com/python-repl/)**
#     - Okay for prototyping. Can alter the state of variables or edit code.
#     - Not convenient and not applicable for more complex tasks.
# 1. Using **Jupyter notebooks** to separate the code into steps and looking at the result of each step.
#     - Great for prototyping. Can alter the state of variables or edit code.
#     - Not applicable for more complex tasks and when it is cumbersome to separate code into steps (e.g., functions, classes)
#     - Can become confusing if many cells are involved and/or cells are evaluated in a non-linear manner and source code is edited in between. 
# 1. Inserting **print statements** to trace code.
#     - You just need to know how to print statements.
#     - Quickly gets tedious and messy, changes source code every time a print statement is added or removed. Use logging instead.
#     - Cannot alter the state of variables or edit code.
#     - You need to specify what is printed. 
# 1. **Logging**
#     - The appropriate tool of choice to monitor (and understand) the operation of a program.
#     - It takes some time to use Python's logging module effectively and efficiently (or use `ds.io.logging`)
#     - Cannot alter the state of variables or edit code.
#     - You need to specify what is logged.
# 1. Using a **debugger**
#     - The appropriate tool to investigate the execution of a program.
#     - Can run, stop, resume and alter the exceution of a program without touching the source code.
#     - Depending on which debugger you use, it takes some time to use them efficiently.

# %% [markdown]
# ### What is a debugger?
# - A debugger is a software tool to **inspect the execution of programs and identify errors** in programs.
# - A debugger can be used to **step through the code, line by line**, to identify the cause of the error or investigate the behavior of a program.
# - Instead of running a program step by step, a debugger can also be used to examine the program at specific lines or when a particular events happen by setting **breakpoints**.
# - The debugger can also be used to **modify values of variables** to see how the program responds to different inputs.
# - Debuggers are available for many programming languages and platforms, ranging from simple **command-line tools** to complex integrated development environments (**IDEs**). 
# - They can be used to debug programs running on a local machine or remotely.
# - Overall, a debugger is an **essential tool for software developers** to ensure that their programs are working correctly.

# %% [markdown]
# ### Why and when should I use a debugger?
# - You don't have to use a debugger if you are "coding" in Jupyter notebooks and don't use functions or classes.
# - In fact, Jupyter notebooks are already like an interactive debugger.
# - You definitely want to use a debugger, if you want to investigate a .py script that contains functions and classes
#     - Automating a job
#     - Developing a package
# - In this case, debuggers are great to identify the cause of a bug and to understand what is happening and how different parts of the code are interacting with each other.
# - Getting used to use a debugger takes some time, but once you know how to use it efficiently you cannot imagine coding without it!

# %% [markdown]
# ## With what tools can you debug in Python?

# %% [markdown]
# - There are many tools to debug in Python, see [here](https://wiki.python.org/moin/PythonDebuggingTools) for an overview of debuggers.
# - **Command-line interfaces**
#     - [pdb](https://docs.python.org/3/library/pdb.html) is the built-in debugger
#         - Advantage: Always available. Quite flexible.
#         - Drawback: Not user friendly, stubborn.
#     - [ipdb](https://pypi.org/project/ipdb/) is the IPython debugger
#         - Advantage: Improves on `pdb`, namely ...
#         - Drawback: Requires installation. Still some issue one has to be aware of. Sometimes doesn't work (?)
#     - [pdb++](https://github.com/pdbpp/pdbpp) (Plus Plus!)
#         - Advantage: Ever better than `ipdb`.
#         - Drawback: Requires installation.
#     - ...
# - **IDEs**
#     - [VS Code](https://code.visualstudio.com/docs/python/debugging): The [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) can be used to debug scripts and (individual cells of) [Jupyter notebooks](https://code.visualstudio.com/docs/python/jupyter-support-py#_debug-a-jupyter-notebook). 
#         - The used debugger is the Python package [debugpy](https://github.com/microsoft/debugpy) which is an implementation of the [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/)
#         - Advantage: Very nice interface, easy to use, and powerful.
#         - Drawback:
#             - ~~AFAIK cannot modify the state of a program, cannot evaluate functions, pd.DataFrames are hard to investigate, pd.DataFrames are hard to modify~~
#             - Requires VS Code and Python >= 3.7   
#             - Setting of breakpoints from the command line not possible, for me it does not work from the command line. Documentation about debugpy is limited.
#     - PyCharm: No experience but appears to be good.
#         
# - **Recommendation**:
#     - ~~Use `pdb` and `ipdb` unless the debugger of VS Code allows to change the state of a programm~~
#     - Use VS Code

# %% [markdown]
# ## How to start a debugger
# In general, a debugger can be used in the following ways
#
# - Run a script in debug mode. This allows for post-mortem debugging or stopping at breakpoints.
# - Interactive: Start a debugger for an expression during an interactive Python session.
# - Setting a breakpoint: Stop the exceution at the breakpoint.
# - Post mortem: Start a debugger when an exception is thrown.

# %% [markdown]
# ## Using VS Code to debug a script
# - AFAIK it is not possible to use VS Code for debugging during an interactive Python session
# - In the following, you can use the script `illstrate_debugging.py` to debug

# %% [markdown]
# ### Starting the debugger

# %% [markdown]
# - You can debug a script with no debugger configuration or by selecting a debugger configuration
# - In any case, you can start a debugger for an opened .py file in one of the following ways
#     - Press `F5`
#     - Select the Run and Debug icon in the Activity Bar (or press `Ctrl+Shift+D`) and select `Run and Debug`
#     - Choose `Run` > `Start Debugging` in the top level menu
# -  If no configuration is selected and you start the debugger of a workspace for the first time, you also have to select how to debug your code, e.g., `Python File`, before the debugger starts
# - You can also click `Debug Python File` at the top right of the editor pane, [which does not consider any configuration](https://stackoverflow.com/a/69803152), even if a configuration file has been created (!)
# - Note, if not configured,
#     - The debugger uses the Python interpreter that is selected in VS Code. To change the interpreter select `Python: Select Interpreter` via the Comand Palette, see [here](https://code.visualstudio.com/docs/python/debugging#_python)
#         - Unfortuantely, setting `"python": "${env:CONDA_PREFIX}/bin/python"` to use the interpreter of the current terminal, yiels an error
#         - Thus, it does not seem to be possible to synchronize the integrated terminal with the debugger, I've opened the corresponding [issue](https://github.com/microsoft/pylance-release/issues/4356)
#     - The working directory of the debugger is your workspace folder, i.e., the folder you have opened, see [here](https://code.visualstudio.com/docs/python/debugging#_cwd). 
#         - So if you run the debugger, your working directory in the terminal is be changed to this directory
#         - Set `"cwd": ".",` in the configuration so that the current working directory of the terminal is used and not changed

# %% [markdown]
# ### Set up a debugger configuration

# %% [markdown]
# - A configuration drives VS Code's behavior during a debugging session. 
# - Configurations are defined in a launch.json file that's stored in a .vscode folder in your workspace.
# - Use `Run > Open configurations` menu command to create a configuration.
# - See [here](https://code.visualstudio.com/docs/python/debugging#_initialize-configurations) for more information and [here](https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes) and [here](https://code.visualstudio.com/docs/python/debugging#_set-configuration-options) for all configuration options.
# - The configuration is stored in the launch.json file located in the .vscode folder of your workspace.
# - Note that if you have created a configuration, a configuration will always be selected and considered when a debugger runs.
# - You have to select the configuration before you start the debugger.
# - To run the debugger with no configuration click `Debug Python File` at the top right of the editor pane.
# - See [here](https://code.visualstudio.com/docs/editor/debugging#_global-launch-configuration) for a global configuration.

# %% [markdown]
# #### [Launch and attach configurations](https://code.visualstudio.com/docs/editor/debugging#_launch-versus-attach-configurations)
# - In VS Code, there are two core debugging modes, Launch and Attach, which handle two different workflows and segments of developers.
# - VS Code debuggers typically support launching a program in debug mode or attaching to an already running program in debug mode.

# %% [markdown]
# ### Interacting with the debugger
#
#

# %% [markdown]
# - Once a debug session starts, the Debug toolbar will appear on the top of the editor, see [here](https://code.visualstudio.com/docs/editor/debugging#_debug-actions)
# - The top-level `Run` menu has the most common run and debug commands

# %% [markdown]
# #### Mutating state
# **Inspecting and setting values**
# - The value of variables can be seen and set in the following ways
#     - In the `VARIABLES` section of the `Run and Debug` view
#     - By hovering over the names in the script
#     - In the `Debug Console`
#
# **Evaluating expressions**
# - You can use the [Debug Console](https://code.visualstudio.com/docs/editor/debugging#_debug-console-repl) to evaluate arbitrary expressions, e.g., evaluate or change functions
# - To use the Debug Console, press `Ctrl+Shift+Y` or select `View: Debug Console command` at the top menu, or select it in the terminal view.
# - Note: 
#     - If you need to enter multiple lines, use `Shift+Enter` between the lines and then send all lines for evaluation with `Enter`
#     - If [redirectOutput](https://code.visualstudio.com/docs/python/debugging#_redirectoutput) is set to false, 
#         - If you execute `help´ into the debug console, the result is printed to the terminal
#         - If you need to enter your MFA code for AWS, it must be entered into the terminal
#     - To disable warnings like `pyydevd warning: Computing repr of ... was slow (took x.xs)`, set the following environment variable to, e.g., 2 seconds, `PYDEVD_WARN_SLOW_RESOLVE_TIMEOUT=2`, see [here](https://stackoverflow.com/questions/71695716/pydevd-warnings-in-visual-studio-code-debug-console) for more information
#
# **Investigating the Call Stack**
# - https://stackoverflow.com/a/70536049

# %% [markdown]
# #### [Log points](https://code.visualstudio.com/docs/editor/debugging#_logpoints)
# - A Logpoint is a variant of a breakpoint that does not "break" into the debugger but instead logs a message to the console. -> does not work for me?
#
# #### Watching variables
# - You can watch the value of a variable by adding it via `+` in the WATCH panel of the `Run and Debug` view in the sidebar
#
# #### Conditional breakpoints
# - A powerful VS Code debugging feature is the ability to set conditions based on expressions, hit counts, or a combination of both.
# - Expression condition: The breakpoint will be hit whenever the expression evaluates to true.
# - Hit count: The 'hit count' controls how many times a breakpoint needs to be hit before it will 'break' execution. Whether a 'hit count' is respected and the exact syntax of the expression vary among debugger extensions.
#
# #### Functions breakpoints
# - A function breakpoint is created by pressing the `+` button in the BREAKPOINTS panel of the `Run and Debug` view in the sidebar and entering the function name. Function breakpoints are shown with a red triangle in the BREAKPOINTS section.

# %% [markdown]
# ### [Debugging from the command line](https://code.visualstudio.com/docs/python/debugging#_command-line-debugging)
# Resources
# - https://github.com/microsoft/debugpy
# - https://pypi.org/project/debugpy-run/: Normally, you have to edit the configuration each time when CLI arguments are changed. With this tool you don't.

# %% [markdown]
# #### Providing command line arguments to a program that should be debugged
# - It should be possible to add arguments when the debugger is run via the command line
# - However, I did not succeed to start the debugger from the command line as explained [here](https://code.visualstudio.com/docs/python/debugging#_command-line-debugging) (The problem is that the debugger does not attach)
# - If you start the debugger using VS Code as explained before, you can provide arguments to the program by using the field `args` in the configuration
# - ~~Note that the documentation says that one should use the field [`pythonArgs`](https://code.visualstudio.com/docs/python/debugging#_pythonargs), but this throws an error for me. ~~
# - ~~On the other hand, the last note of [initialize_configurations](https://code.visualstudio.com/docs/python/debugging#_initialize-configurations) the documentation says that `args` should be used~~
# - ~~Other stackoverflow sources also indicate that `args` is the correct field.~~
# - These sources ([here](https://stackoverflow.com/a/70511468) and [here](https://stackoverflow.com/a/73610759)) state that you may have to add the entry `"purpose": ["debug-in-terminal"]`, but for me it was not necessary
# - Note that you must not use spaces in `args`, e.g., use `"args": ["--key1", "value1", "value2", "--key2", "value3", "value4"`] to pass the arguments `--key1 value1 value2 --key2 value3 value4`, see [here](https://stackoverflow.com/a/51244649)
#
#

# %% [markdown]
# ## Using VS Code to debug a notebook

# %% [markdown]
# - If you are using VS Code to work with notebooks you can also debug cells
# - To do so, select `Jupyter: Debug Cell` from the command palette

# %% [markdown]
# ## Real case example: Debugging https://gitlab.p7s1.io/ent-bi-data-science/ga_vs_walle_report/-/issues/21

# %% [markdown]
# # Unfinished
# The following sections are work in progress

# %% [markdown]
# Resources:
# - https://docs.python.org/3/library/pdb.html
# - Resources in 1.1
# - Notes in the section `debug` of 3_data_science/knowledge/0_tools/python_notizen.docx

# %% [markdown]
# ## Using pdb

# %% [markdown]
# ### Interactive IPython/Jupyter sessions
# - If you have installed ipython/jupyter, you also have installed `ipdb`. 
# - When 

# %% [markdown]
# #### Post mortem
# - This is probably the most useful way to start a debugger
# - Use `%debug` to start an `ipdb` debugger for the last exception that has been raised
# - Use `%pdb%` onece to always start an `ipdb` debugger every time right after an exception has been raised. Use `%pdb` again to deactivate.

# %%
c

# %%
%debug

# %%
#### Interactive
- Skipped, because


# %% code_folding=[]
def sum_(a, b):
    # breakpoint()
    return a + b

sum_(1, 2)

# %%
import pdb

pdb.runeval("sum_(1, 2)")

# %%
python -m debugpy --listen 8887 illustrate_debugging.py 2 supplies 2, see also the last note of https://code.visualstudio.com/docs/python/debugging#_basic-debugging

python -m debugpy --listen 8887 --wait-for-client illustrate_debugging.py 2, supplies 2, but hangs, I have to attach?

# %% [markdown]
#
#
#

# %% [markdown]
# ## How to debug?

# %%
# importing pdb
import pdb
  
# make a simple function to debug
def sum(a, b):
    if b == 2:
        b = 3
    return a + b


# %%

# %%
pdb
 It supports setting (conditional) breakpoints and single stepping at the source line level, inspection of stack frames, source code listing, and evaluation of arbitrary Python code in the context of any stack frame. It also supports post-mortem debugging and can be called under program control.

# %%
## Using it from an interactive session

# %%
## Using a debugger from the co

# %% [markdown]
# # Debugger
# - ipdb is a nice debugger but it has some problems from the command line
# - I use pdb from the CLI and then maybe embed an IPython Session
# - But when an IPython Session is active it may be useful to use %run so that everything defined in the script is then available in the IPython Session
#
#
# https://docs.python.org/3/library/pdb.html
# https://stackoverflow.com/a/38983557
#
# https://pypi.org/project/ipdb/

# %% [markdown]
# ## Enter the debugger at a specifc line
# - https://stackoverflow.com/a/33808301

# %%
# enter the debugger at line 376 with arguments for the script
python3 -m pdb -c "unt 376" append_data_to_table.py --test-run 2023-04-27 2023-04-27
# python3 -m pdb -c "b 3" -c c append_data_to_table.py --test-run 2023-04-27 2023-04-27 has the same effect
# use ipython
ipython -i -c "%run -d my_script.py" -> check
# ChatGPT: In this command, ipython starts an interactive IPython session, -i tells IPython to run in interactive mode, and -c specifies a command to run in IPython. The command that we pass to IPython is %run -d my_script.py, which tells IPython to run the script my_script.py with debugging enabled (-d flag).


ipython -i -c "%run -d -b 376 append_data_to_table.py --test-run 2023-04-27 2023-04-27" 
starts at the first line and then waits, but breakpoint is set at line 376

# %%


python -m pdb -c "unt 376" -c c your_script.py

# %% [markdown]
# ## interact and embed
# - Useful if I want to execute multi-line statements etc.
# https://stackoverflow.com/questions/5967241/how-to-execute-multi-line-statements-within-pythons-own-debugger-pdb
#
# how to quit?
#
# start ipython session from python?

# %%
### embed IPython session
import IPython
IPython.embed() # useful for multiline statements
exit # go back to the debugger

# %%
## how to start an interactive session when the debugger has ended

# %%
# Pandas
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_clipboard.html
infer_dtypes
