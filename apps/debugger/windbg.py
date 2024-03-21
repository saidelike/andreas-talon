from talon import Module, Context, actions
import re

mod = Module()
ctx = Context()

mod.apps.windbg = r"""
app.name: WinDbgX
"""

ctx.matches = r"""
app: windbg
"""


# @ctx.action_class("user")
# class UserActions:
