from talon import Module, Context, actions

mod = Module()

# we define what it is to be a "git_bash" app
# This requires using a "Git Bash" profile into Windows Terminal
mod.apps.git_bash = """
app: windows_terminal
and win.title: /MINGW64:/i
"""
# This is when opening "Git Bash" standalone
mod.apps.git_bash = r"""
os: windows
and app.exe: mintty.exe
"""
# TODO: what is this?
mod.apps.git_bash = r"""
os: windows
app: vscode
win.file_ext: .bashbook
"""

# this context is only active when the above "git_bash" app is enabled
# or when we are in the vscode terminal
# or when we have git bash inside window terminal (this is to give priority to git bash vs windows terminal)
ctx = Context()
ctx.matches = r"""
app: git_bash

app: vscode
and win.title: /\[Terminal\]$/

app: git_bash
and app: windows_terminal
"""

# we want to be able to use bash commands and browse tabs
# make sure that tabs are available through "standalone Git Bash with groupy"
# TODO: enabling the "user.tabs" is actually problematic when in vscode, because it changes tabs in the vscode editor
ctx.tags = ["user.bash", "user.tabs"]


# these are "user" actions inherited from "file manager"
@ctx.action_class("user")
class UserActions:
    # ----- Path -----

    # inherited from "file_manager.py"
    def talon_app() -> str:
        return update_path(actions.next())

    def talon_home() -> str:
        return update_path(actions.next())

    def talon_user() -> str:
        return update_path(actions.next())

    def user_home() -> str:
        return update_path(actions.next())

    # ----- Navigation -----

    # inherited from "file_manager.py"
    def file_manager_go(path: str):
        if path.startswith("shell:"):
            actions.insert(f"start {path}")
            actions.key("enter")
            return
        path = update_path(path)
        actions.next(path)


def update_path(path: str) -> str:
    path = str(path)
    if len(path) > 1 and path[1] == ":":
        path = f"/{path[0]}{path[2:]}"
    return path.replace("\\", "/")
