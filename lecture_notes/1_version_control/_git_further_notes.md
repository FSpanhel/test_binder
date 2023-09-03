# investigating options of merge

1. setup
```bash
git checkout main;
git branch -D a b;

git branch a;
git branch b;

git checkout b;
echo "1" > text.txt && git add text.txt && git commit -m "add text.txt";
echo "1" > text2.txt && git add text2.txt && git commit -m "add text2.txt";

git checkout a;
echo "1" > text3.txt && git add text3.txt && git commit -m "add text3.txt";
# echo "2" > text.txt && git add text.txt && git commit -m "add text.txt";
```

2. no commit: does not work if ff
```bash
git merge --no-commit --log b;
```

3. no commit and squash
    - similar to a merge but you have to commit the changes as a new commit, automatically calls --no-commit
    - https://stackoverflow.com/questions/2427238/what-is-the-difference-between-merge-squash-and-rebase
        - does not mark any merge relationship. (Note: it does not produce a commit right away: you need an additional git commit -m "squash branch")
        - This is useful if you want to throw away the source branch completely
        - Da nicht direkt ein commit erzeugt wird kann ich mir auch nur die änderungen holen die mich interessieren!
```bash
git merge --no-commit --squash -v b;  # no-commit hat hier keinen effekt da suqash eh anhält, wasa ist wenn ich --commit mache?
```

4. reset
```bash
git checkout b;
git merge --commit a;
```


# relation push and merge
- from remote to local
    - since this correspond to a fetch and merge/rebase, it does not matter whether the branch to be merged is a remote or not
- from local to remote
    - A push could be understood as a fast-forward merge (?)
    - When I push there is never a 3-way merge and a separate
    commit message.
    - Therefore, it is so important that the local branch
    has all the information the remote has before I push.

1. setup
```bash
git checkout main;
git branch -D a;
git push -d origin a;

git branch a;

git checkout a;
git push origin HEAD;
echo "1" > text.txt && git add text.txt && git commit -m "add text.txt";
```

2. add manual change on remote
3.
```bash
git pull --log origin a;
echo "1" > text2.txt && git add text2.txt && git commit -m "add text2.txt";
git push origin a;
```
