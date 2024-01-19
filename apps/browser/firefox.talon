# this file is only active when the "user"-defined "firefox" app is enabled
app: firefox
-
# enable the "browser" tag to inherit all its features:
# zoom, browse tabs, find text, and navigate forward/backward.
# we also want to scroll and use Rango
tag(): browser
tag(): user.scroll
tag(): user.rango_direct_clicking

# Tabs
# TODO: change this to "scout tab"? need to make a new action in the browser
tab search:
    browser.focus_address()
    "% "
tab search <user.text>$:
    browser.focus_address()
    "% {text}"
    key(down)
tab mute:                   key(ctrl-m)

# Rango
{user.rango_with_target_action} <user.rango_target>:
    user.rango_command_with_target(rango_with_target_action, rango_target)
{user.rango_without_target_action}:
    user.rango_command_without_target(rango_without_target_action)

# TODO: support latest Rango to allow switching back and forth from explicit/direct
rango explicit:
    user.rango_disable_direct_clicking()
rango direct:
    user.rango_enable_direct_clicking()

copy page address:
    user.rango_command_without_target("copyLocationProperty", "href")

# Miscellaneous
copy image:
    mouse_click(1)
    sleep(100ms)
    key(y)
copy image source:
    mouse_click(1)
    sleep(100ms)
    key(o:2 enter)
copy video:
    mouse_click(1)
    sleep(100ms)
    key(o:2 enter)
