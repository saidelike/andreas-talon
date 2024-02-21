settings():
    user.clipboard_manager_max_rows = 20

clippy:                     user.clipboard_manager_toggle()

(pace | paste) <number_small> [and <number_small>]*:
    user.clipboard_manager_paste(number_small_list)
(pace | paste) <user.ordinals_small> [and <user.ordinals_small>]*:
    user.clipboard_manager_paste(ordinals_small_list)

(pace | paste) special <number_small> [and <number_small>]*:
    user.clipboard_manager_paste(number_small_list, 1)
(pace | paste) special <user.ordinals_small> [and <user.ordinals_small>]*:
    user.clipboard_manager_paste(ordinals_small_list, 1)
