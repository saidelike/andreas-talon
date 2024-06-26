# this file is only active when the "user"-defined "user.git" and Talon-defined "terminal" tags are enabled
tag: user.git
and tag: terminal
-

git:                        "git "
git version:                "git --version\n"
git init:                   "git init\n"
git log original:           "git log\n"
git reflog:                 "git reflog\n"
git clean:                  "git clean "
git remove:                 "git rm "
git rebase:                 "git rebase "
git revert:                 "git revert "

git reset:                  "git reset "
git reset head:             "git reset --soft HEAD^"
git reset soft:             "git reset --soft "
git reset hard:             "git reset --hard "

git fetch:                  "git fetch "
git fetch upstream:         "git fetch upstream\n"
git fetch prune:            "git fetch --prune origin\n"

git checkout last:          "git checkout -\n"

git add:                    "git add "
git add update:             "git add -u\n"

git diff halt:              "git diff "
git diff [cache|cached]:    "git diff --cached\n"
git diff <user.text>:       "git diff {text}"

git pull upstream:          "git pull upstream\n"
git pull upstream master:   "git pull upstream master\n"
git pull upstream main:     "git pull upstream main\n"

git merge no commit:        "git merge upstream/master --no-ff --no-commit"

git push deli:              "git push origin -d "

git numstat:                user.git_numstat("")
git numstat year:           user.git_numstat("1 year")
git numstat month:          user.git_numstat("1 month")
git numstat week:           user.git_numstat("1 week")

git shortlog:               "git shortlog -sn\n"
