from talon import Context, Module, actions

mod = Module()
# Declare a new global "user.cursorless_mimic" tag
mod.tag("cursorless_mimic")

ctx = Context()

# this context is only active when we can't use cursorless
ctx.matches = r"""
not tag: user.cursorless

tag: user.cursorless
and not win.title: /\[Text Editor\]$/
"""


# we enable the "cursorless_mimic" tag so we have some Cursorless commands
ctx.tags = ["user.cursorless_mimic"]
