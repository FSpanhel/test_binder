# ---
# jupyter:
#   jupytext:
#     comment_magics: false
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python [conda env:dsc]
#     language: python
#     name: conda-env-dsc-py
# ---

# %% [markdown]
# The history of notebooks:
#     
# Taken from https://florianwilhelm.info/2018/11/working_efficiently_with_jupyter_lab/
#
# In 2001 Fernando Pérez was quite dissatisfied with the capabilities of Python’s interactive prompt compared to the commercial notebook environments of Maple and Mathematica which he really liked. In order to improve upon this situation he laid the foundation for a notebook environment by building IPython (Interactive Python), a command shell for interactive computing. IPython quickly became a success as the REPL of choice for many users but it was only a small step towards a graphical interactive notebook environment. Several years and many failed attempts later, it took until late 2010 for Grain Granger and several others to develop a first graphical console, named QTConsole which was based on QT. As the speed of development picked up, IPython 0.12 was released only one year later in December 2011 and included for the first time a browser-based IPython notebook environment. People were psyched about the possibilities IPython notebook provided them and the adoption rose quickly.
#
# In 2014, Project Jupyter started as a spin-off project from IPython for several reasons. At that time IPython encompassed an interactive shell, the notebook server, the QT console and other parts in a single repository with the obvious organisational downsides. After the spin-off, IPython concentrated on providing solely an interactive shell for Python while Project Jupyter itself started as an umbrella organisation for several components like Jupyter notebook and QTConsole, which were moved over from IPython, as well as many others. Another reason for the split was the fact that Jupyter wanted to support other languages besides Python like R, Julia and more. The name Jupyter itself was chosen to reflect the fact that the three most popular languages in data science are supported among others, thus Jupyter is actually an acronym for Julia, Python, R.
#
# But evolution never stops and the source code of Jupyter notebook built on the web technologies of 2011 started to show its age. As the code grew bigger, people also started to realise that it actually is more than just a notebook. Some parts of it rather dealt with managing files, running notebooks and parallel workers. This eventually led again to the idea of splitting these functionalities and laid the foundation for JupyterLab. JupyterLab is an interactive development environment for working with notebooks, code and data. It has full support for Jupyter notebooks and enables you to use text editors, terminals, data file viewers, and other custom components side by side with notebooks in a tabbed work area. Since February 2018 it’s officially considered to be ready for users and the 1.0 release is expected to happen end of 2018.
#     

# %% [markdown]
# # tips

# %% [markdown]
# Access a cell’s result
# Surely you have experienced this facepalm moment when your cell with long_running_transformation(df) is finally finished but you forgot to store the result in another variable. Don’t despair! You can just use result = _NUMBER, e.g. result = _42, where NUMBER is the execution number of your cell, e.g. In [42], to access and save your result. An alternative to _NUMBER is Out[NUMBER].

# %% [markdown]
# Avoid unintended outputs
# Using ; in Python is actually frowned upon but in Jupyterlab you can put it to good use. You surely have noticed outputs like <matplotlib.axes._subplots.AxesSubplot at 0x7fce2e03a208> when you use a library like Matplotlib for plotting. This is due to the fact that Jupyter renders in the output cell the return value of the function as well as the graphical output. You can easily suppress and only show the plot by appending ; to a command like plt.plot(...);.

# %%
If we use an IDE for development we will run into an obvious problem. How can we modify a function in our package and have these modifications reflected in our notebook without restarting the kernel every time? At this point I want to introduce you to your new best friend, the autoreload extension. Just add in the first cell of your notebook

%load_ext autoreload
%autoreload 2
and execute. This extension reloads modules before executing user code and thus allows you to use your IDE for development while executing it inside of JupyterLab.

However, this does not work every time and can produce weird errors.
Sometimes it is better to restart the kernel or used importlib.reload

# %%
Basic Intro How to Use Jupyter Notebook in 2020: A Beginner’s Tutorial (dataquest.io) (not relevant for me, only if you haven’t worked with notebooks before)
