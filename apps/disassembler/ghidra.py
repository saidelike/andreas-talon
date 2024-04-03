from talon import Module, Context, actions
import re

mod = Module()
ctx = Context()

mod.apps.ghidra = r"""
os: windows
app.exe: javaw.exe
win.title: /CodeBrowser/
"""

ctx.matches = r"""
app: ghidra
"""


# Requirements: same shortcuts as ida https://github.com/enovella/ida2ghidra-kb/
# Installation: follow https://github.com/JeremyBlackthorne/Ghidra-Keybindings?tab=readme-ov-file#install
@ctx.action_class("user")
class UserActions:

    # def disassembler_load_header():
    #     actions.key("ctrl-f9")

    # def disassembler_reload_header():
    #     actions.key("ctrl-f9")
    #     actions.sleep("500ms")
    #     actions.key("enter")

    # def disassembler_decompile():
    #     actions.key("f5")

    def disassembler_rename():
        actions.key("n")

    def disassembler_change_type():
        actions.key("y")

    def disassembler_change_function_type():
        actions.key("ctrl-y")
