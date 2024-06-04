tag: user.splits
-

# Arrangement
split up:                   user.split_move_up()
split down:                 user.split_move_down()
split left:                 user.split_move_left()
split right:                user.split_move_right()

# Navigation
cross up:                   user.split_focus_up()
cross down:                 user.split_focus_down()
cross left:                 user.split_focus_left()
cross right:                user.split_focus_right()
cross next:                 user.split_focus_next()
cross last:                 user.split_focus_last()
cross <number_small>:       user.split_focus(number_small)

# Resizing
shrink width:               user.split_shrink_width()
shrink height:              user.split_shrink_height()
expand width:               user.split_expand_width()
expand height:              user.split_expand_height()

split flip:                 user.split_layout_toggle()
split clear:                user.split_layout_join_two_groups()
split solo:                 user.split_layout_clear()
split max:                  user.split_layout_toggle_maximize()
