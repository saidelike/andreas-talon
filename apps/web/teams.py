from talon import Context, Module, actions

ctx = Context()
mod = Module()

# we define what it is to be a "teams" app
mod.apps.teams = """
tag: browser
browser.host: teams.microsoft.com
"""
mod.apps.teams = """
os: windows
and app.exe: Teams.exe
"""
mod.apps.teams = """
os: windows
and app.exe: ms-teams.exe
"""

# this context is only active when the above "teams" app is enabled
ctx.matches = """
app: teams
"""

ctx.tags = ["user.voip"]


@ctx.action_class("user")
class UserActions:
    def mute_microphone():
        actions.key("ctrl-shift-m")
