from talon import (
    Context,
    Module,
    actions,
    app,
    storage,
)
from typing import Optional

mod = Module()

mod.tag("eye_tracker", "Indicates that the eye tracker is enabled")
mod.tag(
    "eye_tracker_frozen",
    "Indicates that the eye tracker cursor position updating is frozen",
)


ctx = Context()

ctx_eye_tracker = Context()
ctx_eye_tracker.matches = r"""
tag: user.eye_tracker
"""

ctx_frozen = Context()
ctx_frozen.matches = r"""
tag: user.eye_tracker_frozen
"""


@ctx_eye_tracker.action_class("user")
class EyeTrackerActions:
    def mouse_on_pop():
        actions.user.mouse_click_with_conditions()

    def mouse_control_toggle(enable: Optional[bool] = None):
        mouse_control_toggle(enable if enable is not None else False)


@ctx_frozen.action_class("user")
class FrozenActions:
    def mouse_on_pop():
        """Frozen mouse on pop handler"""
        actions.user.mouse_click_with_conditions()

    def mouse_freeze_toggle(freeze: Optional[bool] = None):
        """Toggle freeze cursor position updates for the eye tracker"""
        mouse_freeze_toggle(freeze if freeze is not None else False)


@mod.action_class
class Actions:
    def mouse_control_toggle(enable: Optional[bool] = None):
        """Toggle enable/disable for the eye tracker"""
        mouse_control_toggle(enable if enable is not None else True)

    def mouse_freeze_toggle(freeze: Optional[bool] = None):
        """Toggle freeze cursor position updates for the eye tracker"""
        mouse_freeze_toggle(freeze if freeze is not None else True)

    def mouse_wake():
        """Set control mouse to earlier state"""
        tracking_control = storage.get("tracking_control", False)
        control_toggle(tracking_control)

    def mouse_sleep():
        """Disables control mouse and scroll"""
        actions.user.mouse_scroll_stop()
        actions.user.mouse_release_held_buttons()
        control_toggle(False)


def control_toggle(enable: bool) -> bool:
    actions.tracking.control_toggle(enable)
    if actions.tracking.control_enabled():
        ctx.tags = ["user.eye_tracker"]
        return True
    else:
        ctx.tags = []
        return False


def mouse_control_toggle(enable: bool):
    enabled = control_toggle(enable)
    storage.set("tracking_control", enabled)
    actions.user.notify(f"Control mouse: {enabled}")


def mouse_freeze_toggle(freeze: bool):
    if freeze:
        control_toggle(False)
        ctx.tags = ["user.eye_tracker_frozen"]
    else:
        control_toggle(True)


def on_launch():
    """Restore eye tracker after a Talon restart"""
    if actions.user.talon_was_restart():
        actions.user.mouse_wake()


app.register("launch", on_launch)
