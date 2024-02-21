from talon import Module, actions

mod = Module()

mod.tag("code_call_function")

# Declare a new global "user.code_call_function" list
mod.list("code_call_function", "Names of functions to call")


# we define new actions that are "code call function" related
@mod.action_class
class Action:
    def code_call_function(name: str):
        """Call function <name>"""
        actions.user.insert_snippet_by_name("functionCall", {"name": name})
