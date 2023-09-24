# Git
-----------------------------------------------------------------------------------
## interactive rebase
1. Checkout a new branch
1. Add a readme.md:
    - Add "abc" as first line and commit "Added abc to the first line".
    - Add "def" as second line and commit "Added def to the second line".
    - Add "ghi" as third line and commit "Added ghi to the third line".
    - Add "jkl" as fourth line and commit "Added jkl to the fourth line".
1. Drop the last commit.
1. Combine the first and second commit and adjust the commit message accordingly to "Added abc to the first line and def to the second line".
1. Add "jkl" and not "ghi" as third line in the third commit.
1. Undo the commits.

**solution**

1.
```bash
git checkout -b temp
```
2.
```bash
echo "abc" > readme.md;
git add readme.md && git commit -m "Added abc to the first line";

echo "def" >> readme.md;
git add readme.md && git commit -m "Added def to the second line";

echo "ghi" >> readme.md;
git add readme.md && git commit -m "Added ghi to the third line";

echo "jkl" >> readme.md;
git add readme.md && git commit -m "Added ghi to the fourth line";
```
3.-6.
```bash
git rebase -i HEAD~4
```
and edit the git-rebase-tod file as follows
```bash
pick 193caaf Added abc to the first line
squash 49bdf42 Added def to the second line
edit 02ea624 Added ghi to the third line
drop 1da20a1 Added ghi to the fourth line
```
and conduct the rebase by
- performing the squash of 49bdf42 into 193caaf by changing the commit message to
    "Added abc to the first line and def to the second line."
- during the edit of the third commi change readme.md into
```
abc
def
jkl
```
and then run git add, git commend --amend and git rebase --continue.

7.
```bash
git checkout -;
git branch -D temp;
```


-----------------------------------------------------------------------------------
## remote
1) Create a new branch named by your name
2) Commit and push a text file name 'animal.txt' that contains the name of your favorite animal to the remote branch
3) Undo the push of 'animal.txt'
4) Undo all commits

1) Create a new branch named by your name.
2) Commit a text file name 'animal.txt' that contains the name of your favorite animal.
3) Undo the previous commit use an interactive rebase so that 'animal.txt' contains your second favorite animal.
4) Push 'animal.txt' to a remote with the same name.
5) Undo the previous commit on the remote so that 'animal.txt' contains your favorite animal.
6) Checkout to main and delete the local and remote branch named by your name.

**solution**
1 & 2)
    ```bash
    git checkout -b my_name;
    echo "cat" > animal.txt;
    git add animal.txt && git commit -m "Add animal.txt";
    git push origin HEAD;
    ```
    3)
    ```bash
    rm animal.txt;
    git add animal.txt && git commit -m "Delete animal.txt";
    git push origin HEAD;
    ```

    4)
    ```bash
    git push -d origin my_name;
    git checkout -;
    git branch -D my_name;
    ```

----------------------------------------------------------------------------------
## Merging
**Setup for 1)**
```bash
# work on B
git checkout -b B && echo "123" > b.txt &&  git add b.txt && git commit -m "Add b.txt" &&
git checkout -b B_remote && echo "123" > b_remote.txt && git add b_remote.txt && git commit -m "Add b_remote.txt" &&
git checkout -b A && echo "123" > a.txt && git add a.txt && git commit -m "Add a.txt" &&
git checkout -b A_remote && echo "123" > a_remote.txt && git add a_remote.txt && git commit -m "Add a_remote.txt"
```

**Solution for 3): using rebase for ff-merges**
```bash
# integrate B_remote into B
git checkout B;
# git merge B_remote --ff-only; # not possible
git rebase B_remote;

# integrate B into A
git checkout A;
git merge B --ff-only; # not possible
git rebase B;

# integrate A into A_remote
git checkout A_remote;
git merge A --ff-only; # not possible
git rebase A;
```

**Solution for 5): using merge**
```bash
# using merges
git checkout B;
git merge B_remote --no-edit;

# integrate B into A
git checkout A;
git merge B --no-edit;

# integrate A into A_remote
git checkout A_remote;
git merge A --no-edit;
```

**Solution for 4) and 6)**
```bash
# reset
git checkout main;
git branch -D A B A_remote B_remote;
```

git checkout main &&
git branch -D A B A_remote B_remote

# DVC



-----------------------------------------------------------------------------------
## rebase on other branch: UNFINISHED
1. Add the following two (separate) commits to your 'wrong' branch:
    - a text file named 'animal.txt' that contains the name of your favorite animal
    - a text file that 'color.txt' contains the name of your favorite color
2. Create a new branch named 'right'
    - transfers the commits of 'wrong' to the branch 'right' without using a merge
    - undo the first commit on the branch 'right'
3. Undo all commits
4. Repeat 1 and 2

**solution**
```bash
git checkout -b wrong;

echo "cat" > animal.txt;
git add animal.txt && git commit -m "Add animal.txt";

echo "blue" > animal.txt;
git add color.txt && git commit -m "Add color.txt";

git checkout -b right;
git rebase
```

1. Add the following two (separate) commits to your 'wrong' branch:
    - a text file named 'animal.txt' that contains the name of your favorite animal
    - a text file that 'color.txt' contains the name of your favorite color
2. Create a new branch named 'right'
    - a text file named 'plant.txt' that contains the name of your favorite plant
    - a text file that 'food.txt' contains the name of your favorite food
3. rebase right on wrong and wrong and right


- add jupytext exercise? ja
evtl. auf branch A
1. erstelle
zelle 1:
from datetime import datetime
zelle 2:
datetime.now()
2. versioniere .ipnyb mit git
3. checkout branch B und führe notebook noch mal aus
4. versuche ein rebase auf A/oder merge A rein
5. mache die änderungen auf B rückgängig
6. führe die 1. zelle von ipnyb 2 mal aus. versuche 4. noch mal

7. checkout zu branch A und unversioniere .ipynb
8. benutze jupytext um die entsprechende .py datei zu versionien
9. wiederhole 3-6
