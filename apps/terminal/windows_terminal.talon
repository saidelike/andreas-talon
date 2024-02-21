# this file is only active when the Talon-defined "windows_terminal" tag is enabled
app: windows_terminal
-
# this is a terminal after all and we want to be able to browse tabs, find text
tag(): terminal
tag(): user.tabs
tag(): user.find

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
