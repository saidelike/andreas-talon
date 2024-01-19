from talon import Module, actions


mod = Module()
# Declare a new global "user.navigation" tag
mod.tag("navigation")


# Declare actions that are global too (not related to any tag)
# Note that everything you define on the module is in the "user" namespace. You can't change that.
@mod.action_class
class Actions:
    def go_back():
        """Navigate back"""
        actions.key("alt-left")

    def go_forward():
        """Navigate forward"""
        actions.key("alt-right")
