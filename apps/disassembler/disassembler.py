from talon import Module, Context, actions, app

mod = Module()
mod.tag("disassembler")

ctx = Context()

ctx.matches = r"""
tag: user.disassembler
"""


@mod.action_class
class Actions:
    def disassembler_load_header():
        """Load header file"""

    def disassembler_reload_header():
        """Reload last header file"""

    def disassembler_decompile():
        """Decompile the current function"""
