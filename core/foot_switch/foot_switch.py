from talon import Module, Context, actions, cron
import time

HOLD_TIMEOUT = 0.2

LEFT = 0
CENTER = 1
RIGHT = 2
TOP = 3

DOWN = 0
UP = 1

mod = Module()
current_state = [UP, UP, UP, UP]
last_state = [UP, UP, UP, UP]
timestamps = [0, 0, 0, 0]
scroll_reversed = False
cron_job = None


# the whole logic about calling foot switch "user"-actions is done here
def on_interval():
    for key in range(4):
        if last_state[key] != current_state[key]:
            last_state[key] = current_state[key]

            if current_state[key] == DOWN:
                call_down(key)
            else:
                held = time.perf_counter() - timestamps[key] > HOLD_TIMEOUT
                call_up(key, held)


# In a hotkey event, eg "key(ctrl:down)", any key you press with key/insert
# actions will be combined with ctrl since it's still held. Just updating a
# boolean in the actual hotkey event and reading it asynchronously with cron
# gets around this issue.
cron.interval("16ms", on_interval)


# the whole logic about calling foot switch "user"-actions is done here
def call_down(key: int):
    if key == LEFT:
        actions.user.foot_switch_left_down()
    elif key == CENTER:
        actions.user.foot_switch_center_down()
    elif key == RIGHT:
        actions.user.foot_switch_right_down()
    elif key == TOP:
        actions.user.foot_switch_top_down()


# the whole logic about calling foot switch "user"-actions is done here
def call_up(key: int, held: bool):
    if key == LEFT:
        actions.user.foot_switch_left_up(held)
    elif key == CENTER:
        actions.user.foot_switch_center_up(held)
    elif key == RIGHT:
        actions.user.foot_switch_right_up(held)
    elif key == TOP:
        actions.user.foot_switch_top_up(held)


# we define new actions that are "foot switch" related
@mod.action_class
class Actions:
    def foot_switch_down_event(key: int):
        """Foot switch key down event. Left(0), Center(1), Right(2), Top(3)"""
        timestamps[key] = time.perf_counter()
        current_state[key] = DOWN

    def foot_switch_up_event(key: int):
        """Foot switch key up event. Left(0), Center(1), Right(2), Top(3)"""
        current_state[key] = UP

    def foot_switch_scroll_reverse():
        """Reverse scroll direction using foot switch"""
        global scroll_reversed
        scroll_reversed = not scroll_reversed

    def foot_switch_top_down():
        """Foot switch button top:down"""

    def foot_switch_top_up(held: bool):
        """Foot switch button top:up"""

    def foot_switch_center_down():
        """Foot switch button center:down"""

    def foot_switch_center_up(held: bool):
        """Foot switch button center:up"""

    def foot_switch_left_down():
        """Foot switch button left:down"""

    def foot_switch_left_up(held: bool):
        """Foot switch button left:up"""

    def foot_switch_right_down():
        """Foot switch button right:down"""

    def foot_switch_right_up(held: bool):
        """Foot switch button right:up"""


# ---------- Default implementation ----------
ctx = Context()


@ctx.action_class("user")
class UserActions:
    def foot_switch_top_down():
        if scroll_reversed:
            actions.user.mouse_scrolling("down")
        else:
            actions.user.mouse_scrolling("up")

    def foot_switch_top_up(held: bool):
        if held:
            actions.user.mouse_scroll_stop()

    def foot_switch_center_down():
        if scroll_reversed:
            actions.user.mouse_scrolling("up")
        else:
            actions.user.mouse_scrolling("down")

    def foot_switch_center_up(held: bool):
        if held:
            actions.user.mouse_scroll_stop()

    def foot_switch_left_down():
        global cron_job
        cron_job = cron.after(
            f"{int(HOLD_TIMEOUT*1000)}ms", actions.user.quick_pick_show
        )

    def foot_switch_left_up(held: bool):
        global cron_job
        cron.cancel(cron_job)
        cron_job = None
        if not held:
            actions.user.go_back()

    def foot_switch_right_down():
        pass

    def foot_switch_right_up(held: bool):
        pass


# ---------- Default non-sleep implementation ----------
ctx_eye_tracker = Context()
# this context is only active when eye tracking is being currently used or temporarily frozen
ctx_eye_tracker.matches = r"""
tag: user.eye_tracker
tag: user.eye_tracker_frozen
"""


@ctx_eye_tracker.action_class("user")
class EyeTrackerActions:
    def foot_switch_right_down():
        actions.user.mouse_freeze_toggle()

    def foot_switch_right_up(held: bool):
        if held:
            actions.user.mouse_freeze_toggle()


# ---------- Audio conferencing ----------
ctx_voip = Context()
# this context is only active when the "user.voip" tag is enabled
# in any mode, including when Talon is sleeping
ctx_voip.matches = r"""
mode: command
mode: dictation
mode: sleep
tag: user.voip
"""


@ctx_voip.action_class("user")
class VoipActions:
    def foot_switch_left_down():
        actions.user.mute_microphone()

    def foot_switch_left_up(held: bool):
        if held:
            actions.user.mute_microphone()
