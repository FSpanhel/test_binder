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

# %% slideshow={"slide_type": "notes"}
import os

from dsc.notebook import embed_website

# %% [markdown] slideshow={"slide_type": "slide"}
# # Intro
# <div align="left">
# <img src="https://imgs.xkcd.com/comics/git.png" alt="Git..." width=600/>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# <div align="left">
# <img src="./figures/git_intro.png" alt="Dropbox" width=1200/>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Prerequisites and scope
# - It is assumed that you know the **basics of Git**
#     - Adding and committing changes to Git
#     - Working with remotes, e.g., the difference between fetch and pull
#     - Working with branches, e.g., checkout branches and merging
# - If you lack some knowledge or want to deepen you knowledge please have a look at the [Resources](#Resources)
# - This chapter starts with **minor notes on Git that might be helpful**.
# - The focus of this chapter is on **Git rebase** to obtain a concise commit history.
#     - A concise commit history is helpful if you work collaboratively.
#     - It will also make it easier for meto track and review your progress on the project work.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## How did Git get its name?

# %% [markdown] slideshow={"slide_type": "-"}
# Source: https://initialcommit.com/blog/How-Did-Git-Get-Its-Name
#
#
# - When Linus Torvalds made his initial commit of Git's code on April 7th 2005, he supplied the commit message:  
#     ```Initial revision of "git", the information manager from hell```
#     
# - In this commit, he included a file called README. The first paragraph in this file reads:
#
# ```
# GIT - the stupid content tracker
#
# "git" can mean anything, depending on your mood.
#
#  - random three-letter combination that is pronounceable, and not 
#    actually used by any common UNIX command.  The fact that it is a
#    mispronunciation of "get" may or may not be relevant.
#  - stupid. contemptible and despicable. simple. Take your pick from the 
#    dictionary of slang.
#  - "global information tracker": you're in a good mood, and it actually
#    works for you. Angels sing, and a light suddenly fills the room. 
#  - "goddamn idiotic truckload of sh*t": when it breaks
#
# This is a stupid (but extremely fast) directory content manager.  It  
# doesn't do a whole lot, but what it _does_ do is track directory
# contents efficiently.
# ```

# %% [markdown] slideshow={"slide_type": "subslide"}
# - First commit of Git: https://bitbucket.org/jacobstopak/baby-git/src/master/
# - Written in the C programming language and consists of about 1,000 lines of code and a total of 7 commands

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Master vs. main
#
# - Historically, Git has named the initial branch master.
#
# - The master/slave terminology has a [long history in computing](https://en.wikipedia.org/wiki/Master/slave_(technology)), especially in reference to hardware such as disk drives. 
# - Other version control systems such as BitKeeper, a predecessor to Git, have used this terminology.
# - This terminology is somewhat outdated as it is associated with colonialism.
# - Current versions of Git (>= 2.28) display the following message when you create a new repository using git init:  
#     ```Using 'master' as the name for the initial branch. This default branch name is subject to change. To configure the initial branch name to use in all of your new repositories, which will suppress this warning, call: git config --global init.defaultBranch <name> Names commonly chosen instead of 'master' are 'main', 'trunk' and 'development'. The just-created branch can be renamed via this command: git branch -m <name>```
# - Git maintainers are [actively working](https://lore.kernel.org/git/pull.656.v4.git.1593009996.gitgitgadget@gmail.com/) toward a permanent change for the default name from master to main
#

# %% [markdown] slideshow={"slide_type": "subslide"}
# **Git providers**
# - Starting [October 1 2020](https://github.blog/changelog/2020-10-01-the-default-branch-for-newly-created-repositories-is-now-main/), the initial branch name of **new GitHub repositories** is main.
# - Since [May 24 2021](https://about.gitlab.com/blog/2021/03/10/new-git-default-branch-name/), the initial branch the name of **new GitLab repositorries** is main.
# - Thus, any new project that its hosted on GitHub or GitLab and expects a master branch might run into problems.
# - Therefore, I recommend to rename the initial branch to main if you use git init and not get clone.

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Git 2.28, released in July 2020, added init.defaultBranch to the configuration
# - This allows to name the name of the default branch other than master, e.g.,  
#     ```git config --global init.defaultBranch main ```
# - Alternatively, one can manually rename master each time you have initialized a repo and made the first commit using  
# ```git branch -m main```  
# - Or just run  ```git checkout -b main``` after initializing a repo but before the first commit
# to switch the unborn branch name to main
# - For renaming a remote branch see [here](https://stackoverflow.com/questions/30590083/how-do-i-rename-both-a-git-local-and-remote-branch-name).

