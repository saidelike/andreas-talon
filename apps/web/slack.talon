# this file is only active when the "user"-defined "slack" app is enabled
app: slack
-

# see profile > preferences > accessibility > handy keyboard shortcuts
keyboard shortcuts:         key(ctrl-/)

# TODO: ??
sidebar (show | hide):      key(ctrl-shift-d)
panel (show | hide):        key(ctrl-.)

go unreads:                 key(ctrl-shift-a)
go threads:                 user.slack_open_search_result("Threads")
# DMs
go [direct] messages:       key(ctrl-shift-k)
# Activity
go (mentions | reactions):  key(ctrl-shift-m)
go drafts:                  user.slack_open_search_result("Drafts")

scout channel [<user.text>]:
    # Jump to a conversation
    key(ctrl-k)
    "{text or ''}"
pop channel <user.text>:
    user.slack_open_search_result(text)

please [<user.text>]$:
    # Jump to a conversation
    key(ctrl-k)
    sleep(100ms)
    edit.delete()
    sleep(100ms)
    "{text or ''}"

# Previous channel or DM
channel last:               key(alt-up)
# Next channel or DM
channel next:               key(alt-down)
# Previous unread channel or DM
channel unread last:        key(alt-shift-up)
# Next unread channel or DM
channel unread next:        key(alt-shift-down)
next unread:                key(alt-shift-down)

# Edit last message (in empty text input)
edit last:                  key(ctrl-up)
# Edit (your own message)
edit:                       key(e)

# Format text as code
format code:                key(ctrl-shift-c)
# Format selection as code block
format [code] block:        key(ctrl-alt-shift-c)
# Format selection as quote
format quote:               key(ctrl-shift-9)
