from typing import Optional
from talon import Module, Context, actions

mod = Module()
ctx = Context()
# Declare a new global "user.git" tag
mod.tag("git")

mod.list("git_branch", "List of common git branches")
ctx.lists["user.git_branch"] = {
    "master": "master",
    "main": "main",
    "men": "main",
    "develop": "develop",
}


# we define new actions that are "git" related
# i.e. in vscode or the terminal
# with a default behavior and that we can override later
@mod.action_class
class Action:
    def git_clone():
        """Clone git repository"""
        actions.insert(f"git clone ")

    def git_status():
        """Show git status"""
        actions.insert("git status\n")

    def git_stage_all():
        """Stage all files"""
        actions.insert("git add .\n")

    def git_unstage_all():
        """Unstage all files"""
        actions.insert("git reset .\n")

    def git_pull():
        """Pull from remote"""
        actions.insert("git pull\n")

    def git_push():
        """Push to remote"""
        actions.insert("git push\n")

    def git_push_tags():
        """Push tags to remote"""
        actions.insert("git push --tags\n")

    def git_create_tag(tag: Optional[str] = None):
        """Create tag <tag>"""
        actions.insert(f"git tag {tag or ''}")

    def git_show_tags():
        """Show tags"""
        actions.insert("git tag\n")

    def git_stash():
        """Stash changes"""
        actions.insert("git stash ")

    def git_stash_pop():
        """Pop stash"""
        actions.insert("git stash pop")

    def git_fetch_all():
        """Fetch all repositories"""
        actions.insert("git fetch --all\n")

    def git_merge(branch: Optional[str] = None):
        """Merge branch <branch>"""
        actions.insert(f"git merge {branch or ''}")

    def git_checkout(branch: Optional[str] = None, submit: bool = False):
        """Checkout branch <branch>"""
        actions.insert(f"git checkout {branch or ''}")
        if submit:
            actions.insert("\n")

    def git_show_branches():
        """Show branches"""
        actions.insert("git branch --all\n")

    def git_create_branch(branch: Optional[str] = None):
        """Create branch <branch>"""
        actions.insert(f"git checkout -b {branch or ''}")

    def git_delete_branch(branch: Optional[str] = None):
        """Delete branch <branch>"""
        actions.insert(f"git branch -d {branch or ''}")

    def git_commit(message: Optional[str] = None):
        """Commit changes <message>"""
        actions.insert(f'git commit -m "{message or ""}"')
        actions.edit.left()

    def git_commit_amend(message: Optional[str] = None):
        """Commit changes <message>"""
        actions.insert(f'git commit --amend -m "{message or ""}"')
        actions.edit.left()

    def git_diff():
        """Show git diff"""
        actions.insert("git diff\n")

    def git_stash_show():
        """Show git stashes"""
        actions.insert("git stash show\n")

    def git_stash_list():
        """List git stashes"""
        actions.insert("git stash list\n")

    def git_log():
        """Show git log"""
        actions.insert(
            "git log --graph --color=always --format='%C(auto)%h%d %s %C(green)(%cr) %C(bold blue)<%an>%Creset'\n"
        )

    def git_remote():
        """Show git remote"""
        actions.insert("git remote -v\n")

    def git_cherry_pick():
        """Cherry pick commit"""
        actions.insert("git cherry-pick ")

    def git_numstat(since: Optional[str] = None):
        """Show git statistics"""
        args = "--author='Cedric Halbronn'"
        if since:
            args = f"{args} --since '{since}'"
        awk = "awk 'NF==3 {plus+=$1; minus+=$2} END {printf(\"+%d, -%d\\n\", plus, minus)}'"
        actions.insert(f"git log --numstat {args} | {awk}\n")
