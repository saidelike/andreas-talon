from talon import Context, Module, actions

ctx = Context()
mod = Module()


# these are Talon-defined "edit" actions (only grouped for clarity) that we override
@ctx.action_class("edit")
class EditActions:
    # Move cursor to the start of the current paragraph
    def paragraph_start():
        if extend_paragraph_start():
            actions.edit.left()

    # Move cursor to the end of the current paragraph
    def paragraph_end():
        if extend_paragraph_end():
            actions.edit.right()

    # Select the entire nearest paragraph
    def select_paragraph():
        if is_line_empty():
            return
        # Search for start of paragraph
        actions.edit.extend_paragraph_start()
        actions.edit.left()
        # Extend to end of paragraph
        actions.edit.extend_paragraph_end()

    # Extend selection to the start of the current paragraph
    def extend_paragraph_start():
        extend_paragraph_start()

    # Extend selection to the end of the current paragraph
    def extend_paragraph_end():
        extend_paragraph_end()

    # Delete paragraph under cursor
    def delete_paragraph():
        actions.edit.select_paragraph()
        actions.edit.delete()
        actions.edit.delete()
        actions.edit.delete_line()


# we define new actions that are "paragraph edition" related
@mod.action_class
class Actions:
    def cut_paragraph():
        """Cut paragraph under the cursor"""
        actions.edit.select_paragraph()
        actions.edit.cut()

    def copy_paragraph():
        """Copy paragraph under the cursor"""
        actions.edit.select_paragraph()
        actions.edit.copy()
        actions.edit.select_none()

    def paste_paragraph():
        """Paste to paragraph under the cursor"""
        actions.edit.select_paragraph()
        actions.edit.paste()


def is_line_empty():
    actions.edit.extend_line_start()
    text = actions.edit.selected_text().strip()
    if text:
        actions.edit.right()
        return False
    actions.edit.extend_line_end()
    text = actions.edit.selected_text().strip()
    if text:
        actions.edit.left()
        return False
    return True


def extend_paragraph_start() -> bool:
    actions.edit.extend_line_start()
    text = actions.edit.selected_text()
    length = len(text)
    while True:
        actions.edit.extend_up()
        actions.edit.extend_line_start()
        text = actions.edit.selected_text()
        new_length = len(text)
        if new_length == length:
            break
        line = text[: new_length - length].strip()
        if not line:
            actions.edit.extend_down()
            break
        length = new_length
    return text.strip() != ""


def extend_paragraph_end() -> bool:
    actions.edit.extend_line_end()
    text = actions.edit.selected_text()
    length = len(text)
    while True:
        actions.edit.extend_down()
        actions.edit.extend_line_end()
        text = actions.edit.selected_text()
        new_length = len(text)
        if new_length == length:
            break
        line = text[length:].strip()
        if not line:
            actions.edit.extend_line_start()
            actions.edit.extend_left()
            break
        length = new_length
    return text.strip() != ""
