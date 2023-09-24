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

# %% [markdown]
# # What characterizes good Data Science code?

# %% [markdown]
# In my humble opinion the following 
# 1. Correct: The code should do what it is supposed to do.
# 2. Readable and Understandable: [More time is spent reading code than writing.](https://bayrhammer-klaus.medium.com/you-spend-much-more-time-reading-code-than-writing-code-bc953376fe19)
# 3. Reproducible: In order that Data Science experiments are reproducible we have to version code, data and models.
# 4. Portable, Scalable and Resuable: Code should be runnable in different environments (e.g., no hard-coded paths), adding new features should be possible, components should be resuable.
# 5. Fast execution.
# 6. Elegant.
#
#
# **Good coding practices**
# - KISS
# - DRY
# - YAGNI

# %% [markdown]
# **What should you generally consider?** 

# %% [markdown]
# - modularize
# - use jupyter notebooks mainly for exploration and presentation/communication
# - adopt SE principles 
# - use version control and make code reviews
# - document your code 
# - make code self-containable 
# - do not hard code paths 
# - use classes when appropriate and only when appropriate (python is not java)
# - nicht das rad neu erfunden, use existing libraries 
# - wenn man selbst was schreibt dann versuchen die api an bestehendes anzupassen (scikit-learn), auch wenn das dann vll selber aufwändiger ist damit es damit funktioniert, der vorteil damit aber ist das andere dann schnell damit arbeiten kann (siehe boost projekt), den vorteil dafrf man nicht unterschätzen
# - Use tool that help you (linting, formatting, pre-commits, IDEs...)
# - Use virtual environments and Git
# - whenever possible, a function should be pure, use methods if you want to alter the state of an object

# %%
How can I learn how to write clean code? Code (Do it, fail repeat) and code reviews.

# %%
https://www.thoughtworks.com/insights/blog/coding-habits-data-scientists

https://goodresearch.dev/decoupled.html -> wonderful source!
https://goodresearch.dev/tidy.html

https://www.reddit.com/r/datascience/comments/yphayx/pointers_to_write_clean_code_for_production/?utm_source=share&utm_medium=ios_app&utm_name=iossmf

# %%
https://confluence.p7s1-tech.com/display/DF/writing+functions

# %%
# Mutability 
https://www.geeksforgeeks.org/is-python-call-by-reference-or-call-by-value/
https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/

# %% [markdown]
#

# %% [markdown]
# # Formatter -> zu Python

# %% [markdown]
# Memes:
# https://www.reddit.com/r/ProgrammerHumor/comments/xxv8sz/perfect_situation/?utm_source=share&utm_medium=ios_app&utm_name=iossmf


# %%



# %%
