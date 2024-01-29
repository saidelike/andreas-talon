# this file is only active when the Talon-defined "windows_terminal" tag is enabled
app: windows_terminal
-
# we want to be able to browse tabs, find text, and this is a terminal after all
tag(): user.tabs
tag(): user.find
tag(): terminal

split cross:                key(alt-shift-d)
split right:                key(alt-shift-+)
split down:                 key(alt-shift--)

cross$:                     key(ctrl-alt-left)
cross up:                   key(alt-up)
cross down:                 key(alt-down)
cross left:                 key(alt-left)
cross right:                key(alt-right)

resize up:                  key(alt-shift-up)
resize down:                key(alt-shift-down)
resize left:                key(alt-shift-left)
resize right:               key(alt-shift-right)

please:                     key(ctrl-shift-p)
please <user.text>$:
    key(ctrl-shift-p)
    "{text}"
