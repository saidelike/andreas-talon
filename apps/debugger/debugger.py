from talon import Module, Context, actions, app

mod = Module()
mod.tag("debugger")

ctx = Context()

ctx.matches = r"""
tag: user.debugger
"""


# @mod.action_class
# class Actions:
