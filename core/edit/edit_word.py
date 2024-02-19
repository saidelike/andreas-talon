from talon import Context, Module, actions

mod = Module()
ctx = Context()


# these are Talon-defined "edit" actions (only grouped for clarity) that we override
@ctx.action_class("edit")
class EditActions:
    # Move cursor left one word
    def word_left():
        actions.key("ctrl-left")

    # Move cursor right one word
    def word_right():
        actions.key("ctrl-right")

    # Select word under cursor
    def select_word():
        actions.edit.right()
        actions.edit.word_left()
        actions.edit.extend_word_right()
        text = actions.edit.selected_text()
        text_trim = text.rstrip()
        for _ in range(len(text) - len(text_trim)):
            actions.edit.extend_left()

    # Extend selection left one word
    def extend_word_left():
        actions.key("ctrl-shift-left")

    # Extend selection right one word
    def extend_word_right():
        actions.key("ctrl-shift-right")

    # Delete word under cursor
    def delete_word():
        actions.edit.select_word()
        actions.edit.delete()


# we define new actions that are "word edition" related
@mod.action_class
class Actions:
    def select_word_left():
        """Select word to the left"""
        actions.edit.word_left()
        actions.edit.extend_word_right()

    def select_word_right():
        """Select word to the right"""
        actions.edit.word_right()
        actions.edit.extend_word_left()

    def cut_word():
        """Cut word under cursor"""
        actions.edit.select_word()
        actions.edit.cut()

    def copy_word():
        """Copy word under cursor"""
        actions.edit.select_word()
        actions.edit.copy()

    def paste_word():
        """Paste to word under cursor"""
        actions.edit.select_word()
        actions.edit.paste()

    def delete_word_left():
        """Delete word to the left"""
        actions.user.select_word_left()
        actions.sleep("50ms")
        actions.edit.delete()

    def delete_word_right():
        """Delete word to the right"""
        actions.user.select_word_right()
        actions.sleep("50ms")
        actions.edit.delete()

    # XXX this could be improved to delete the word on the left or right
    # depending if the cursor is close to a special character and a word is on the other side
    def delete_selection_or_word():
        """Delete selection or word under cursor (simulates 'chuck this')"""
        text = actions.edit.selected_text()
        if len(text) > 0:
            actions.edit.delete()
        else:
            actions.user.delete_word_right()

    def copy_selection_or_word():
        """Copy selection or word under cursor (simulates 'copy this')"""
        text = actions.edit.selected_text()
        if len(text) > 0:
            actions.edit.copy()
        else:
            actions.user.copy_word()

    def cut_selection_or_word():
        """Cut selection or word under cursor (simulates 'cut this')"""
        text = actions.edit.selected_text()
        if len(text) > 0:
            actions.edit.cut()
        else:
            actions.user.cut_word()

    def paste_to_selection_or_word():
        """Paste from clipboard to selection or word under cursor (simulates 'paste to this')"""
        text = actions.edit.selected_text()
        if len(text) > 0:
            actions.edit.paste()
        else:
            actions.user.paste_word()

    def set_selection_on_word_if_none():
        """Set selection on word under cursor if nothing is selected"""
        text = actions.edit.selected_text()
        if len(text) == 0:
            actions.edit.select_word()
