from talon import Module, Context, actions

ctx = Context()
mod = Module()

# we define what it is to be a "chrome" app
mod.apps.chrome = r"""
os: windows
and app.exe: chrome.exe
"""

# this context is only active when the above "chrome" app is enabled
ctx.matches = r"""
app: chrome
"""

# we enable the "browser" tag so we have the usual browser features
ctx.tags = ["browser"]


# these are Talon-defined "browser" actions (only grouped for clarity) that we override
@ctx.action_class("browser")
class BrowserActions:
    # Open a private browsing window
    def open_private_window():
        actions.key("ctrl-shift-n")
