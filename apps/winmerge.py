from talon import actions, Context, Module

mod = Module()
ctx = Context()

# we define what it is to be a "winmerge" app, but it's already the case by default
mod.apps.winmerge = """
os: windows
and app.exe: WinMergeU.exe
"""


@ctx.action_class("user")
class UserActions:
    # ----- Scroll -----
    # inherited when "user.scroll" tag is enabled
    def scroll_up():
        actions.key("ctrl-up")

    def scroll_down():
        actions.key("ctrl-down")

    def scroll_up_page():
        actions.key("pageup")

    def scroll_down_page():
        actions.key("pagedown")

    def scroll_up_half_page():
        actions.app.notify("half page up not supported for WinMerge")

    def scroll_down_half_page():
        actions.app.notify("half page down supported for WinMerge")
