from talon import Context, Module, actions
from talon.clip import MimeData
import json
import re

ctx = Context()
mod = Module()

# we define what it is to be a "slack" app
# is the browser.host populated automatically by Talon based on the browser.address() action?
mod.apps.slack = """
tag: browser
browser.host: app.slack.com
"""

# this context is only active when the above "slack" app is enabled
ctx.matches = """
app: slack
"""


# "code" has built-in actions that we override here
@ctx.action_class("code")
class CodeActions:
    # Return the active programming language
    def language():
        # hack in order to enable markdown commands in slack chat
        return "markdown"


# "edit" has built-in actions that we override here
@ctx.action_class("edit")
class EditActions:
    # Insert line above cursor
    def line_insert_up():
        actions.key("home ctrl-enter up")

    # Insert line below cursor
    def line_insert_down():
        actions.key("end ctrl-enter")


@mod.action_class
class UserActions:
    def slack_open_search_result(search: str):
        """Opens the given search result on slack"""
        # Jump to a conversation
        actions.key("ctrl-k")
        actions.insert(search)
        actions.sleep("400ms")
        actions.key("enter")
