from pathlib import Path
from talon import app, Module, Context, actions
from os import path, environ

from talon import Context, Module, actions
from dataclasses import dataclass


@dataclass
class Application:
    app: str
    spoken_form: str


applications = [
    Application("cmd", "command"),
    Application("windows_explorer", "windows explorer"),
    Application("windbg", "wind bag"),
]


mod = Module()
# mod.tag("vmware", "Tag for indicating we are running inside vmware")
mod.list("vmware_application", "List of applications we can run inside vmware")
for a in applications:
    mod.tag(
        f"forced_app_{a.app}", f"tag to enable the {a.app} application inside vmware"
    )

    mod.apps[
        a.app
    ] = rf"""
    tag: user.forced_app_{a.app}
    """

mod.apps.vmware = r"""
os: windows
app.name: VMware Workstation
"""

ctx = Context()

ctx = Context()
ctx.matches = r"""
app: vmware
"""

ctx.lists["user.vmware_application"] = {a.spoken_form: a.app for a in applications}


# we define new actions that are "vmware" related
@mod.action_class
class Actions:
    def vmware_set_application(app: str):
        """Forces the active application to <app>"""
        # Update tags to force a context refresh.
        # Necessary to first set an empty list otherwise you can't move from one forced application to another.
        ctx.tags = []
        ctx.tags = [f"user.forced_app_{app}"]

    def vmware_clear_applications():
        """Clears the forced application"""
        ctx.tags = []
