from talon import Context, actions

ctx = Context()
ctx.matches = r"""
app: vscode
win.title: /windows_kernel_exploitation/
"""


@ctx.action_class("user")
class Actions:
    def vscode_build_program():
        actions.user.vscode_run_terminal_command("./build_slides.bat")


ctx = Context()
ctx.matches = r"""
app: vscode
win.title: /cursorless_fork/
win.title: /command-server_fork/
"""


@ctx.action_class("user")
class Actions:
    def vscode_build_program():
        actions.user.vscode_run_terminal_command("pnpm compile")

    def vscode_run_program():
        actions.user.exec("C:\\Program Files\\Neovim\\bin\\nvim-qt.exe")
        actions.sleep("2000ms")
        actions.key("alt-tab")  # actions.user.window_focus_last()
        actions.sleep("2000ms")
        actions.user.vscode_debug_program(4000)

    def vscode_debug_program(sleep_time: int = 2000):
        # show the debug console
        actions.user.vscode("workbench.debug.action.toggleRepl")
        # attach to the node process
        actions.user.vscode("extension.pwa-node-debug.attachNodeProcess")
        actions.insert("Node")
        actions.sleep(f"{sleep_time}ms")
        actions.key("enter")
