from talon import Module, actions, registry
from ...core.imgui import imgui

mod = Module()


@imgui.open()
def gui(gui: imgui.GUI):
    gui.header("Alphabet")
    gui.line(bold=True)
    alphabet = registry.lists["user.letter"][-1]
    for key, val in alphabet.items():
        gui.text(f"{val}:  {key}")
    gui.spacer()
    # Hiding the button as we don't enable the "user.help_commands" tag
    # if gui.button("Hide"):
    #     actions.user.help_alphabet_toggle()


@mod.action_class
class Actions:
    def help_alphabet_toggle():
        """Toggle alphabet help gui"""
        if gui.showing:
            gui.hide()
        else:
            gui.show()
