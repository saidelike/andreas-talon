# this file is only active when the "user"-defined "keepass" app is enabled
app: keepass
-
# Database
# We can use generic commands for opening/closing it

# Entries
pour this:                  key(ctrl-y)
change this:                key(enter)
clone this:                 key(ctrl-k)
chuck this:                 key(ctrl-d)

# Credentials
copy user [name]:
    key(ctrl-b)
    sleep(200ms)
    user.window_focus_last()
copy pass [word]:
    key(ctrl-c)
    sleep(200ms)
    user.window_focus_last()
follow (this | earl | url | link): key(ctrl-u)

# Search
scout:                      key(ctrl-f)
scout <user.text>:
    key(ctrl-f)
    insert("{text}")
    key(enter)
