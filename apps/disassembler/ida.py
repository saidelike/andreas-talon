from talon import Module, Context, actions
import re

mod = Module()
ctx = Context()

mod.apps.ida = r"""
app.name: The Interactive Disassembler
"""

ctx.matches = r"""
app: ida
"""


@ctx.action_class("user")
class UserActions:
    def disassembler_load_header():
        actions.key("ctrl-f9")

    def disassembler_reload_header():
        actions.key("ctrl-f9")
        actions.sleep("500ms")
        actions.key("enter")

    def disassembler_decompile():
        actions.key("f5")
