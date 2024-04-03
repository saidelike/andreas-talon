from typing import Optional
from talon import Module, Context, actions
import json
import re

mod = Module()
mod.list("vscode_sessions", "Known vscode sessions/workspaces")

# we define what it is to be a "vscode" app
mod.apps.vscode = r"""
os: windows
and app.exe: code.exe
os: linux
and app.name: Code
"""


# this context is only active when the above "vscode" app is enabled
ctx = Context()
ctx.matches = r"""
app: vscode
"""


# these are Talon-defined "app" actions (only grouped for clarity) that we override
@ctx.action_class("app")
class AppActions:
    # Open a new window
    def window_open():
        actions.user.vscode("workbench.action.newWindow")

    # Open a new tab
    def tab_open():
        actions.user.vscode("workbench.action.files.newUntitledFile")

    # Switch to previous tab for this window
    def tab_previous():
        actions.user.vscode("workbench.action.previousEditorInGroup")

    # Switch to next tab for this window
    def tab_next():
        actions.user.vscode("workbench.action.nextEditorInGroup")

    # Open app preferences
    def preferences():
        actions.user.vscode("workbench.action.openGlobalSettings")


# these are Talon-defined "code" actions (only grouped for clarity) that we override
@ctx.action_class("code")
class CodeActions:
    # Toggle comments on the current line(s)
    def toggle_comment():
        actions.user.vscode("editor.action.commentLine")

    # Trigger code autocomplete
    def complete():
        actions.user.vscode("editor.action.triggerSuggest")


# these are Talon-defined "edit" actions (only grouped for clarity) that we override
@ctx.action_class("edit")
class EditActions:
    # Save current document
    def save():
        actions.user.vscode("hideSuggestWidget")
        actions.next()

    # Get currently selected text
    def selected_text() -> str:
        try:
            selectedTexts = actions.user.vscode_get("andreas.getSelectedText")
            if selectedTexts is not None:
                return "\n".join(selectedTexts)
        except Exception as ex:
            print(f"EXCEPTION: {ex}")

        return actions.next()

    # Clear current selection
    def select_none():
        actions.key("escape")

    # ----- Word -----
    # Delete word under cursor
    def delete_word():
        empty_selection()
        actions.next()

    # ----- Line commands -----
    # Swap the current line with the line above
    def line_swap_up():
        actions.user.vscode("editor.action.moveLinesUpAction")

    # Swap the current line with the line below
    def line_swap_down():
        actions.user.vscode("editor.action.moveLinesDownAction")

    # Clones specified line at current position
    def line_clone():
        actions.user.vscode("editor.action.copyLinesDownAction")

    # Insert line above cursor
    def line_insert_up():
        actions.user.vscode("editor.action.insertLineBefore")

    # Don't use RPC since some vscode extension(eg markdown) has specific behavior on enter
    # def line_insert_down():
    # actions.user.vscode("editor.action.insertLineAfter")

    # Delete line under cursor
    def delete_line():
        actions.user.vscode("editor.action.deleteLines")

    # Move cursor to line <n>
    def jump_line(n: int):
        actions.user.vscode("andreas.goToLine", n)

    # ----- Indent -----
    # Add a tab stop of indentation
    def indent_more():
        actions.user.vscode("editor.action.indentLines")

    # Remove a tab stop of indentation
    def indent_less():
        actions.user.vscode("editor.action.outdentLines")

    # ----- Zoom -----
    # Zoom to original size
    def zoom_reset():
        actions.user.vscode("workbench.action.zoomReset")


