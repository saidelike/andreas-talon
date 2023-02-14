import time
from talon import Module, Context, actions, cron

mod = Module()
mod.tag("av")

settings_timeout = mod.setting(
    "foot_switch_timeout",
    type=bool,
    default=True,
    desc="If true timeout will be used to decide if the foot switch was held or not",
)

current_state = [False, False, False, False]
last_state = [False, False, False, False]
timestamps = [0, 0, 0, 0]
scroll_reversed = False
hold_timeout = 0.2


def on_interval():
    for key in range(4):
        if current_state[key] != last_state[key]:
            last_state[key] = current_state[key]
            # Key is pressed down
            if current_state[key]:
                call_down(key)
            # Key is released after specified hold time out. ie key was held.
            elif (
                not settings_timeout.get()
                or time.perf_counter() - timestamps[key] > hold_timeout
            ):
                call_up(key)


cron.interval("16ms", on_interval)


@mod.action_class
class Actions:
    def foot_switch_down(key: int):
        """Foot switch key down event. Top(0), Center(1), Left(2), Right(3)"""
        timestamps[key] = time.perf_counter()
        current_state[key] = True

    def foot_switch_up(key: int):
        """Foot switch key up event. Top(0), Center(1), Left(2), Right(3)"""
        current_state[key] = False

    def foot_switch_scroll_reverse():
        """Reverse scroll direction using foot switch"""
        global scroll_reversed
        scroll_reversed = not scroll_reversed

    def foot_switch_top_down():
        """Foot switch button top:down"""

    def foot_switch_top_up():
        """Foot switch button top:up"""

    def foot_switch_center_down():
        """Foot switch button center:down"""

    def foot_switch_center_up():
        """Foot switch button center:up"""

    def foot_switch_left_down():
        """Foot switch button left:down"""

    def foot_switch_left_up():
        """Foot switch button left:up"""

    def foot_switch_right_down():
        """Foot switch button right:down"""

    def foot_switch_right_up():
        """Foot switch button right:up"""


# Default implementation
ctx = Context()


@ctx.action_class("user")
class UserActions:
    def foot_switch_top_down():
        if scroll_reversed:
            actions.user.mouse_scrolling("down")
        else:
            actions.user.mouse_scrolling("up")

    def foot_switch_top_up():
        actions.user.mouse_stop()

    def foot_switch_center_down():
        if scroll_reversed:
            actions.user.mouse_scrolling("up")
        else:
            actions.user.mouse_scrolling("down")

    def foot_switch_center_up():
        actions.user.mouse_stop()

    def foot_switch_left_down():
        actions.user.go_back()

    def foot_switch_left_up():
        pass

    def foot_switch_right_down():
        pass

    def foot_switch_right_up():
        pass


# Default non sleep implementation
ctx_wake = Context()
ctx_wake.matches = r"""
not mode: sleep
"""


@ctx_wake.action_class("user")
class UserWakeActions:
    def foot_switch_right_down():
        actions.user.mouse_sleep_toggle()

    def foot_switch_right_up():
        actions.user.mouse_sleep_toggle()


# Audio / Video conferencing
ctx_av = Context()
ctx_av.matches = r"""
mode: all
tag: user.av
"""


@ctx_av.action_class("user")
class AvActions:
    def foot_switch_left_down():
        actions.user.mute_microphone()

    def foot_switch_left_up():
        actions.user.mute_microphone()


def call_down(key: int):
    # Top
    if key == 0:
        actions.user.foot_switch_top_down()
    # Center
    elif key == 1:
        actions.user.foot_switch_center_down()
    # Left
    elif key == 2:
        actions.user.foot_switch_left_down()
    # Right
    elif key == 3:
        actions.user.foot_switch_right_down()


def call_up(key: int):
    # Top
    if key == 0:
        actions.user.foot_switch_top_up()
    # Center
    elif key == 1:
        actions.user.foot_switch_center_up()
    # Left
    elif key == 2:
        actions.user.foot_switch_left_up()
    # Right
    elif key == 3:
        actions.user.foot_switch_right_up()
