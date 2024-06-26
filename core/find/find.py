from talon import Module, actions

mod = Module()
# Declare a new global "user.find_and_replace" tag
mod.tag("find_and_replace")


# we define new actions that are "find_and_replace" related
@mod.action_class
class Actions:
    def find_file(text: str = None):
        """Find file <text>"""

    def find_everywhere(text: str = None):
        """Find in entire project/all files"""
        actions.key("ctrl-shift-f")
        if text:
            actions.insert(text)

    def find_everywhere_next():
        """Find next result in entire project/all files"""

    def find_everywhere_previous():
        """Find previous result in entire project/all files"""

    def find_replace(text: str = None):
        """Find and replace in current file/editor"""
        actions.key("ctrl-h")
        if text:
            actions.insert(text)

    def find_replace_everywhere(text: str = None):
        """Find and replace in entire project/all files"""
        actions.key("ctrl-shift-h")
        if text:
            actions.insert(text)

    def find_replace_confirm():
        """Confirm replace current"""

    def find_replace_confirm_all():
        """Confirm replace all"""

    def find_toggle_match_by_case():
        """Toggles find match by case sensitivity"""

    def find_toggle_match_by_word():
        """Toggles find match by whole words"""

    def find_toggle_match_by_regex():
        """Toggles find match by regex"""

    def find_replace_toggle_preserve_case():
        """Toggles replace preserve case"""
