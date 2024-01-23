from talon import Module, Context, actions

mod = Module()

# we define what it is to be a "wsl" app
# This requires starting wsl.exe into Windows Terminal
mod.apps.wsl = r"""
app: windows_terminal
and win.title: /\w+@[\w-]+: /i
"""
# This is when opening "wsl" standalone
mod.apps.wsl = """
os: windows
and app.name: Microsoft Windows Subsystem for Linux Launcher
os: windows
and app.exe: wsl.exe
"""

ctx = Context()
# this context is only active when the above "wsl" app is enabled
ctx.matches = """
app: wsl
"""

ctx.tags = ["terminal", "user.bash"]


@ctx.action_class("user")
class UserActions:
    def talon_app() -> str:
        return update_path(actions.next())

    def talon_home() -> str:
        return update_path(actions.next())

    def talon_user() -> str:
        return update_path(actions.next())

    def user_home() -> str:
        return update_path(actions.next())

    def file_manager_go(path: str):
        if path.startswith("shell:"):
            actions.user.file_manager_open(path)
        else:
            path = update_path(path)
            actions.next(path)


def update_path(path: str) -> str:
    path = str(path)
    if path[1] == ":":
        path = f"/mnt/{path[0].lower()}{path[2:]}"
    return path.replace("\\", "/")