# %% [markdown] slideshow={"slide_type": "slide"}
# ## GUIs and tools that facilitate the working with Git
# - While I think it is very useful if one can perform essential Git operations in the terminal, there are tools that make working with Git and learning Git much more enjoyable. 
# - In particular, a tool might come in very handy, if you want to
#     - Investigate the commit history
#     - Compare changes between commits
#     - Compare differences between your working directory and the current commit
#     - Merge commits
#     - Want to visualizes commits across different branches  
#
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### General GUIs
# - [GitKraken](https://www.gitkraken.com/)
# - [SourceTree](https://www.sourcetreeapp.com/)
# - ...

# %% [markdown] slideshow={"slide_type": "slide"}
# ### VSCode
# - VSCode has a fairly minimal Git integration by default.
# - But there are a [lot of extensions](https://dev.to/jamieswift90/the-best-vs-code-extensions-to-supercharge-git-yes-there-s-more-than-gitlens-4588) to make using Git more comfortable
# - In particular, [GitLens](https://gitlens.amod.io/) and [GitGraph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) are very helpful (more information on the next slides)

# %% [markdown] slideshow={"slide_type": "subslide"}
#     
# **GitLens** (by GitKraken)
# - GitLens is with over 17 millions installs (September 2022) the de facto standard extension for working with Git in VS Code. 
#     - Revision navigation
#     - Current line blame
#     - Side Bar views
#     - interactive rebase editor
#     - Commit Graph (only + version)
# - Resources:
#     - [Official website](https://gitlens.amod.io/)
#     - [Tips on utilizing features](https://www.reddit.com/r/vscode/comments/ueydoi/gitlens_is_by_far_my_favorite_vs_code_extension/?utm_source=share&utm_medium=ios_app&utm_name=iossmf)

# %% [markdown] slideshow={"slide_type": "subslide"}
# **GitGraph**
# - GitGraph (over 3 millions installs September 2022) provides a commit graph of your repository, and easily performs Git actions from the graph. 
# - It is very useful if you don't have the GitLens +.
# - Note that you often have to manually refresh GitGraph so that the correct graph is shown (!).
# - [Download extension](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
#
# **GItHistory**
# - An alternative to GitLens with less features.
# - [Download extension](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## How to change the default editor
# - The default editor that Git uses is Vim which you probably don't want to use. 
# <div align="left">
# <img src="./figures/vim.png" alt="Vim" width=600 height=100/>
# <div/>
# <div align="left">
# <div/>
# - To change the default editor run in the terminal
#
# ```bash
# git config --global core.editor 'code --wait' # code (for VSCode), or e.g., nano, pycharm or full path to executable
# ```
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Git alias
# - Defining Git aliases shortens frequently used commands and simplifies long commands with many options.
# - Git aliases are created through the git config command or Git configuration files.
# - For instance, to globally create the alias git st for git status
#     - Run ```git config --global alias.st 'status'``` in the terminal
#     - Or edit ~/.gitconfig (on unix-like systems)
# - You can also use shell commands in aliases using !, e.g., ```git config --global alias.list '!ls -a | head -n 4'```
# - You can also create aliases in your favorite shell using 'alias gs='git status', however
#     - The alias is bound to the shell.
#     - May pollute shell commands.

# %% [markdown] slideshow={"slide_type": "subslide"}
# **Some useful git aliases**
#
# ```bash
# # show all aliases
# git config --global alias.alias "! git config --get-regexp ^alias\. | sed -e s/^alias\.// -e s/\ /\ =\ /";
#
# # config
# git config --global alias.clv 'config --list --show-origin'; # verbose overview of config
#
# # status
# git config --global alias.st 'status';
# git config --global alias.stc 'status -sb'; # concise git status, does not show untracked files
# git config --global alias.ftst '!git fetch && git status';  # in principle, you should always fetch before getting the status
#
# # log
# git config --global alias.lo 'log --oneline'; # concise log
# git config --global alias.lc 'log -1 HEAD --stat'; # details about the last commit 
# git config --global alias.lg 'log --graph --oneline --decorate'; # simple and concise log graph which also shows branches
# git config --global alias.lgv "log --graph --pretty='format:%C(red)%d%C(reset) %C(yellow)%h%C(reset) %cd %C(green)%aN%C(reset) %s'  --date=format:'%a %y-%m-%d %H:%M'"; # verbose log graph with date and author
# ```

