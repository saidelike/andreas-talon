from talon import Context, Module, actions

mod = Module()
ctx = Context()


# these are Talon-defined "edit" actions (only grouped for clarity) that we override
@ctx.action_class("edit")
class EditActions:
    # Move cursor to start of file
    def file_start():
        actions.key("ctrl-home")

    # Move cursor to end of file (start of line)
    def file_end():
        actions.key("ctrl-end home")

    # Select all text in the current document
    def select_all():
        actions.key("ctrl-a")

    # Extend selection to start of file
    def extend_file_start():
        actions.key("shift-ctrl-home")

    # Extend selection to end of file
    def extend_file_end():
        actions.key("shift-ctrl-end")


# we define new actions that are "file edition" related
@mod.action_class
class Actions:
    def cut_all():
        """Cut all text in the current document"""
        actions.edit.select_all()
        actions.edit.cut()

    def copy_all():
        """Copy all text in the current document"""
        actions.edit.select_all()
        actions.edit.copy()
        actions.edit.select_none()

    def paste_all():
        """Paste to the current document"""
        actions.edit.select_all()
        actions.edit.paste()

    def delete_all():
        """Delete all text in the current document"""
        actions.edit.select_all()
        actions.edit.delete()

    # TODO: this should probably be moved to a non-edit file
    def file_post():
        """Simulate the 'post file' cursorless command"""
        actions.key("ctrl-end")
