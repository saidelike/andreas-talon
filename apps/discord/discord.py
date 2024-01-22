from talon import Module, Context, actions


mod = Module()
ctx = Context()

# we define what it is to be a "discord" app
mod.apps.discord = r"""
os: windows
and app.name: Discord
os: windows
and app.exe: Discord.exe
"""

# this context is only active when the above "discord" app is enabled
ctx.matches = r"""
app: discord
"""


# these are Talon-defined "edit" actions (only grouped for clarity) that we override
@ctx.action_class("edit")
class EditActions:
    # Delete word under cursor
    def delete_word():
        actions.edit.select_word()
        actions.sleep("100ms")
        actions.edit.delete()

    # Insert line above cursor
    def line_insert_up():
        actions.key("home shift-enter up")

    # Insert line below cursor
    def line_insert_down():
        actions.key("end shift-enter")


# these are "user" actions
@ctx.action_class("user")
class UserActions:
    # inherited from "edit_word.py" so we can extend the sleep time
    def delete_word_right():
        actions.user.select_word_right()
        actions.sleep("100ms")
        actions.edit.delete()

    # inherited when the "user.voip" tag is enabled
    def mute_microphone():
        actions.key("ctrl-shift-m")