# %% [markdown] slideshow={"slide_type": "subslide"}
# **Some useful git aliases cont'd**
# ```bash
# # changing
# git config --global alias.cm 'commit -m';
# git config --global alias.rbi 'rebase -i';
# git config --global alias.cmad 'git commit --amend --date "$(date)"';  # set date of current commit to today, useful for rebase
#
# # checkout and branches
# git config --global alias.cob 'checkout -b';
# git config --global alias.com 'checkout main';
# git config --global alias.br branch;
# git config --global alias.brr 'branch -r';
# git config --global alias.co checkout;
# git config --global alias.brst "branch --format='%(HEAD) %(color:yellow)%(refname:short)%(color:reset) - %(contents:subject) %(color:green)(%(committerdate:relative)) [%(authorname)]' --sort=-committerdate"; # show last commit of each branch
# git config --global alias.brdm "!git branch --merged | grep -v '*' | xargs -n 1 git branch -d"; # delete all merged branches
#
# # merge
# git config --global alias.mg 'merge';
# git config --global alias.mgff 'merge --ff-only';  # abort if no fast-forward merge is possible 
# git config --global alias.mgnoff 'merge --no-ff'; # always perform 3-way merge
# git config --global alias.mgi 'merge --no-ff --no-commit'; # 'interactive' 3-way merge, i.e., add merged files to the staging are but do not commit, useful for inspecting changes (note that --no-commit has no no effect if --no-ff is ommitted and ff is possible)
# git config --global alias.ma 'merge --abort';
# git config --global alias.mc 'merge --continue';
#
# # remote
# git config --global alias.ft 'fetch -p';  # fetch and prune 
# git config --global alias.pl 'pull'; 
# git config --global alias.plff 'pull --ff-only'; # abort if no fast-forward merge is possible
# git config --global alias.plr 'pull --rebase'; # do not merge but rebase after fetch
# git config --global alias.ipl 'pull --no-ff --no-commit'; # inspect and further tweak the merge result before merging (it is not recommend to finish the merge if a ff would be possible due to the creation of a new commit, use git merge --abort to abort the merge)
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Resources
# - [One of best introductions to using Git by Atlassian](https://www.atlassian.com/git/tutorials/what-is-version-control)
# - [Official website](https://git-scm.com/about)
# - [The pro Git book](https://git-scm.com/book/en/v2)
# - [A visual Git reference](https://marklodato.github.io/visual-git-guide/index-en.html)
# - Interactive games:
#     - https://ohmygit.org/: needs installation
#     - https://learngitbranching.js.org: very nice to learn branching
# - [Cheat sheet](https://wac-cdn.atlassian.com/dam/jcr:e7e22f25-bba2-4ef1-a197-53f46b6df4a5/SWTM-2088_Atlassian-Git-Cheatsheet.pdf?cdnVersion=543)

# %% slideshow={"slide_type": "subslide"}
embed_website("https://learngitbranching.js.org/?locale=de_DE&NODEMO")

# %% [markdown] slideshow={"slide_type": "slide"}
# # Rebase
# - With rebase you can **use another branch or commit as the new base** for your work.
# - Like merge it **integrate changes from one branch into another branch** - just in a very different way
# - In combination with fast-forward merges, this 
#     - Allows for a linear commit history 
#     - Eliminates the possibly superfluous 3-way merge commit (depends on the use case and preferences)
#     - Makes it easier to navigate your project with commands like git log or git bisect.
# - If used **interactively**, rebase allows you to **rewrite history and tidy up commits** before integrating them in another branch.
# - Both points together help to **obtain a concise commit history** for your project. 
# - However, you should rebase only on your own private branch but not on public branches, see the [golden rule of rebasing](https://www.atlassian.com/git/tutorials/merging-vs-rebasing#the-golden-rule-of-rebasing).
# - To illustrate the use of rebase, let's consider a motivating example.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Motivation

# %% [markdown] slideshow={"slide_type": "subslide"}
# Assume your main branch is '_target' and contains the main application for your very secret project.
# ```bash
# git checkout -b _target &&
# echo "print(1)" > main.py &&
# git add main.py && git commit -m "add main.py";
# ```

# %% [markdown] slideshow={"slide_type": "fragment"}
# To create a module for your main program you checkout the branch '_messy_branch'.
# ```bash
# git checkout -b _messy_branch &&
# echo 'print("this is the frist line")' > module_a.py &&
# git add module_a.py && git commit -m "add module_a.py";
# ```

# %% [markdown] slideshow={"slide_type": "fragment"}
# You recognize the spelling error in module_a.py and correct it.
# ```bash
# rm messy_readme.md &&
# echo 'print("this is the first line")' > module_a.py &&
# git add module_a.py && git commit -m "fix spelling error in module_a.py";
# ```

