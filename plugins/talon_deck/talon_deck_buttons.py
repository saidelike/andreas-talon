from talon import Module, Context, actions, scope


mod = Module()
ctx = Context()

ctx_command = Context()
ctx_command.matches = r"""
mode: command
"""

ctx_dictation = Context()
ctx_dictation.matches = r"""
mode: dictation
"""

ctx_sleep = Context()
ctx_sleep.matches = r"""
mode: sleep
"""

ctx_eye_tracker = Context()
ctx_eye_tracker.matches = r"""
tag: user.eye_tracker
"""

ctx_eye_tracker_frozen = Context()
ctx_eye_tracker_frozen.matches = r"""
tag: user.eye_tracker_frozen
"""

ctx_vscode = Context()
ctx_vscode.matches = r"""
mode: command
mode: dictation
app: vscode
"""


@ctx.action_class("user")
class Actions:
    def sound_microphone_enable_event():
        actions.user.talon_deck_update()
        actions.next()

    def talon_deck_get_buttons():
        return get_microphone_buttons()


@ctx_command.action_class("user")
class CommandActions:
    def talon_deck_get_buttons():
        return [
            *actions.next(),
            {"icon": "commandMode3", "action": "user.talon_sleep()", "order": 0},
            *get_code_language_buttons(),
        ]


@ctx_dictation.action_class("user")
class DictationActions:
    def talon_deck_get_buttons():
        return [
            *actions.next(),
            {"icon": get_language(), "action": "user.command_mode()", "order": 0},
        ]


@ctx_sleep.action_class("user")
class SleepActions:
    def talon_deck_get_buttons():
        return [
            *actions.next(),
            {"icon": "sleepMode", "action": "user.talon_wake()", "order": 0},
        ]


@ctx_eye_tracker.action_class("user")
class EyeTrackerActions:
    def talon_deck_get_buttons() -> list[dict]:
        return [
            *actions.next(),
            {"icon": "eyeTracking"},
        ]


@ctx_eye_tracker_frozen.action_class("user")
class EyeTrackerFrozenActions:
    def talon_deck_get_buttons() -> list[dict]:
        return [
            *actions.next(),
            {"icon": "eyeTracking2", "action": "user.mouse_control_toggle(True)"},
        ]


@ctx_vscode.action_class("user")
class VscodeActions:
    def talon_deck_get_buttons() -> list[dict]:
        return [
            *actions.next(),
            {"icon": "vscode"},
        ]


def get_language():
    language = scope.get("language", "en_US")
    if isinstance(language, str):
        return language
    for lang in language:
        if "_" in lang:
            return lang


def get_code_language_buttons():
    lang = actions.code.language()
    if lang:
        return [{"icon": lang}]
    return []


def get_microphone_buttons():
    microphone_enabled = actions.user.sound_microphone_enabled()
    if microphone_enabled and actions.speech.enabled():
        return []
    icon = "On" if microphone_enabled else "Off"
    return [
        {
            "icon": f"microphone{icon}",
            "action": f"user.sound_microphone_enable({not microphone_enabled})",
        }
    ]
