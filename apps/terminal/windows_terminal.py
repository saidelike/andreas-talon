from talon import Module, Context, actions

ctx = Context()
mod = Module()

# we define what it is to be a "windows_terminal" app
mod.apps.windows_terminal = r"""
os: windows
and app.exe: windowsterminal.exe
"""

# this context is only active when the above "windows_terminal" app is enabled
ctx.matches = r"""
app: windows_terminal
"""


# these are Talon-defined "app" actions (only grouped for clarity) that we override
@ctx.action_class("app")
class AppActions:
    # Open a new window
    def window_open():
        actions.key("ctrl-shift-n")

    # Open a new tab
    def tab_open():
        actions.key("ctrl-shift-t")

    # Close the current tab
    def tab_close():
        actions.key("ctrl-shift-w")

    # Open app preferences
    def preferences():
        actions.key("ctrl-,")


# these are Talon-defined "edit" actions (only grouped for clarity) that we override
@ctx.action_class("edit")
class EditActions:
    # Copy selection to clipboard
    def copy():
        actions.key("ctrl-shift-c")

    # Paste clipboard at cursor
    def paste():
        actions.key("ctrl-shift-v")

    # Open Find dialog, optionally searching for text
    def find(text: str = None):
        actions.key("ctrl-shift-f")
        if text:
            actions.insert(text)


# these are "user" actions inherited when the "user.tabs" tag is enabled
# that we override to call our Windows Terminal implementation
@ctx.action_class("user")
class UserActions:
    # ----- Tabs -----
    # inherited when "user.tabs" tag is enabled
    def tab_jump(number: int):
        if number < 9:
            actions.key(f"ctrl-alt-{number}")

    def tab_final():
        actions.key("ctrl-alt-9")

    def tab_duplicate():
        actions.key("ctrl-shift-d")
