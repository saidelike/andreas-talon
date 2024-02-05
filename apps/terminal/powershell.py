from talon import Module, Context, actions, ui

ctx = Context()
mod = Module()

# we define what it is to be a "powershell" app
mod.apps.powershell = """
os: windows
and app.name: WindowsTerminal.exe
and win.title: /Windows PowerShell/

os: windows
and app.name: Windows PowerShell
"""

# this context is only active when the above "powershell" app is enabled
ctx.matches = r"""
app: powershell
"""


# these are Talon-defined "edit" actions (only grouped for clarity) that we override
@ctx.action_class("edit")
class EditActions:
    pass
    # there is no notion of selected text on a terminal.
    # so the general way to get the selected text on a terminal is to disable the clipboard, see clipboard_manager.py:selected_text()
    # and then copy the selected text, see edit.py:selected_text()
    # however in powershell app (standalone or an window terminal), copying the text unselects it so we can't use that method
    # def selected_text() -> str:
    #     ...


# these are "user" actions
@ctx.action_class("user")
class UserActions:
    # ----- Path -----
    # inherited from "file_manager.py"
    def file_manager_go(path: str):
        actions.insert(f"cd {path}")
        actions.key("enter")
