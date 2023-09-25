# In these notes I have pasted text that build the basis for some cells in the corresponding notebooks that I've created.
These notes might be messy and are just here so that I can read them in the next year to better understand my notebook inspirations.

Conda vs. Pip vs. Venv — What’s the Difference?
Before we get started, some of you might be wondering what the difference is between conda, pip, and venv.
I’m glad you asked. We can’t put it any better than this: pip is a package manager for Python. venv is an environment manager for Python. conda is both a package and environment manager and is language agnostic.
Whereas venv creates isolated environments for Python development only, conda can create isolated environments for any language (in theory).
Whereas pip only installs Python packages from PyPI, conda can both
•	Install packages (written in any language) from repositories like Anaconda Repository and Anaconda Cloud.
•	Install packages from PyPI by using pip in an active Conda environment.


This highlights a key difference between conda and pip. Pip installs Python packages whereas conda installs packages which may contain software written in any language. For example, before using pip, a Python interpreter must be installed via a system package manager or by downloading and running an installer. Conda on the other hand can install Python packages as well as the Python interpreter directly.

https://stackoverflow.com/a/21008900

https://stackoverflow.com/a/68897551

Do we still need conda when we have docker?
And while Docker is nice for deployment, developing software in it is often asking for headaches and it can easily end up complicating the development workflow unnecessarily.
 They also can be overkill and an unnecessary complication many times.
Maybe docker replace virtual env but not the package management

Windows is not the standard to develop Data Science projects (and most software development tasks), so you can expect lots of things to not work as smoothly as on Linux.


Some of the following notes were extracted from https://www.reddit.com/r/Python/comments/xhbhbh/venv_or_anaconda/?utm_source=share&utm_medium=ios_app&utm_name=iossmf


# Why conda


When working with complex Python environments, I would recommend using conda for the following reasons:

