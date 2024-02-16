from talon import Module, Context, actions

mod = Module()
ctx = Context()

# we define what it is to be a "cmd" app
# TODO: for now we enable cmd when we are in vim terminal
mod.apps.cmd = r"""
os: windows
and win.title: Command Prompt

os: windows
and win.title: /C:\\Windows\\System32\\cmd.exe/
"""

# this context is only active when the above "cmd" app is enabled
ctx.matches = r"""
app: cmd
"""


# these are "user" actions
@ctx.action_class("user")
class UserActions:
    # ----- Navigation -----

    # inherited from "file_manager.py"
    def file_manager_go_parent():
        actions.user.file_manager_go("..")

    def file_manager_go_home():
        actions.user.file_manager_go("%USERPROFILE%")

    def file_manager_go(path: str):
        path = path.replace(" ", "\\ ")
        actions.insert(f"cd {path}")
        actions.key("enter")

    # ----- Create folders / files -----

    # inherited from "file_manager.py"
    def file_manager_new_folder(name: str = None):
        actions.insert(f"mkdir {name or ''}")