# %% [markdown] slideshow={"slide_type": "fragment"}
# After some elaborate thinking you put more details to module_a.py.
# ```bash
# echo 'print("this is the second line")' >> module_a.py &&
# git add module_a.py && git commit -m "add more details to module_a.py";
# ```

# %% [markdown] slideshow={"slide_type": "subslide"}
# In the meantime you have to update main.py on the branch _target.
# ```bash
# echo "print(2)" >> main.py &&
# git add main.py && git commit -m "update main.py";
# ```

# %% [markdown] slideshow={"slide_type": "-"}
# Since the module_a.py depends on main.py you have to consider its update on '_messy_branch'.
#
# For this purpose, you merge the '_target' branch into '_messy_branch':
# ```bash
# git merge _target
# ```
# Your text editor opens and displays the following file:

# %% [markdown] slideshow={"slide_type": "-"}
# <div align="left">
# <img src="./figures/merge_conflict.png" alt="merge conflict" width=1200/>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "subslide"}
# You edit (or don't edit) the merge message and perform the merge.   
#
# You finish module_a.py accordingly,
# ```bash
# echo 'print("this is the third line")' >> module_a.py &&
# git add module_a.py && git commit -m "consider update of main.py in module_a.py";
# ```
# and merge your branch into '_target' and delete the obsolete '_messy_branch'.
# ```bash
# git checkout _target;
# git merge _messy_branch;
# git branch -d _messy_branch;
# ```
#
# <br>
#
# Note:  
# - You can reproduce these commits by running
# ```python3 -m dsc.version_control.git merge merge``` in the terminal.  
# - To undo all changes use ```python3 -m dsc.version_control.git reset```

# %% [markdown] slideshow={"slide_type": "subslide"}
# Using  GitGraph in VSCode (or ```git log --graph --oneline --decorate```) we can investigate the 
# the commit history of '_target' which now looks as follows.

# %% [markdown] slideshow={"slide_type": "-"}
# <div align="left">
# <img src="./figures/r_0_messy.png" alt="messy commit history" width=1000 />
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "fragment"}
# How do we read this history?
# - Three squential commits (blue) were based on commit "add main.py"
# - One commit (pink) was also based on commit "add main.py"
# - A merge occured: _target (pink) was merged into _messy_branch (blue)
# - As a result, both branches are identical after the merge
# - Since _messy_branch is missing from the history it has been removed
#

# %% [markdown] slideshow={"slide_type": "slide"}
# What's not so nice about this commit history?

# %% [markdown] slideshow={"slide_type": "-"}
# <div align="left">
# <figcaption>A: Messy commit history with merge</figcaption>
# <img src="./figures/r_0_messy.png" alt="messy commit history" width=1000/>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "fragment"}
# - The history does not really reflect the essence of the changes, namely:
#     - main.py was added and updated
#     - module_a.py was created on the basis of the current main.py
# - The commit "Merge branch '_target' into _messy_branch" is distracting 
# - The fix of spelling errors and the adding of more detail is also superfluous 
#

# %% [markdown] slideshow={"slide_type": "slide"}
# Wouldn't it be nice if we had a more concise commit history?

# %% [markdown] slideshow={"slide_type": "-"}
# <div align="left">
# <figcaption>B: Clean commit history with merge</figcaption>
# <img src="./figures/r_3_squash_no_ff.png" alt="clean commit history with merge" width=1000/>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "fragment"}
# Or even a commit history without a merge commit?

# %% [markdown] slideshow={"slide_type": "-"}
# <div align="left">
# <figcaption>C: Clean linear commit history</figcaption>
# <img src="./figures/r_3_squash.png" alt="clean linear commit history" width=1000/>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "fragment"}
# Instead of 

# %% [markdown] slideshow={"slide_type": "-"}
# <div align="left">
# <figcaption>A: Messy commit history with merge</figcaption>
# <img src="./figures/r_0_messy.png" alt="messy commit history" width=1000/>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Fast-forward and three-way merge
# - With Git rebase you can rewrite the commit history into a linear commit history by allowing for fast-forward merges.
# - To understand this, let's first discuss the two different merge types in Git.

