from talon import Module, Context, actions

ctx = Context()
mod = Module()

# we define what it is to be a "chrome" app
mod.apps.chrome = """
os: windows
and app.name: Google Chrome
os: windows
and app.exe: chrome.exe
"""

# this context is only active when the above "chrome" app is enabled
ctx.matches = """
app: chrome
"""

# we enable the "browser" tag so we have the usual browser features
ctx.tags = ["browser"]


@ctx.action_class("browser")
class BrowserActions:
    def open_private_window():
        actions.key("ctrl-shift-n")
