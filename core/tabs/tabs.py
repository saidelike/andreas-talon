from talon import Module, Context, actions


mod = Module()
# Declare a new global "user.tabs" tag
mod.tag("tabs")

# this context is only active when the "user.tabs" tag is enabled
ctx = Context()
ctx.matches = r"""
tag: user.tabs
"""


# these are Talon-defined "app" actions (only grouped for clarity) that we override
@ctx.action_class("app")
class AppActions:
    # Switch to previous tab for this window
    def tab_previous():
        actions.key("ctrl-shift-tab")

    # Switch to next tab for this window
    def tab_next():
        actions.key("ctrl-tab")

    # Open a new tab
    def tab_open():
        actions.key("ctrl-t")

    # Close the current tab
    def tab_close():
        actions.key("ctrl-w")

    # Re-open the last-closed tab
    def tab_reopen():
        actions.key("ctrl-shift-t")


# Declare actions that are global too (not related to any tag)
# Note that everything you define on the module is in the "user" namespace. You can't change that.
@mod.action_class
class TabActions:
    def tab_jump(number: int):
        """Jumps to the specified tab"""
        actions.key(f"ctrl-{number}")

    def tab_jump_from_back(number: int):
        """Jumps to the specified tab counted from the back"""
        actions.user.tab_final()
        for _ in range(number - 1):
            actions.app.tab_previous()

    def tab_final():
        """Jumps to the final tab"""
        actions.user.tab_jump(1)
        actions.app.tab_previous()

    def tab_move_left():
        """Move tab to the left"""
        actions.key("ctrl-shift-pageup")

    def tab_move_right():
        """Move tab to the right"""
        actions.key("ctrl-shift-pagedown")

    def tab_duplicate():
        """Duplicate tab"""

    def tab_back():
        """Jump to last used tab"""
