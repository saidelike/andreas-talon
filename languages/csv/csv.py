from talon import Context, actions


ctx = Context()
# we need to specify the apps so we can override the toggle_comment() implementation
ctx.matches = r"""
app: notepadpp
app: vscode
code.language: csv
"""


# TODO: this could be generalized to talon-list/talon files in notepad++ as well
@ctx.action_class("code")
class CodeActions:
    # this is not a great implementation because it moves the cursor,
    # but it's better than nothing
    def toggle_comment():
        comment_character = "#"
        actions.edit.select_line()
        selected = actions.edit.selected_text()
        actions.edit.line_start()
        if selected.startswith(comment_character + " "):
            actions.user.delete_right()
            actions.user.delete_right()
        elif selected.startswith(comment_character):
            actions.user.delete_right()
        elif selected.startswith(" "):
            actions.insert(comment_character)
        else:
            actions.insert(comment_character + " ")