@ctx.action_class("user")
class UserActions:
    # ----- Navigation -----
    # inherited when "user.navigation" tag is enabled
    def go_back():
        actions.user.vscode("workbench.action.navigateBack")

    def go_forward():
        actions.user.vscode("workbench.action.navigateForward")

    # inherited from "edit_line.py"
    def line_middle():
        actions.user.vscode("andreas.lineMiddle")

    # ----- Find / Replace -----
    # inherited when "user.find" tag is enabled
    def find_everywhere(text: str = None):
        actions.user.vscode("workbench.action.findInFiles")
        if text:
            actions.sleep("50ms")
            actions.insert(text)

    def find_everywhere_next():
        actions.user.vscode("search.action.focusNextSearchResult")

    def find_everywhere_previous():
        actions.user.vscode("search.action.focusPreviousSearchResult")

    def find_file(text: str = None):
        actions.user.vscode("workbench.action.quickOpen")
        if text:
            actions.sleep("50ms")
            actions.insert(text)

    def find_toggle_match_by_case():
        actions.key("alt-c")

    def find_toggle_match_by_word():
        actions.key("alt-w")

    def find_toggle_match_by_regex():
        actions.key("alt-r")

    def find_replace_toggle_preserve_case():
        actions.key("alt-p")

    def find_replace_confirm():
        actions.key("enter")

    def find_replace_confirm_all():
        actions.key("ctrl-alt-enter")

    # ----- Tabs -----
    # inherited when "user.tabs" tag is enabled
    def tab_back():
        actions.user.vscode("workbench.action.openPreviousRecentlyUsedEditorInGroup")

    def tab_final():
        actions.user.vscode("workbench.action.lastEditorInGroup")

    def tab_jump(number: int):
        actions.user.vscode("andreas.openEditorAtIndex", number - 1)

    def tab_jump_from_back(number: int):
        actions.user.vscode("andreas.openEditorAtIndex", -number)

    # ----- Scroll -----
    # inherited when "user.scroll" tag is enabled
    def scroll_up():
        actions.key("ctrl-up")

    def scroll_down():
        actions.key("ctrl-down")

    def scroll_up_page():
        actions.key("alt-pageup")

    def scroll_down_page():
        actions.key("alt-pagedown")

    def scroll_up_half_page():
        actions.user.vscode("editorScroll", {"to": "up", "by": "halfPage"})

    def scroll_down_half_page():
        actions.user.vscode("editorScroll", {"to": "down", "by": "halfPage"})

    # ----- Word -----
    # inherited from "edit_word.py"
    def cut_word():
        empty_selection()
        actions.next()

    def copy_word():
        empty_selection()
        actions.next()

    def paste_word():
        empty_selection()
        actions.next()

    # ----- Dictation -----
    # inherited from "text_and_dictation.py"
    def dictation_get_context() -> tuple[Optional[str], Optional[str]]:
        try:
            context = actions.user.vscode_get("andreas.getDictationContext")
        except Exception:
            context = None

        if context is not None:
            return (context["before"], context["after"])
        return (None, None)

    # ----- Snippets -----
    # inherited from "snippets_insert.py"
    def insert_snippet(body: str):
        # actions.user.cursorless_insert_snippet(body)
        actions.user.vscode("editor.action.insertSnippet", {"snippet": body})

    # ----- Text getters -----
    # inherited from "code_generic_language.py"
    def code_get_class_name() -> Optional[str]:
        return actions.user.vscode_get("andreas.getClassName")

    def code_get_open_tag_name() -> Optional[str]:
        return actions.user.vscode_get("andreas.getOpenTagName")

    # ----- Delimiters -----
    # vscode automatically appends the right delimiter if the selection is a word
    def delimiters_pair_wrap_selection_with(left: str, right: str):
        selected = actions.edit.selected_text()
        if " " not in selected:
            right = ""
        actions.user.delimiters_pair_insert(left, right, selected)

    # ----- Split -----
    def split_move_up():
        actions.user.vscode("workbench.action.moveEditorToAboveGroup")

    def split_move_down():
        actions.user.vscode("workbench.action.moveEditorToBelowGroup")

    def split_move_left():
        actions.user.vscode("workbench.action.moveEditorToLeftGroup")

    def split_move_right():
        actions.user.vscode("workbench.action.moveEditorToRightGroup")

    def split_focus_up():
        actions.user.vscode("workbench.action.focusAboveGroup")

    def split_focus_down():
        actions.user.vscode("workbench.action.focusBelowGroup")

    def split_focus_left():
        actions.user.vscode("workbench.action.focusLeftGroup")

    def split_focus_right():
        actions.user.vscode("workbench.action.focusRightGroup")

    def split_focus_next():
        actions.user.vscode("workbench.action.focusNextGroup")

    # def split_focus_last():

    def split_shrink_width():
        actions.user.vscode("workbench.action.decreaseViewWidth")

    def split_shrink_height():
        actions.user.vscode("workbench.action.decreaseViewHeight")

    def split_expand_width():
        actions.user.vscode("workbench.action.increaseViewWidth")

    def split_expand_height():
        actions.user.vscode("workbench.action.increaseViewHeight")

    def split_layout_toggle():
        actions.user.vscode("workbench.action.toggleEditorGroupLayout")

    def split_layout_join_two_groups():
        actions.user.vscode("workbench.action.joinTwoGroups")

    def split_layout_clear():
        actions.user.vscode("workbench.action.editorLayoutSingle")

    def split_layout_toggle_maximize():
        actions.user.vscode("workbench.action.toggleMaximizeEditorGroup")


