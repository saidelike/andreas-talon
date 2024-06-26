from talon import Context, Module, actions

ctx = Context()
mod = Module()


# these are Talon-defined "edit" actions (only grouped for clarity) that we override
@ctx.action_class("edit")
class EditActions:
    # Move cursor to start of line
    def line_start():
        actions.key("home")

    # Move cursor to end of line
    def line_end():
        actions.key("end")

    # Select entire line <n>, or current line
    def select_line(n: int = None):
        if n:
            actions.edit.jump_line(n)
        actions.key("end shift-home")

    # Select entire lines from <a> to <b>
    def select_lines(a: int, b: int):
        number_of_lines = abs(a - b)
        if number_of_lines < 1 or number_of_lines > 500:
            return
        actions.edit.jump_line(a)
        if a < b:
            for _ in range(number_of_lines):
                actions.edit.extend_line_down()
            actions.edit.extend_line_end()
        else:
            actions.edit.line_end()
            for _ in range(number_of_lines):
                actions.edit.extend_line_up()
            actions.edit.extend_line_start()

    # Extend selection up one full line
    def extend_line_up():
        actions.key("shift-up")

    # Extend selection down one full line
    def extend_line_down():
        actions.key("shift-down")

    # Extend selection to start of line
    def extend_line_start():
        actions.key("shift-home")

    # Extend selection to end of line
    def extend_line_end():
        actions.key("shift-end")

    # Insert line above cursor
    def line_insert_up():
        actions.key("home enter up")

    # Insert line below cursor
    def line_insert_down():
        actions.key("end enter")

    # Create a new line identical to the current line
    def line_clone():
        actions.user.copy_line()
        actions.edit.line_insert_down()
        actions.edit.paste()

    # Swap the current line with the line above
    def line_swap_up():
        actions.user.cut_line()
        actions.edit.line_start()
        actions.edit.paste()
        actions.key("enter up")

    # Swap the current line with the line below
    def line_swap_down():
        actions.user.cut_line()
        actions.key("down end enter")
        actions.edit.paste()

    # Delete line under cursor
    def delete_line():
        actions.user.clear_line()
        actions.key("home delete")


# we define new actions that are "line edition" related
@mod.action_class
class Actions:
    def line_middle():
        """Move cursor to middle of line"""
        actions.edit.select_line()
        text = actions.edit.selected_text().strip()
        actions.edit.right()
        for _ in range(round(len(text) / 2)):
            actions.edit.left()

    def cut_line():
        """Cut current line"""
        actions.edit.select_line()
        actions.edit.cut()

    def copy_line():
        """Copy current line"""
        actions.edit.select_line()
        actions.edit.copy()
        actions.edit.select_none()

    def paste_line():
        """Paste to current line"""
        actions.edit.select_line()
        actions.edit.paste()

    def line_insert_down_twice():
        """Insert two lines below cursor"""
        actions.edit.line_insert_down()
        actions.edit.line_insert_down()

    def clear_line():
        """Clear current line"""
        actions.key("end shift-home space backspace")

    # ----- Start / End -----
    def select_line_start():
        """Select start of current line"""
        if actions.edit.selected_text():
            actions.edit.left()
        actions.edit.extend_line_start()

    def select_line_end():
        """Select end of current line"""
        if actions.edit.selected_text():
            actions.edit.right()
        actions.edit.extend_line_end()

    def cut_line_start():
        """Cut start of current line"""
        actions.user.select_line_start()
        actions.edit.cut()

    def cut_line_end():
        """Cut end of current line"""
        actions.user.select_line_end()
        actions.edit.cut()

    def copy_line_start():
        """Copy start of current line"""
        actions.user.select_line_start()
        actions.edit.copy()
        actions.edit.right()

    def copy_line_end():
        """Copy end of current line"""
        actions.user.select_line_end()
        actions.edit.copy()
        actions.edit.left()

    def paste_line_start():
        """Paste to start of current line"""
        actions.user.select_line_start()
        actions.edit.paste()

    def paste_line_end():
        """Paste to end of current line"""
        actions.user.select_line_end()
        actions.edit.paste()

    def delete_line_start():
        """Delete start of current line"""
        actions.user.select_line_start()
        actions.edit.delete()

    def delete_line_end():
        """Delete end of current line"""
        actions.user.select_line_end()
        actions.edit.delete()
