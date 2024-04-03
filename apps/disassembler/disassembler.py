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

    def disassembler_rename():
        """Rename the current item (function, variable)"""

    def disassembler_rename_function():
        """Rename the current function"""

    def disassembler_rename_variable():
        """Rename the current variable"""

    def disassembler_change_type():
        """Change the current item type (function, variable)"""

    def disassembler_change_function_type():
        """Change the current function type"""
