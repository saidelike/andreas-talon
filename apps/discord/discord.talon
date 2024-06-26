# this file is only active when the "user"-defined "discord" app is enabled
app: discord
-
# in Discord, we want to be able to toggle mute and navigate forward/backward
tag(): user.voip
tag(): user.navigation

deafen:                     key(ctrl-shift-d)

server last:                key(ctrl-alt-up)
server next:                key(ctrl-alt-down)

channel last:               key(alt-up)
channel next:               key(alt-down)

edit last:                  key(up)
focus text:                 key(tab)
go oldest unread:           key(shift-pageup)
go audio channel:           key(alt-left)
go text channel:            key(alt-right)
go call:                    key(ctrl-shift-alt-v)
