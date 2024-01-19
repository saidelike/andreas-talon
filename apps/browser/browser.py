from talon import Module, Context, actions, app

mod = Module()
ctx = Context()

# this context is only active when the "browser" tag is enabled
ctx.matches = r"""
tag: browser
"""

browser_name = "Firefox" if app.platform == "windows" else "firefox"


# "browser" has built-in actions that we override here
@ctx.action_class("browser")
class BrowserActions:
    # Focus address bar
    def focus_address():
        actions.key("ctrl-l")

    # Go to home page
    def go_home():
        actions.key("alt-home")

    # Go to a new URL
    def go(url: str):
        actions.browser.focus_address()
        actions.sleep("100ms")
        actions.insert(url)
        actions.key("enter")

    # Focus the search box
    def focus_search():
        actions.focus_address()

    # Submit the current form
    def submit_form():
        actions.key("enter")

    # Go back in the history
    def go_back():
        actions.key("alt-left")

    # Go forward in the history
    def go_forward():
        actions.key("alt-right")

    # Reload current page
    def reload():
        actions.key("ctrl-r")

    # Reload current page (harder)
    def reload_hard():
        actions.key("ctrl-shift-r")

    # Open or close the developer tools
    def toggle_dev_tools():
        actions.key("ctrl-shift-i")

    # Show recently visited pages
    def show_history():
        actions.key("ctrl-h")

    # Show download list
    def show_downloads():
        actions.key("ctrl-j")

    # Bookmark the current page
    def bookmark():
        actions.key("ctrl-d")

    # Open the Bookmarks editor
    def bookmarks():
        actions.key("ctrl-shift-O")

    # Toggle the bookmarks bar
    def bookmarks_bar():
        actions.key("ctrl-shift-b")

    # Bookmark all open tabs
    def bookmark_tabs():
        actions.key("ctrl-shift-d")

    # Show 'Clear Cache' dialog
    def show_clear_cache():
        actions.key("ctrl-shift-delete")


# "edit" has built-in actions that we override here
@ctx.action_class("edit")
class EditActions:
    # Move cursor to end of file (start of line)
    def file_end():
        actions.key("ctrl-end")


# these are general "user" actions that we override here
# to call our browser implementation
# TODO: why is this needed? if we comment this and say go back, it still works in Firefox
@ctx.action_class("user")
class UserActions:
    def go_back():
        actions.browser.go_back()

    def go_forward():
        actions.browser.go_forward()


# we define new actions that are "browser" related
# with a default behavior and that we can override later
@mod.action_class
class Actions:
    def browser_focus_default():
        """Focus default browser"""
        actions.user.window_focus_name(browser_name)

    # TODO: we could have a open_new_tab() generic action instead that works for all apps, not just browsers?
    def browser_open_new_tab(url: str):
        """Open url in new tab"""

    def browser_open(url: str):
        """Focus default browser and open url"""
        if actions.app.name() != browser_name:
            actions.user.browser_focus_default()
            actions.sleep("50ms")
        actions.user.browser_open_new_tab(url)

    def browser_search(text: str):
        """Focus browser and search for <text>"""
        # We pass the text in the URL field since it will automatically search for it instead.
        # Prefix with space to avoid matching search text with history
        actions.user.browser_open(f" {text}")

    def browser_search_selected():
        """Focus browser and search for selected text"""
        text = actions.edit.selected_text()
        actions.user.browser_search(text)
