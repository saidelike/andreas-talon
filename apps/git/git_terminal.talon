tag: user.git
tag: terminal
-

git:                        "git "
git verison:                "git --version\n"
git init:                   "git init\n"
git log original:           "git log\n"
git reflog:                 "git reflog\n"
git clean:                  "git clean "
git remove:                 "git rm "
git branch:                 "git branch "
git cherry pick:            "git cherry-pick "
git rebase:                 "git rebase "
git revert:                 "git revert "

git remote:                 "git remote "
git remote verbose:         "git remote -v\n"

git reset:                  "git reset "
git reset head:             "git reset --soft HEAD^"
git reset soft:             "git reset --soft "
git reset hard:             "git reset --hard "

git fetch:                  "git fetch "
git fetch all:              "git fetch -a\n"
git fetch upstream:         "git fetch upstream\n"
git fetch prune:            "git fetch --prune origin\n"

git checkout last:          "git checkout -\n"

git add:                    "git add "

git commit amend:           "git commit --amend "

git diff halt:              "git diff "
git diff <user.text>:       "git diff {text}"

git pull upstream:          "git pull upstream\n"
git pull upstream master:   "git pull upstream master\n"
git pull upstream main:     "git pull upstream main\n"

git push deli:              "git push origin -d "

git merge quit:
    ":q"
    key(enter)

git numstat:                user.git_numstat("")
git numstat year:           user.git_numstat("1 year")
git numstat month:          user.git_numstat("1 month")
git numstat week:           user.git_numstat("1 week")