# %% [markdown] slideshow={"slide_type": "fragment"}
# - In the most frequent use case, git merge is used to combine two branches.
# - Once Git finds a common base commit it integrates the deviating commit sequence of the source branch, i.e., the branch to be integrated, into the current branch:
#     - **Fast-forward**: If there is a linear path from the current branch tip to the source branch tip, Git only has to move (i.e., “fast forward”) the current branch tip up to the tip of the source branch
#     <div align="left">
#     <img src="./figures/merge_ff_0.png" alt="clean commit history with merge" width=600/>
#     <img src="./figures/merge_ff_1.png" alt="clean commit history with merge" width=600/>
#     <div/>
#     <div align="left">
#     <div/>
#     - **3-way**: Otherwise, Git uses the two branch tips and their common ancestor to create a new commit to integrate the source branch into the current branch.
#     - 3-way merge commits differ from other commits in that they have **two parent commits**. 
#     <div align="left">
#     <img src="./figures/merge_0.png" alt="clean commit history with merge" width=600/>
#     <img src="./figures/merge_1.png" alt="clean commit history with merge" width=600/>
#     <div/>
#     <div align="left">
#     <div/>
#
# Figure source: https://www.atlassian.com/git/tutorials/using-branches/git-merge

# %% [markdown] slideshow={"slide_type": "slide"}
# ## (Non-interactive) rebase
# - With rebase you can use another branch as the new base for your work.
# - By rebasing on another branch, you are effectively copying all commits that have taken place on the other branch to your recent branch to create a linear commit history 
# - Because of a linear commit history you can merge your recent branch into the other branch using a fast-forward merge
# - However, you lose the commit message of a 3-way merge and can't see when changes from another branch were incorporated
# - Note that rebasing produces **new commits** 
# <div align="left">
# <img src="./figures/at_rebase_0.png" alt="clean commit history with merge" width=600/>
# <img src="./figures/at_rebase_2.png" alt="clean commit history with merge" width=600/>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Illustration

# %% [markdown] slideshow={"slide_type": "subslide"}
# Let's return to our motivation and to the commit when main.py is updated.
#
# For this purpose, you can run 
# ```python3 -m dsc.version_control.git```
#
# We have the following commit history before integrating the changes of _target into _messy_branch

# %% [markdown] slideshow={"slide_type": "-"}
# <div align="left">
# <img src="./figures/r_0_before_merge.png" alt="Before integrating changes of _target into _messy_branch" width=1000/>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "subslide"}
# - We can now rebase to get a linear commit history and avoid the superfluous merge if we use (on _messy_branch)  
# ```git rebase _target```  
# instead of  
# ```git merge _target```
# - ```git rebase <branch>``` automatically takes the commits in your current working branch and applies them to the tip of the passed branch.
# -  In this case, _messy_branch is rebased on the _target commit ```1609999b``` that has the description "add main.py".
# - Alternatively, you can use ```git rebase 1609999b``` to base the commits in your current working branch on the _target commit ```1609999b```
# - Running ```git rebase _target``` in the terminal yields

# %% [markdown] slideshow={"slide_type": "-"}
# <div align="left">
# <img src="./figures/r_after_rebase.png" alt="After rebasing _messy_branch on _target" width=1000/>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Finishing module_a and merging our commits into _target yields then the following linear commit history.
# - You can also run ```python3 -m dsc.version_control.git rebase merge``` to produce the following commit history.

# %% [markdown] slideshow={"slide_type": "-"}
# <div align="left">
# <img src="./figures/r_1_rebased.png" alt="After rebasing _messy_branch on _target" width=1000/>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "-"}
# - We now have gotten rid of the superfluous merge but still do not have a concise commit history.
# - To get a concise commit history we can use interactive rebasing which we will discuss next.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Interactive rebase
# - An interactive rebase allows you to **rewrite history**. 
# - This allows you to make commits without worrying whether they meanigful enough, you can fix them later with rebase.
# - The only thing other developers will see is your finished commit history, which should be a concise and simple branch history.
# - You can start and interactive rebase using ```git rebase -i <branch/commit>``` which opens the git-rebase-todo file.
# - Note that, in contrast to a non-interactive rebase, it makes sense to use an interactive rebase on a commit of the current branch to rewrite its history.
# - If you do a more complex rebase, I recommend to **backup the branch to be rebased** using ```git branch [<name>]```, where name have the format backup_branch_YYYY_MM_DD.

# %% [markdown] slideshow={"slide_type": "slide"}
# **Options during interactive rebase**  
# - When an interactive rebase is started, the text file git-rebase-todo is opened
# - The file git-rebase-todo lists all commits that are about to be moved to the new base.
# - This listing defines exactly what the branch will look like after the rebase is performed.
#
# - For each commit you can apply one of the following commands 
#     - p, **pick**: use this commit
#     - d, **drop**: remove commit (you can also delete the line of the commit)
#     - r, **reword**: use this commit, but edit its commit message
#     - e, **edit**: temporarily stops the rebase after applying the chosen commit
#         - Makes it possible to edit commits using ```git add``` and ```git commit –amend```.  
#         - Use ```git rebase --continue``` to continue applying other commits.
#     - s, **squash**: include this commit in the previous commit that is considered
#         - The suggested commit message for the folded commit is the combination of the first commit and those with the squash command.
#         - Note that the folded commit is always a new commit with a new SHA
#     - f, **fixup**: like squash, but don't consider its commit message
#     - x, **exec**: run command (the rest of the line) using shell

