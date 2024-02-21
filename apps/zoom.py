from talon import Context, actions, Module

ctx = Context()
mod = Module()

# we define what it is to be a "zoom" app, but it's already the case by default
mod.apps.zoom = r"""
os: windows
and app.exe: zoom.exe
"""

# this context is only active when the above "zoom" app is enabled
ctx.matches = r"""
app: zoom
"""

ctx.tags = ["user.voip"]


@ctx.action_class("user")
class UserActions:
    def mute_microphone():
        actions.key("alt-a")
