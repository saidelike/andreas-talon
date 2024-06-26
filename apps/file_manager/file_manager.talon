# this file is only active when the user-defined "user.file_manager" tag is enabled
tag: user.file_manager
-
# we want to be able to navigate forward/backward
tag(): user.navigation
tag(): user.extensions

# ----- Navigation -----
go parent:                  user.file_manager_go_parent()
go home:                    user.file_manager_go_home()
go <user.path_any>:         user.file_manager_go(path_any)
# go path <user.path_any>:    user.file_manager_go(path_any)
go address:                 user.file_manager_focus_address()
copy address:               user.file_manager_copy_address()

# ----- Create folders / files -----
file new:                   user.file_manager_new_file("")
folder new:                 user.file_manager_new_folder("")
file new <user.text>$:      user.file_manager_new_file(text)
folder new <user.text>$:    user.file_manager_new_folder(text)

# ----- Miscellaneous -----
properties show:            user.file_manager_show_properties()
terminal here:              user.file_manager_terminal_here()
