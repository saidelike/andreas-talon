# this file is only active when on Windows and the "user"-defined "user.file_manager" tag is enabled
# i.e. in Windows explorer or the terminal
os: windows
and tag: user.file_manager
-

go {user.letter} colon:     user.file_manager_go("{letter}:")

file delete:                key(delete)
file open:                  key(enter)
# eg useful to edit an image in ms paint
# https://superuser.com/questions/810352/is-there-a-keyboard-shortcut-to-edit-files-such-as-reg-bat-and-so-on
file edit:
    key(shift-f10)
    key(e)
