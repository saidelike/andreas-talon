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
    "flick": "focusElement",
    "blank": "openInNewTab",
    "stash": "openInBackgroundTab",
    "show": "showLink",
    "hover": "hoverElement",
    "copy": "copyLink",
    "copy link": "copyLink",
    "copy mark": "copyMarkdownLink",
    "copy text": "copyElementTextContent",
    "crown": "scrollElementToTop",
    "bottom": "scrollElementToBottom",
    "center": "scrollElementToCenter",
    "upper": "scrollUpAtElement",
    "downer": "scrollDownAtElement",
    "include": "includeExtraSelectors",
    "exclude": "excludeExtraSelectors",
}

ctx.lists["user.rango_without_target_action"] = {
    "hint exclude singles": "includeSingleLetterHints",
    "hint include singles": "excludeSingleLetterHints",
    "hints toggle": "toggleHints",
    "hints switch": "toggleHints",
    "hints refresh": "refreshHints",
    "dismiss": "unhoverAll",
    "tab clone": "cloneCurrentTab",
    "up again": "scrollUpAtElement",
    "down again": "scrollDownAtElement",
    "hint extra": "displayExtraHints",
    "hint more": "displayExcludedHints",
    "hint less": "displayLessHints",
    "custom hints save": "confirmSelectorsCustomization",
    "custom hints reset": "resetCustomSelectors",
    "hint bigger": "increaseHintSize",
    "hint smaller": "decreaseHintSize",
    "some more": "includeOrExcludeMoreSelectors",
    "some less": "includeOrExcludeLessSelectors",
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
