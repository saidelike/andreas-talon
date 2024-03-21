from talon import Module, Context, actions, ui

mod = Module()
ctx = Context()

ctx.matches = r"""
tag: terminal
"""


@ctx.action_class("user")
class Actions:
    def file_manager_go_step(path: str):
        actions.insert(f"cd {path}")


@mod.action_class
class Actions:
    def list_directory(path: str):
        """Lists the current directory"""
        actions.insert(f"ls {path}\n")

    def list_directory_all(path: str):
        """Lists the current directory including hidden files"""
        actions.insert(f"ls -a {path}\n")

    def list_directory_long(path: str):
        """Lists the current directory with long format, including hidden files and human readable file sizes"""
        actions.insert(f"ls -lah {path}\n")

    def make_directory(path: str):
        """Create a directory"""
        actions.insert(f"mkdir {path}")
