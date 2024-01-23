from talon import Context, actions, Module

ctx = Context()
mod = Module()

# we define what it is to be a "notepad" app
mod.apps.notepad = """
os: windows
and app.name: Notepad
os: windows
and app.exe: notepad.exe
"""

# this context is only active when the above "notepad" app is enabled
ctx.matches = r"""
app: notepad
"""


@ctx.action_class("win")
class win_actions:
    # Return the open filename
    def filename():
        filename = actions.win.title().split(" - ")[0]
        if "." in filename:
            return filename
        return ""