# %% [markdown] slideshow={"slide_type": "subslide"}
# **Abort and conflicts**
# - To abort the rebase, enter ctrl + c in the terminal and run ```git rebase --abort```.
# - If there are merge errors during rebase the process will stop. 
#     - If you are done resolving the conflicts you can proceed with ```git rebase --continue```.
#     - If you want to start another rebase use ```git rebase --abort``` before!
#     

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Illustration

# %% [markdown] slideshow={"slide_type": "-"}
# Let's return to our motivation and to the commit when main.py is updated.
#
# For this purpose, you can run 
# ```python3 -m dsc.version_control.git```
#
# We have the following commit history before integrating the changes of _target into _messy_branch.

# %% [markdown] slideshow={"slide_type": "-"}
# <div align="left">
# <img src="./figures/r_0_before_merge.png" alt="Before integrating changes of _target into _messy_branch" width=1000/>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# - Instead of merging _target into _messy_branch we can also rebase _messy_branch on _target using  
# ```git rebase -i _target```
# -  Just like for a (non-interactive) rebase,  _messy_branch is rebased on the tip of _messy_branch which is the commit
# with the description "add main.py".
# - Executing ```git rebase -i _target``` opens the git-rebase-todo text file with the following first three lines  
# ```bash
# pick cf0091e add module_a.py
# pick e3516ab fix spelling error in module_a.py
# pick edf1942 add more details to module_a.py
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# * We can tidy up our commit history by modifying the git-rebase-todo text file as follows
# ```bash
# pick cf0091e add module_a.py
# fixup e3516ab fix spelling error in module_a.py
# fixup edf1942 add more details to module_a.py
# ```
# * Closing the git-rebase-todo text file starts the rebase and results in the following linear commit history

# %% [markdown] slideshow={"slide_type": "fragment"}
# <div align="left">
# <img src="./figures/r_first_i_rebase.png" alt="After interactively rebasing _messy_branch on _target" width=1000/>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# * We now add the updates to module_a.py that are required due to the update of main.py

# %% [markdown] slideshow={"slide_type": "-"}
# <div align="left">
# <img src="./figures/r_before_second_rebase.png" alt="Before interactive rebase of _messy_branch on itself" width=1000>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "fragment"}
# * We can now start another interactive rebase to squash the last commit into the previous commit
# * Running ```git rebase -i HEAD~2``` or ```git rebase -i cbe58462``` in the terminal yields the following two lines for the git-rebase-todo file
# ```bash
# pick 06dd804 add module_a.py
# pick 05373dd consider update of main.py in module_a.py
# ```
# * Changing the git-rebase-to file to
# ```bash
# pick 06dd804 add module_a.py
# fixup 05373dd consider update of main.py in module_a.py
# ```
# yields

# %% [markdown] slideshow={"slide_type": "-"}
# <div align="left">
# <figcaption>After interactive rebase of _messy_branch on itself</figcaption>
# <img src="./figures/r_after_second_i_rebase.png" alt="After interactive rebase of _messy_branch on itself" width=1000/>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# * We are now free to merge _messy_branch into _target using 
#     - or a three-way merge with an additional merge message
#     ```bash
#         git checkout _target;
#         git merge _messy_branch --no-ff
#     ```
#     - a fast-forward merge
#     ```bash
#         git checkout _target;
#         git merge _messy_branch
#     ```

# %% [markdown] cell_style="split" slideshow={"slide_type": "-"}
# <div align="left">
# <figcaption>B: Clean commit history with explicit 3-way merge</figcaption>
# <img src="./figures/r_3_squash_no_ff.png" alt="clean commit history with merge" width=1000/>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] cell_style="split"
# <div align="left">
# <figcaption>C: Clean linear commit history</figcaption>
# <img src="./figures/r_3_squash.png" alt="clean linear commit history" width=1000/>
# <div/>
# <div align="left">
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Concluding remarks and what commits not to rebase
# - (Interactive) rebasing helps to **obtain a concise and linear commit history** for your project. 
# - Especially if you want to integrate updates from another branch into you private branch, rebase allows you to avoid 3-way merges.
# - Many developers like to use fast-forward merges (facilitated through rebasing) for small features or bug fixes, while reserving 3-way merges for the integration of longer-running features.
# - Moreover, you should **try to avoid 3-way merges in feature branches**.
# - Alternatively, you can also use merge squashes to avoid 3-way merges. 
# - **There is no rule** what should be a 3-way merge, a squash, or a fast-forward merge, it depends on the team.
# - However, **I recommend to use git pull --rebase** in general. In most circumstances, this is more intuitive than synchronizing with the remote branch via a merge commit.

