from talon import Module, Context

ctx = Context()
mod = Module()

# we define what it is to be a "edge" app
mod.apps.edge = """
os: windows
and app.name: Microsoft Edge
os: windows
and app.exe: msedge.exe
"""

# this context is only active when the above "edge" app is enabled
ctx.matches = """
app: edge
"""

# we enable the "browser" tag so we have the usual browser features
ctx.tags = ["browser"]
