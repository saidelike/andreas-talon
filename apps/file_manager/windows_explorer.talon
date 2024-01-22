# this file is only active when the "user"-defined "windows_explorer" or "windows_file_browser" app is enabled
app: windows_explorer
app: windows_file_browser
-
# we want to be able to navigate folders, create files/folders, browse tabs
tag(): user.file_manager
tag(): user.tabs

go up:                      user.select_up()
go down:                    user.select_down()
select:                     user.select_toggle()
file rename:                key(f2)

open home:
    app.tab_open()
    user.file_manager_go_home()
open <user.path_any>:
    app.tab_open()
    user.file_manager_go(path_any)

file copy name:
    key(f2)
    edit.copy()
    key(enter)

scout [<user.text>]$:
    edit.find(text or "")
pop <user.text>$:
    edit.find(text)
    sleep(100ms)
    key(enter)
