# I am using the mapping F16 to F19 as I was already using F13 for other stuff

# Left button
key(f16:down):              user.foot_switch_down_event(0)
key(f16:up):                user.foot_switch_up_event(0)

# Center button
key(f17:down):              user.foot_switch_down_event(1)
key(f17:up):                user.foot_switch_up_event(1)

# Right button
key(f18:down):              user.foot_switch_down_event(2)
key(f18:up):                user.foot_switch_up_event(2)

# Top button
key(f19:down):              user.foot_switch_down_event(3)
key(f19:up):                user.foot_switch_up_event(3)

# Misc
scroll reverse:             user.foot_switch_scroll_reverse()