# %% [markdown] slideshow={"slide_type": "slide"}
# - Moreover, there is the rule that **'public' commits should not be rebased**.
# <div align="left">
# <img src="./figures/spiderman.png" alt="With great power" width=600/>
# <div/>

# %% [markdown] slideshow={"slide_type": "subslide"}
# - Recall that rebase rewrites history yielding new commits 
# <div align="left">
# <img src="./figures/at_rebase_0.png" alt="Before rebase" width=800/>
# <div/>
# <div align="left">
# <div/>
# - What would happen if you rebase main on feature?
# <div align="left">
# <img src="./figures/at_rebase_3.png" alt="Rebasing main" width=800/>
# <div/>
# <div align="left">
# <div/>
#
# - As a result, Git will think that your main branch’s history has diverged from the corresponding remote
#     - Consequently, you can't push to the remote unless you specify --force
#     - This overwrites the remote branch to match the local rebased one and makes things very confusing for other people if they try to integrate these changes
#     - You should only push --force if the branch is 'private'
# - If your branch is 'public', i.e., anybody else might work with it, **do not rebase**!
#     - Do not rebase pull/merge requests (more about this later)
#
# Figures source: https://www.atlassian.com/git/tutorials/merging-vs-rebasing

# %% [markdown] slideshow={"slide_type": "slide"}
# # Workflows

# %% [markdown] slideshow={"slide_type": "-"}
# The following workflow is recommend for integrating data from one remote into another.
#
# **Merging and rebasing**
# - Confirm that the source branch that should be merged is up-to-date
#     - If required, checkout the source branch, tidy the local commit history and integrate data from a remote 
# - Confirm the HEAD points to the receiving branch which is up-to-date: 
#     - If not done already, checkout the receiving branch, tidy the local commit history and integrate data from a remote
# - Integrate the source branch into the current branch using
#     - ```git merge <source branch>``` to ff-merge if possible, otherwise 3-way merge
#     - ```git merge --ff-only <source branch>``` to only allow a ff-merge
#     - ```git merge --no-ff <source branch>``` to enforce a 3-way merge
#     - ```git merge --squash <source branch>``` to squash
#         - It is recommended to delete the source branch after a squash to avoid duplication of commits if data from this branch is integrated in the receiving branch again
#     - ```rebase <source branch>``` to perform a rebase on the source branch
#     - ```rebase -i <source branch>``` to perform an interactive rebase on the source branch
#     
# See also https://www.atlassian.com/git/tutorials/merging-vs-rebasing#conceptual-overview

# %% [markdown] slideshow={"slide_type": "slide"}
# **Integrating data from a remote into a local branch**
# - Optional, but useful: fetch data from the remote and have a look at its commits using git log origin/branch_name
#     - Instead of ```git pull origin <source branch>``` you can then use ```git merge origin/branch_name```
#     - Instead of ```git pull --rebase origin <source branch>``` you can then use ```git rebase origin/branch_name```
# - Merge data into you local branch using ```git pull origin <source branch>```, you can use the same options here as for merge
# - Rebase your local branch on the remote using ```git pull --rebase origin <source branch>```: In most circumstances, this is more intuitive than synchronizing with the remote branch via a merge commit.
#     
# **Pushing data to a remote**
# - If required, start an interactive rebase to tidy the part of the commit history that has not been pushed to the remote
# - Never ever change commits that have already been pushed to a remote from which other people might fetch (!)
# - Integrate data from the remote into your local branch
# - Push to the remote

# %% [markdown] slideshow={"slide_type": "slide"}
# # Versioning Jupyter notebooks

# %% [markdown] slideshow={"slide_type": "fragment"}
# - Notebooks are .json files which contain metadata, input and output of cells
# - For instance, the first 31 lines of lecture_notes/1_version_control/intro.ipynb are given by

# %% slideshow={"slide_type": "fragment"}
!cat 0_intro.ipynb | head -n 31

