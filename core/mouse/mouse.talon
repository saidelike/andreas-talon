# Click
click {user.mouse_click}:   user.mouse_click(mouse_click)
drag:                       mouse_drag()
touch:                      user.mouse_click("left")
duke:                       user.mouse_click("double")
righty:                     user.mouse_click("right")
# midd:                       user.mouse_click("middle")
# mimic the "stash" command from rango to open a link in a non focused new tab
# then we can use the repeater parrot sound in order to opened several links
stash:                      user.mouse_click("control")

# Scroll
# TODO: should the scrolling commands be moved to scroll.talon?
climb:                      user.mouse_scrolling("up")
drop:                       user.mouse_scrolling("down")
climb <number_small>:       user.mouse_scroll("up", number_small)
drop <number_small>:        user.mouse_scroll("down", number_small)
mouse gaze:                 user.mouse_gaze_scroll()

scroll speed show:          user.mouse_scroll_speed_notify()
scroll speed <number_small>: user.mouse_scroll_speed_set(number_small)
scroll speed up:            user.mouse_scroll_speed_increase()
scroll speed down:          user.mouse_scroll_speed_decrease()

# Eye tracking
track on:                   user.mouse_control_toggle(true)
track off:                  user.mouse_control_toggle(false)
track:                      user.mouse_control_toggle()
track gaze:                 tracking.control_gaze_toggle(true)
track head:                 tracking.control_gaze_toggle(false)
track debug:                tracking.control_debug_toggle()
track calibrate:            tracking.calibrate()

# Cursor
cursor center:              user.mouse_move_center_window()
cursor print:               print("{mouse_x()}, {mouse_y()}")
cursor copy:                clip.set_text("{mouse_x()}, {mouse_y()}")
# ^cursor show$:              user.mouse_show_cursor()
# ^cursor hide$:              user.mouse_hide_cursor()