# we define new actions that are "vscode" related
@mod.action_class
class Actions:
    def save_without_formatting():
        """Save current document without formatting"""
        actions.user.vscode("hideSuggestWidget")
        actions.user.vscode("workbench.action.files.saveWithoutFormatting")

    def format_document():
        """Format document"""
        actions.user.vscode("editor.action.formatDocument")

    def vscode_find_recent(text: Optional[str] = None):
        """Find recent session, directory or file"""
        actions.user.vscode("workbench.action.openRecent")
        if text:
            actions.sleep("150ms")
            actions.insert(text)

    def vscode_take_word(cursorless_target: dict, repeats: int):
        """Take word on cursorless target with number of repeats"""
        actions.user.cursorless_command("setSelection", cursorless_target)
        text = actions.edit.selected_text()

        if re.match(r"[\wåäöÅÄÖ]", text):
            actions.edit.right()
        else:
            repeats -= 1

        # Select number of next instances
        for _ in range(repeats):
            actions.user.vscode("editor.action.addSelectionToNextFindMatch")

        # Select all instances
        if repeats < 0:
            actions.user.vscode("editor.action.selectHighlights")

    def change_language(language: str = ""):
        """Change language mode"""
        actions.user.vscode("workbench.action.editor.changeLanguageMode")
        if language:
            actions.insert(language)

    # https://www.youtube.com/watch?v=oWUJyDgz63k
    def copy_command_id():
        """Copy the command id of the focused menu item"""
        title = actions.win.title()
        if not title.startswith("Keyboard Shortcuts"):
            # it's expected to be run with the command palette open at least
            actions.key("tab:2 enter")
            actions.sleep("500ms")
        # now we should be in the Keyboard Shortcuts window
        json_text = actions.edit.selected_text()
        command_id = json.loads(json_text)["command"]
        actions.app.tab_close()
        actions.clip.set_text(command_id)

    def vscode_add_missing_imports():
        """Add all missing imports"""
        actions.user.vscode(
            "editor.action.sourceAction",
            {"kind": "source.addMissingImports", "apply": "first"},
        )

    def find_sibling_file():
        """Find sibling file based on file name"""
        full_name = actions.win.filename()
        index = full_name.rfind(".")
        if index < 0:
            return
        short_name = full_name[:index]
        extension = full_name[index + 1 :]
        sibling_extension = actions.user.get_extension_sibling(extension)
        if not sibling_extension:
            return
        sibling_full_name = f"{short_name}.{sibling_extension}"
        actions.user.find_file(sibling_full_name)

    # https://superuser.com/questions/1361113/open-file-from-vscode-file-explorer-using-keyboard
    def vscode_explore_file(direction: str = "up"):
        """open the next/previous file in the vscode bar explorer"""
        title = actions.win.title()
        if not title.endswith("focus:[Folders]"):
            actions.user.vscode("workbench.view.explorer")
        actions.key(direction)
        actions.key("space")

    def vscode_build_program():
        """Build the program"""
        actions.user.vscode("workbench.action.tasks.build")

    def vscode_run_program():
        """Run and debug the program"""
        actions.user.vscode("workbench.action.debug.run")

    def vscode_debug_program(sleep_time: int = 600):
        """Debug the program"""

    def vscode_run_terminal_command(cmd: str):
        """Run terminal command"""
        actions.edit.save()
        actions.user.vscode("workbench.action.terminal.toggleTerminal")
        actions.sleep("600ms")
        actions.insert(cmd)
        actions.sleep("100ms")
        actions.key("enter")


def empty_selection():
    if actions.edit.selected_text():
        actions.edit.right()
