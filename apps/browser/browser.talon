# this file is only active when the Talon-defined "browser" tag is enabled
tag: browser
-
# in a browser, we want to be able to zoom, browse tabs, find text, and navigate forward/backward
# tag(): user.zoom
tag(): user.tabs
tag(): user.find_and_replace
tag(): user.navigation

dot {user.domain}:          ".{domain}"

go address:                 browser.focus_address()
go home:                    browser.go_home()
go {user.webpage}:          browser.go(webpage)
open {user.webpage}:        user.browser_open_new_tab(webpage)

go private:                 browser.open_private_window()

bookmark show:              browser.bookmarks()
bookmark bar:               browser.bookmarks_bar()
bookmark it:                browser.bookmark()
bookmark tabs:              browser.bookmark_tabs()

(refresh | reload) page:    browser.reload()
(refresh | reload) page hard: browser.reload_hard()

show downloads:             browser.show_downloads()
show extensions:            browser.show_extensions()
show history:               browser.show_history()
show cache:                 browser.show_clear_cache()

dev tools:                  browser.toggle_dev_tools()

# this allows hiding the actual tabs at the very top
fullscreen switch:          key(f11)