- Ability to select a specific Python interpreter version for a specific project.
- Conda can package more than just Python libraries
- Conda environment directories are more-or-less self-contained. They are not dependent on any system python libraries, nor conda itself. This makes them great for usage in Docker because I can just move a working conda environment to a new minimal Linux container like debian-slim with multi-stage builds (yes, I think conda is great for Docker production deployments).
- Conda is more reliable in my experience. This is because the above three points: ability to select specific Python version, ability to have non-Python packages, and being self-contained make it more consistent and reproducible.
- Much fewer issues when having dependency conflicts, conda will complain and fail installing an environment with issues.
- If you are working with neural network libraries like PyTorch that need a GPU/CUDA you can just install the correct CUDA version in your environment from conda.
- When you want to use conda I would actually recommend using mamba instead. Mamba is a reimplementation of conda and is much faster at resolving the environments. I can be used as a drop-in of conda and is fully compatibly with it afaik.
- Btw, when using conda (besides using mamba), I would recommend not using the default channel in a commercial setting due to licensing issues (unless you're paying for the commercial version). Something like conda-forge should be fine.
- If you are not creating complex Python environments (like is common in a lot of machine-learning/data-science settings). I would recommend to just stick with the System-Python/Venv until you run into issues with complex python environments.




My favorite is conda for several reasons.
- First of all conda is a package manager of the Anaconda distribution and allows
you to install more than just Python packages.
- Anaconda is more like a whole operation system coming with packages for Python, R and C/C++ system libraries like libc.
- From this point of view it’s much more than what virtualenv provides, since conda will also install system libraries like glibc if need be.
- Also the Python interpreter itself is installed separately into an isolated environment and thus independent of the one provided by your system. This makes it possible to easily pin down even the Python version of your environment.
- The tool pyenv allows you to do the same within the virtualenv ecosystem but conda feels just more integrated and gives a unified approach.
- In total, conda allows for much more fined-grained control of what is going on in your virtual environment than virtualenv with less side effects induced by your system.

For these reasons conda is much more common than virtualenv in the field of data science, thus we will use it in this tutorial

……………………………………………

## Why conda
- Conda installs Python packages as well as the Python interpreter directly.
    - Since pip is a Python program, a global Python interpreter must be installed before pip can be used.
- Recognized and supported by a lot of third-party packages
- Multiple Python versions (only one for venv)
- PyPi has been a target for malicious packages.
-  can isolate such as CUDA versions (for deep learning)
- It covers the functionality provided by venv, virtualenv, pipenv, pyenv, and other Python-specific package managers

https://stackoverflow.com/a/21008900
- (Only) installs binaries. (conda build can bild packages from source)
    - Since pip installs from source, it can be painful to install things with it if you are unable to compile the source code (this is especially true on Windows, but it can even be true on Linux if the packages have some difficult C or FORTRAN library dependencies). conda installs from binary, meaning that someone (e.g., Continuum) has already done the hard work of compiling the package, and so the installation is easy.
    - Part of the core philosophy of conda is that it leaves the potentially difficult compilation step to the package maintainer.
- Conda is not Windows-centric, but on Windows it is by far the superior solution currently available when complex scientific packages requiring compilation are required to be installed and managed.
- How it was 7 years ago without conda... https://stackoverflow.com/questions/28413824/installing-numpy-on-windows
- Its very package dependent. Pure Python packages arent a problem. If the package includes C code that needs to be compiled though and they havent included a compiled wheel for your OS, then you need to have the tools to compile it.
- Some of the libraries can be a PAIN IN THE ASSSSSS to install properly because they need to be built. Conda solves 99% of those. Its ALOT better now then 10 years ago but it can still suck depending on your computer. No use for Conda outside of (data) science though just use pip and venv.

I want to weep when I think of how much time I have lost trying to compile many of these packages via pip on Windows, or debug failed pip install sessions when compilation was required.
        -  Historically, pip compiled everything from source but did not support binary packages
        -  If a [wheel](https://realpython.com/python-wheels/) is available, pip install (--use-wheel) <package> will install a built package
        - And of course pip install mostly doesn't work either on windows if your build environment isn't set up exactly right
        - wheels have weaknesses that Conda's binaries address. https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/#Myth-#6:-Now-that-pip-uses-wheels,-conda-is-no-longer-necessary
- Compiled binaries are important because many packages are mixed Python/C/other with third-party dependencies and complex build chains. They MUST be distributed as binaries to be ready-to-use.
- Pure python packages have always worked fine with any of these packagers. The troubles were with not-only-Python packages.
- https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/#Myth-#6:-Now-that-pip-uses-wheels,-conda-is-no-longer-necessary
    - One difficulty which drove the creation of Conda was the fact that pip could distribute only source code, not pre-compiled binary distributions, an issue that was particularly challenging for users building extension-heavy modules like NumPy and SciPy. After Conda had solved this problem in its own way, pip itself added support for wheels, a binary format designed to address this difficulty within pip. With this issue addressed within the common tool, shouldn't Conda early-adopters now flock back to pip?
- It covers the functionality provided by venv, virtualenv, pipenv, pyenv, and other Python-specific package managers

……………..

honestly I havent had many problems with later python versions on Linux
systems when using data science packages via pip/venv. The main challenge
seems to be windows because getting the build tools on windows is a pain (and thus was born the unofficial windows binaries).

Personally, I'm a fan of pip/venv. Less dependencies, less mess.

If you are not creating complex Python environments (like is common in a lot of machine-learning/data-science settings).
I would recommend to just stick with the System-Python/Venv until
you run into issues with complex python environments.

-----------------………
- Dependency resolution
- https://www.anaconda.com/blog/understanding-conda-and-pip: Pip and conda also differ in how dependency relationships within an environment are
fulfilled. When installing packages, pip installs dependencies in a recursive, serial loop.
No effort is made to ensure that the dependencies of all packages are fulfilled simultaneously.
This can lead to environments that are broken in subtle ways, if packages installed earlier in the
order have incompatible dependency versions relative to packages installed later in the order. In contrast,
conda uses a satisfiability (SAT) solver to verify that all requirements of all packages installed in an environment
are met. This check can take extra time but helps prevent the creation of broken environments. As long as package metadata
about dependencies is correct, conda will predictably produce working environments.
- conda includes a true dependency resolver, a component which pip [had been lacking or currently lacks (?)](https://github.com/pypa/pip/issues/988)

# Archive: TODO
The package nb_conda_kernels will automatically detect different conda environments with notebook kernels and automatically register them.
## sys.path
Python is set up to find these modules by adding the relevant path to sys.path. During initialization, Python automatically imports the site module, which sets the defaults for this argument.

The paths that your Python session has access to in sys.path determine which locations Python can import modules from.

If you activate your virtual environment and enter a Python interpreter, then you can confirm that the path to the standard library folder of your base Python installation is available:
- Note that the directory where the pandas package is located in our environment is not contained in the PATH variable.
When a module(a module is a python file) is imported within a Python file,
the interpreter first searches for the specified module among its built-in modules.
If not found it looks through the list of directories(a directory is a folder
that contains related modules) defined by sys.path.
- Instead, Python uses its own environment variables to determine which pandas package should be imported.
- The sys module provides access to some of the environment variables that are used by the interpreter.
- The search path of Python

sys.path is a built-in variable within the sys module.
It contains a list of directories that the interpreter will search in for the required module.




To modify the paths before starting Python, you can modify the PYTHONPATH environment variable.
import path
A list of locations (or path entries) that are searched by the
path based finder for modules to import. During import, this list of
locations usually comes from sys.path, but for subpackages it may also come from the parent package’s __path__ attribute.
[Official doc of sys.path](https://docs.python.org/3/library/sys.html#sys.path):
- A list of strings that specifies the search path for modules.
- Initialized from the environment variable PYTHONPATH, plus an **installation-dependent default**.
- As initialized upon program startup, the first item of this list, path[0],
  is the directory containing the script that was used to invoke the Python interpreter.
- If the script directory is not available (e.g. if the interpreter is invoked interactively or if the script is read from standard input), path[0] is the empty string, which directs Python to search modules in the current directory first.
- Notice that the script directory is inserted before the entries inserted as a result of PYTHONPATH.
- A program is free to modify this list for its own purposes.
Resources:
    - https://realpython.com/python-virtual-environments-a-primer/#how-can-you-work-with-a-python-virtual-environment
    - https://towardsdatascience.com/a-guide-to-conda-environments-bc6180fc533#e814
    - https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/
    - https://www.devdungeon.com/content/python-import-syspath-and-pythonpath-tutorial