# %% [markdown] slideshow={"slide_type": "slide"}
# - It is **confusing to track notebooks (metadata, input and output of cells) as .json files** with Git because
#     - Diffs are hard to investigate because of the nested structure of .json files
#     - Executing the notebook, without changing the input of cells, may change the underlying .json file
#     - As a result, it is often not clear what has changed and if this change has something to do with the underlying code of the notebook
#     - Merging .json files directly is a nightmare
# - [NbDime](https://github.com/jupyter/nbdime) and [nbdev2](https://www.fast.ai/posts/2022-08-25-jupyter-git.html)  can be used to **diff and merge notebooks**
# - I recommend [Jupytext](https://github.com/mwouts/jupytext) for **tracking metadata and input of notebooks** with Git
#     - Converts metadata and input of a notebook to markdown or scripts, e.g., a .py-file
#     - These text files can be normally tracked with Git
#     - Converting a notebook to a script is very handy for restructuring or modularizing notebook code using your favorite text editor
#     - Notebooks can be automatically synced with script files
#     - You can also start with a text file and convert it to a Jupyter notebook
#     - See [examples](https://jupytext.readthedocs.io/en/latest/examples.html) for more details

# %% [markdown] slideshow={"slide_type": "slide"}
# **Jupytext workflow**
# - Using Jupytext you can version Jupyter notebooks as follows:
#     - Only **version the corresponding .py-file**
#         - If you only want to version the **cell inputs**, e.g., the underyling code of the notebook
#         - If you are not interested in sharing the cell outputs, e.g., you don't want to share
#           notebooks as documentation or visualization tool
#     - **Version both the .json and .py-file**
#         - If you want to version the **cell inputs and outputs** of your notebook

# %% [markdown] slideshow={"slide_type": "slide"}
# **Jupytext formats**
# - Jupytext provides several [formats](https://jupytext.readthedocs.io/en/latest/formats.html) when a notebook is converted to a script
# - The most important formats are percent and light
#     - **Percent**: All cells are explicitly delimited with a commented double percent sign # %%. This is supported by many editors, e.g., VS Code, PyCharm.
#     ```python
#     # %% [markdown]
#     # This is a multiline
#     # Markdown cell
#
#     # %%
#     # This is a code cell
#     def one():
#         return 1
#
#     ```
#     - **Light** (default): This format was created for Jupytext and can be used to convert scripts into notebooks which were never prepared to become a notebook.
#     ```python
#     # This is a multiline
#     # Markdown cell
#
#     # This is a code cell
#     def one():
#         return 1
#     ```
#

# %% [markdown] slideshow={"slide_type": "slide"}
# **Jupytext illustration**
# - Cd into the directory of this notebook
# - Checkout a new branch

# %%
!pwd

# %% slideshow={"slide_type": "-"}
!git checkout -b _jupytext

# %% [markdown] slideshow={"slide_type": "slide"}
# * Convert this notebook into a .py script named '1_git_percent.py' using the percent format

# %% slideshow={"slide_type": "-"}
!jupytext --to py:percent --out 1_git_percent.py 1_git.ipynb
!cat 1_git_percent.py | head -n 25

# %% [markdown] slideshow={"slide_type": "slide"}
# - Convert this notebook into a .py script named '1_git_light.py' using the default light format

# %% slideshow={"slide_type": "-"}
!jupytext --out 1_git_light.py 1_git.ipynb
!cat 1_git_light.py | head -n 25

# %% [markdown] slideshow={"slide_type": "slide"}
# - Convert both scripts back to notebooks

# %% slideshow={"slide_type": "-"}
!jupytext --to notebook 1_git_light.py
!jupytext --to notebook 1_git_percent.py

# %% [markdown] slideshow={"slide_type": "-"}
# - Checkout main and delete the temporary branch

# %% slideshow={"slide_type": "-"}
!git checkout main
!git branch -D _jupytext

# %% [markdown] slideshow={"slide_type": "-"}
# - Delete the created files

# %% slideshow={"slide_type": "-"}
for file in ['1_git_light.ipynb', '1_git_light.py', '1_git_percent.ipynb', '1_git_percent.py']:
    if os.path.exists(file):
        os.remove(file)

# %% [markdown] slideshow={"slide_type": "slide"}
# Hint:  
#
# If you want to automatically convert a notebook to a .py script with percent format in the subfolder notebook_as_py whenever you save it do the following.  
#
# Create the file **jupytext.toml** in the root directory of your project with the following content.
# ```
# formats = "ipynb,notebook_as_py//py:percent"
# ``` 

# %% [markdown] slideshow={"slide_type": "slide"}
# # Topics that we will discuss when talking about collaboration and project management
# - Writing good commit messages
# - Working with Git providers like GitHub or GitLab
#     - Working with pull/merge requests
#     - Working with issues and how to automatically close them wit a commit message and push
#     - [Issue board](https://docs.gitlab.com/ee/user/project/issue_board.html)
# - Git branch workflows 
