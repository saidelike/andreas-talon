from talon import Context, Module, actions

ctx = Context()
mod = Module()

# we define what it is to be a "teams" app
mod.apps.teams = r"""
os: windows
and app.exe: teams.exe
"""
mod.apps.teams = r"""
os: windows
and app.exe: ms-teams.exe
"""
mod.apps.teams = r"""
tag: browser
browser.host: teams.microsoft.com
"""

# this context is only active when the above "teams" app is enabled
ctx.matches = r"""
app: teams
"""

# we disable paste with insertion because otherwise when we says "spam", it inserts "," instead of ", " (misses the space)
ctx.tags = ["user.voip", "user.insert_paste_disabled"]


@ctx.action_class("user")
class UserActions:
    def mute_microphone():
        actions.key("ctrl-shift-m")
