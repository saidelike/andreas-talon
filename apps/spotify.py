from talon import Module, Context, actions


mod = Module()
ctx = Context()

# we define what it is to be a "spotify" app, but it's already the case by default
mod.apps.spotify = r"""
os: windows
and app.exe: spotify.exe
"""

# this context is only active when the above "spotify" app is enabled
ctx.matches = r"""
app: spotify
"""

ctx.tags = ["user.navigation"]


@ctx.action_class("user")
class UserActions:
    def volume_up():
        actions.key("ctrl-up")

    def volume_down():
        actions.key("ctrl-down")
