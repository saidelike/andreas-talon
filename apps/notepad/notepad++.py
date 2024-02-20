from talon import Context, actions, Module

ctx = Context()
mod = Module()

# we define what it is to be a "notepadpp" app
mod.apps.notepadpp = """
os: windows
and app.name: Notepad++
os: windows
and app.exe: notepad++.exe
"""

# this context is only active when the above "notepadpp" app is enabled
ctx.matches = r"""
app: notepadpp
"""


@ctx.action_class("win")
class win_actions:
    # Return the open filename
    def filename():
        filename = actions.win.title().split(" - ")[0]
        if "." in filename:
            return filename
        return ""


# @ctx.action_class("code")
# class CodeActions:
#     def toggle_comment():
#         actions.key("ctrl-q")


# these are Talon-defined "app" actions (only grouped for clarity) that we override
@ctx.action_class("app")
class AppActions:
    # Switch to previous tab for this window
    def tab_previous():
        actions.key("ctrl-pageup")

    # Switch to next tab for this window
    def tab_next():
        actions.key("ctrl-pagedown")

    # Open a new tab
    def tab_open():
        actions.key("ctrl-n")


@ctx.action_class("user")
class UserActions:
    # ----- Tabs -----
    # inherited when "user.tabs" tag is enabled
    def tab_jump(number: int):
        if number < 10:
            actions.key(f"ctrl-keypad_{number}")

    def tab_back():
        actions.key("ctrl-tab")
