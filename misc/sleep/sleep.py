from talon import Module, Context, actions
import time

mod = Module()
ctx = Context()

sleep_word = "drowse"
time_last_pop = 0

mod.list("sleep_word", desc="Word used to sleep Talon")
ctx.lists["self.sleep_word"] = {sleep_word}


@mod.action_class
class Actions:
    def talon_sleep():
        """Put Talon to sleep"""
        actions.speech.disable()
        actions.user.mouse_sleep()
        actions.user.notify("Talon sleeping")

    def talon_wake():
        """Wake Talon from sleep"""
        actions.speech.enable()
        actions.user.mouse_wake()
        actions.user.notify("Talon awake")

    def talon_wake_on_pop():
        """Use pop sound to wake from sleep"""
        global time_last_pop
        delta = time.monotonic() - time_last_pop
        if delta >= 0.1 and delta <= 0.3:
            actions.user.talon_wake()
        time_last_pop = time.monotonic()

    def talon_sleep_status():
        """Notify about Talon sleep status"""
        if actions.speech.enabled():
            actions.user.notify("Talon is: awake")
        else:
            actions.user.notify("Talon is: sleeping")

    def talon_sleep_update_phrase(words: list[str]) -> tuple[bool, str]:
        """Update spoke in words in case of sleep command"""
        if sleep_word in words:
            index = words.index(sleep_word)
            text = " ".join(words[: index + 1])
            if index < len(words) - 1:
                text += " ..."
            return True, text
        return False, " ".join(words)
