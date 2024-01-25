from talon import Context, actions
import re


# this context is only active when the "vscode" app is enabled
ctx = Context()
ctx.matches = r"""
app: vscode
"""

# this context is only active when the "vscode" app is enabled and no language has been enforced
ctx_lang = Context()
ctx_lang.matches = r"""
app: vscode
not tag: user.code_language_forced
"""


# these are Talon-defined "win" actions (only grouped for clarity) that we override
@ctx.action_class("win")
class WinActions:
    # Return the open filename
    def filename():
        filename = actions.win.title().split(" - ")[0]
        if is_untitled(filename):
            return get_untitled_name(filename)
        if "." in filename:
            return filename
        return ""


# these are Talon-defined "code" actions (only grouped for clarity) that we override
@ctx_lang.action_class("code")
class LangCodeActions:
    # Return the active programming language
    def language() -> str:
        # New untitled files are markdown in vscode
        if is_untitled(actions.win.filename()):
            return "markdown"
        return actions.next()


UNTITLED_RE = re.compile(r"Untitled-\d$")


def is_untitled(filename: str):
    return UNTITLED_RE.search(filename) is not None


def get_untitled_name(filename: str):
    return UNTITLED_RE.search(filename).group()
