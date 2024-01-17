from talon import Module, Context, actions
import re

mod = Module()
ctx = Context()

mod.apps.firefox = """
os: windows
and app.name: Firefox
os: windows
and app.exe: firefox.exe
"""

ctx.matches = r"""
app: firefox
"""

mod.list("rango_with_target_action", "List of Rango actions used WITH a target")
mod.list("rango_without_target_action", "List of Rango actions used WITHOUT a target")

# https://github.com/david-tejada/rango
ctx.lists["user.rango_with_target_action"] = {
    "click": "clickElement",
    "open": "openInNewTab", # rango default is "blank"
    "stash": "openInBackgroundTab",
    "show": "showLink",
    "hover": "hoverElement",
    "copy": "copyLink", # rango default is "copy [link]"
    "copy mark": "copyMarkdownLink",
    "copy text": "copyElementTextContent",
    "crown": "scrollElementToTop",
    "bottom": "scrollElementToBottom",
    "center": "scrollElementToCenter",
    "upper": "scrollUpAtElement",
    "downer": "scrollDownAtElement",
    "hunt include": "includeExtraSelectors", # rango default is "include"
    "hunt exclude": "excludeExtraSelectors", # rango default is "exclude"
}

ctx.lists["user.rango_without_target_action"] = {
    "rango single": "includeSingleLetterHints", # rango default is "hint exclude singles"
    "rango double": "excludeSingleLetterHints", # rango default is "hint include singles"
    "hunt": "toggleHints", # rango default is hints "(toggle | switch)"
    "hunt refresh": "refreshHints", # rango default is "hints refresh"
    "hover nothing": "unhoverAll", # rango default is "dismiss"
    "tab clone": "cloneCurrentTab",
    "upper again": "scrollUpAtElement", # rango default is "up again"
    "downer again": "scrollDownAtElement", # rango default is "down again"
    "hunt extra": "displayExtraHints", # rango default is "hint extra"
    "hunt more": "displayExcludedHints", # rango default is "hint more"
    "hunt less": "displayLessHints", # rango default is "hint less"
    "hunt save": "confirmSelectorsCustomization", # rango default is "custom hints save"
    "hunt reset": "resetCustomSelectors", # rango default is "custom hints reset"
    "hunt bigger": "increaseHintSize", # rango default is "hint bigger"
    "hunt smaller": "decreaseHintSize", # rango default is "hint smaller"
    "hunt some more": "includeOrExcludeMoreSelectors", # rango default is "some more"
    "hunt some less": "includeOrExcludeLessSelectors", # rango default is "some less"
}

url_pattern = re.compile(r"https?://\S+")


@ctx.action_class("browser")
class BrowserActions:
    def address() -> str:
        # Rango adds address to window title
        title = actions.win.title()
        match = url_pattern.search(title)
        if match:
            return match.group()
        return ""

    def open_private_window():
        actions.key("ctrl-shift-p")

    def show_extensions():
        actions.key("ctrl-shift-a")


@ctx.action_class("app")
class AppActions:
    def preferences():
        actions.user.browser_open_new_tab("about:preferences")

    # ----- Rango -----
    def tab_detach():
        actions.user.rango_command_without_target("moveCurrentTabToNewWindow")


@ctx.action_class("edit")
class EditActions:
    def find(text: str = None):
        actions.key("ctrl-f")
        if text:
            actions.sleep("50ms")
            actions.insert(text)


@ctx.action_class("user")
class UserActions:
    def tab_jump(number: int):
        if number < 9:
            actions.key(f"ctrl-{number}")

    def tab_final():
        actions.key("ctrl-9")

    def browser_open_new_tab(url: str):
        actions.browser.focus_address()
        actions.sleep("50ms")
        actions.insert(url)
        actions.sleep("50ms")
        actions.key("alt-enter")

    # ----- Rango -----
    def tab_back():
        actions.user.rango_command_without_target("focusPreviousTab")

    def scroll_up():
        actions.user.rango_command_without_target("scrollUpPage", 0.1)

    def scroll_down():
        actions.user.rango_command_without_target("scrollDownPage", 0.1)

    def scroll_up_half_page():
        actions.user.rango_command_without_target("scrollUpPage", 0.45)

    def scroll_down_half_page():
        actions.user.rango_command_without_target("scrollDownPage", 0.45)

    def scroll_up_page():
        actions.user.rango_command_without_target("scrollUpPage", 0.9)

    def scroll_down_page():
        actions.user.rango_command_without_target("scrollDownPage", 0.9)


# ----- LINUX -----

ctx_linux = Context()
ctx_linux.matches = r"""
os: linux
app: firefox
"""


@ctx_linux.action_class("user")
class UserActionsLinux:
    def tab_final():
        actions.key("alt-9")

    def tab_jump(number: int):
        if number < 9:
            actions.key(f"alt-{number}")
