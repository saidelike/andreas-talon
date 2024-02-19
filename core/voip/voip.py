from talon import Module

mod = Module()

mod.tag("voip")


# we define new actions that are "voip" related
@mod.action_class
class Actions:
    def mute_microphone():
        """Mute microphone"""
