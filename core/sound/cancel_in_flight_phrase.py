# Source: https://github.com/pokey/pokey_talon/blob/b1718056bd85da95f7778a7ef2340d205e320efb/core/cancel_in_flight_phrase.py
from talon import Module, actions, app

mod = Module()


@mod.action_class
class Actions:
    def cancel_in_flight_phrase():
        """Cancels phrase currently being spoken"""
        active_microphone = actions.sound.active_microphone()
        actions.sound.set_microphone("None")
        actions.sound.set_microphone(active_microphone)

    def cancel_in_flight_phrase_loud():
        """Cancels phrase currently being spoken"""
        actions.user.cancel_in_flight_phrase()
        actions.user.notify("Cancelled phrase")
