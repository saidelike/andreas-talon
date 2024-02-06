from talon import Module, actions


mod = Module()
# Declare a new global "user.navigation" tag
mod.tag("navigation")


# we define new actions that are "navigation" related
# Note that everything you define on the module is in the "user" namespace. You can't change that.
@mod.action_class
class Actions:
    def go_back():
        """Navigate back"""
        actions.key("alt-left")

    def go_forward():
        """Navigate forward"""
        actions.key("alt-right")
