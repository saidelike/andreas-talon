from talon import Module, actions, app, ui, settings
from dataclasses import dataclass
import time, os
from ...imgui import imgui
from ..analyze_phrase.types import AnalyzedPhrase

mod = Module()
history = []
mod.setting("command_history_size", int, default=25)

# If greater then zero ttl(time to live) is used to auto hide older history entries
ttl_setting = 0


# Wrapping in a data class is a simple solution to get a unique identifier for each string even if they are identical
@dataclass
class HistoryEntry:
    phrase: str
    actions: list
    ttl: int
    phrase_start: bool
    path: str
    rule: str


# this place it in the top left corner of my left screen
@imgui.open(screen=ui.screen.screens()[1], x=0.0, y=0.0)
def gui(gui: imgui.GUI):
    t = time.monotonic()
    use_ttl = ttl_setting > 0
    add_line = False
    # Hide entries outside of display size
    for entry in history:
        # If ttl is disabled or time hasn't passed yet: show command.
        if not use_ttl or entry.ttl < 0 or entry.ttl >= t:
            if add_line and entry.phrase_start:
                gui.line()
            add_line = True
            gui.header(entry.phrase)
            gui.text(f"{os.path.relpath(entry.path, 'user')} \"{entry.rule}\"")
            for action in entry.actions:
                gui.text(f" {action.name}: {action.explanation}")


def command_history_append(analyzed_phrase: AnalyzedPhrase):
    """Append command to history"""
    global history
    ttl = time.monotonic() + ttl_setting
    for i, cmd in enumerate(analyzed_phrase.commands):
        history.append(
            HistoryEntry(cmd.phrase, cmd.actions, ttl, i == 0, cmd.path, cmd.rule)
        )
    size = settings.get("user.command_history_size")
    history = history[-size:]


# we define new actions that are "command history" related
@mod.action_class
class Actions:
    def command_history_toggle():
        """Toggles viewing the history"""
        if gui.showing:
            gui.hide()
        else:
            gui.show()

    def command_history_clear():
        """Clear the history"""
        global history
        history = []


def on_ready():
    actions.user.command_history_toggle()


app.register("ready", on_ready)
