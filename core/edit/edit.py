from talon import Context, Module, actions, clip
import re

mod = Module()

# ---------- Paste insert ------

# Declare a new global "user.insert_paste_disabled" tag
mod.tag("insert_paste_disabled", "Never use paste to insert text")

ctx_insert_paste = Context()
ctx_insert_paste.matches = r"""
not tag: user.insert_paste_disabled
"""

# Matching strings that cannot be undone in a single step
PASTE_RE = re.compile(r"\s|[ /-]")


# by default we insert text by pasting it.
# but we allow disabling it by setting the "insert_paste_disabled" tag above
@ctx_insert_paste.action_class("main")
class MainActions:
    def insert(text: str):
        if re.search(PASTE_RE, text):
            actions.user.paste_text(text)
        else:
            actions.next(text)


# ----------------------


ctx = Context()


# these are Talon-defined "edit" actions (only grouped for clarity) that we override
@ctx.action_class("edit")
class EditActions:
    # ----- Navigation -----
    # Move cursor up one row
    def up():
        actions.key("up")

    # Move cursor down one row
    def down():
        actions.key("down")

    # Move cursor left one column
    def left():
        actions.key("left")

    # Move cursor right one column
    def right():
        actions.key("right")

    # Move cursor up one page
    def page_up():
        actions.key("pageup")

    # Move cursor down one page
    def page_down():
        actions.key("pagedown")

    # ----- Selection -----
    # Clear current selection
    def select_none():
        actions.key("right")

    # Extend selection up one row
    def extend_up():
        actions.key("shift-up")

    # Extend selection down one row
    def extend_down():
        actions.key("shift-down")

    # Extend selection left one column
    def extend_left():
        actions.key("shift-left")

    # Extend selection right one column
    def extend_right():
        actions.key("shift-right")

    # Insert a copy of the current selection
    def selection_clone():
        text = actions.edit.selected_text()
        actions.edit.select_none()
        actions.insert(text)

    # ----- Save -----
    # Save all active modes
    def save():
        actions.key("ctrl-s")

    # ----- Delete, Undo, Redo -----
    # Delete selection
    def delete():
        actions.key("backspace")

    # Undo
    def undo():
        actions.key("ctrl-z")

    # Redo
    def redo():
        actions.key("ctrl-y")

    # ----- Cut, Copy, Paste -----
    # Cut selection to clipboard
    def cut():
        actions.key("ctrl-x")

    # Copy selection to clipboard
    def copy():
        actions.key("ctrl-c")

    # Paste clipboard at cursor_
    def paste():
        # Sleeps are necessary when chaining commands before and after sleep
        actions.sleep("25ms")
        actions.key("ctrl-v")
        actions.sleep("25ms")

    # Paste clipboard without style information
    def paste_match_style():
        actions.key("ctrl-shift-v")

    # ----- Indent -----
    # Remove a tab stop of indentation
    def indent_less():
        actions.key("home delete")

    # Add a tab stop of indentation
    def indent_more():
        actions.key("home tab")

    # ----- Find -----
    # Open Find dialog, optionally searching for text
    def find(text: str = None):
        actions.key("ctrl-f")
        if text:
            actions.insert(text)

    # Select previous Find result
    def find_previous():
        actions.key("shift-f3")

    # Select next Find result
    def find_next():
        actions.key("f3")

    # ----- Zoom -----
    # Zoom in
    def zoom_in():
        actions.key("ctrl-+")

    # Zoom out
    def zoom_out():
        actions.key("ctrl--")

    # Zoom to original size
    def zoom_reset():
        actions.key("ctrl-0")

    # ----- Miscellaneous -----
    # Get currently selected text
    def selected_text() -> str:
        with clip.capture(0.1) as c:
            actions.edit.copy()
        try:
            return c.text()
        except clip.NoChange:
            return ""


# we define new actions that are "edition" related
@mod.action_class
class Actions:
    def insert_with_padding(text: str):
        """Insert text with padding"""
        if text[0].isspace() or text[-1].isspace():
            before, after = actions.user.dictation_get_context()

            # At start of line or has leading whitespace
            if before is not None and (len(before) == 0 or before[-1].isspace()):
                text = text.lstrip()

            # Has trailing whitespace
            # Disabled for now because it's too annoying
            # if after is not None and len(after) != 0 and after[0].isspace():
            #     text = text.rstrip()

        actions.insert(text)

    def delete_right():
        """Delete character to the right"""
        actions.key("delete")

    def insert_arrow():
        """Insert arrow symbol"""
        actions.insert(" => ")

    def insert_symbol_and_break_at_end(symbol: str):
        """Add symbol at end of line and then insert line below"""
        actions.edit.line_end()
        actions.key(symbol)
        actions.edit.line_insert_down()

    def paste_text(text: str):
        """Pastes text and preserves clipboard"""
        with clip.revert():
            clip.set_text(text)

            if clip.text() != text:
                actions.user.notify("Failed to set clipboard")
                return

            actions.edit.paste()

            # Sleep here so that clip.revert doesn't revert the clipboard too soon
            actions.sleep("200ms")

    def insert_clipboard_with_keys():
        """Insert clipboard content by key presses"""
        text = actions.clip.text()
        for c in text:
            actions.key(c)

    def edit_text_file(path: str):
        """Edit text file <path>"""
        actions.user.exec(f"code {path}")

    # ----- Cut, copy, paste -----
    def edit_cut():
        """Cut selection to clipboard"""
        actions.edit.cut()

    def edit_copy():
        """Copy selection to clipboard"""
        actions.edit.copy()

    def edit_paste(expand: bool):
        """Paste clipboard at cursor"""
        actions.edit.paste()
