from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: windows
"""


@ctx.action_class("user")
class UserActions:
    def system_shutdown():
        shutdown("s /t 0")

    def system_restart():
        shutdown("r /t 0")

    def system_hibernate():
        shutdown("h")
        actions.key("enter")

    def system_lock():
        actions.user.exec("rundll32.exe user32.dll,LockWorkStation")


def shutdown(flag: str):
    actions.key("super-r")
    actions.sleep("50ms")
    actions.insert(f"shutdown /{flag}")
