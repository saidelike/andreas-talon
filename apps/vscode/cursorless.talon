# this file is only active when the "user"-defined "vscode" app is enabled
app: vscode
-
# enable the "user.cursorless_custom_number_small" tag, which is defined in cursorless-talon
tag(): user.cursorless_custom_number_small

# Cursorless command without targets
^cursorless use release$:
    user.c_use_release()
^cursorless use develop$:
    user.c_use_develop()
^cursorless record$:
    user.vscode("cursorless.recordTestCase")
^cursorless record highlight$:
    argument = user.as_dict("isDecorationsTest", 1)
    user.vscode("cursorless.recordTestCase", argument)
^cursorless record error$:
    argument = user.as_dict("recordErrors", 1)
    user.vscode("cursorless.recordTestCase", argument)
^cursorless record pause$:
    user.vscode("cursorless.pauseRecording")
^cursorless record resume$:
    user.vscode("cursorless.resumeRecording")

# Git
git open <user.cursorless_target>:
    user.cursorless_command("setSelection", cursorless_target)
    user.git_open_remote_file_url(true, false)
git copy <user.cursorless_target>:
    user.cursorless_command("setSelection", cursorless_target)
    user.git_copy_remote_file_url(true, false)
git copy mark [down] <user.cursorless_target>:
    user.git_copy_markdown_remote_file_url(cursorless_target_list)
git copy mark [down] <user.cursorless_target> [as <user.cursorless_target>]:
    user.git_copy_markdown_remote_file_url(cursorless_target_list)

# Actions around take word
take <user.cursorless_target> <user.repeater_phrase_all>:
    user.vscode_take_word(cursorless_target, repeater_phrase_all)
pre <user.cursorless_target> <user.repeater_phrase_all>:
    user.vscode_take_word(cursorless_target, repeater_phrase_all)
    edit.left()
post <user.cursorless_target> <user.repeater_phrase_all>:
    user.vscode_take_word(cursorless_target, repeater_phrase_all)
    edit.right()
cut <user.cursorless_target> <user.repeater_phrase_all>:
    user.vscode_take_word(cursorless_target, repeater_phrase_all)
    edit.cut()
copy <user.cursorless_target> <user.repeater_phrase_all>:
    user.vscode_take_word(cursorless_target, repeater_phrase_all)
    edit.copy()
paste to <user.cursorless_target> <user.repeater_phrase_all>:
    user.vscode_take_word(cursorless_target, repeater_phrase_all)
    edit.paste()
# clear <user.cursorless_target> <user.repeater_phrase_all>:
change <user.cursorless_target> <user.repeater_phrase_all>:
    user.vscode_take_word(cursorless_target, repeater_phrase_all)
    edit.delete()

# Text insertion
# eg "place stack to end of next line" will append a ":" to the end of the following line
place ({user.symbol} | <user.text>) <user.cursorless_destination>:
    user.cursorless_insert(cursorless_destination, symbol or text)

# eg "snip if to row 10" will insert the if statement snippet at row 10
# see core\snippets\snippets\ifStatement.snippet
snip {user.snippet} <user.cursorless_destination>:
    user.c_insert_snippet(cursorless_destination, snippet)

# eg "dash wrap this" wraps the target with "-"
{user.symbol} wrap <user.cursorless_target>:
    user.c_wrap_with_symbol(cursorless_target, symbol)

# eg "if wrap this" in .py file
# see core\snippets\snippets\ifStatement.snippet
{user.snippet_wrapper} wrap <user.cursorless_target>:
    user.c_wrap_with_snippet(cursorless_target, snippet_wrapper)

# Misc
search for <user.cursorless_target>:
    user.c_browser_open_target(cursorless_target)
