from talon import Module, Context

mod = Module()
ctx = Context()

# we define what it is to be a "cmd" app
mod.apps.cmd = r"""
os: windows
win.title: Command Prompt
os: windows
win.title: /C:\\Windows\\System32\\cmd.exe/
"""

# this context is only active when the above "cmd" app is enabled
ctx.matches = r"""
app: cmd
"""
