# this file is only active when the "user"-defined "user.find" tag is enabled
tag: user.find
-

# search in current file
scout paste:                edit.find(clip.text())
# scout text [<user.text>] [then]: edit.find(text or "")
scout text [<user.text>]$:  edit.find(text or "")
# scout$:                     edit.find("")

scout last:                 edit.find_previous()
scout next:                 edit.find_next()

# search everywhere
scout (eve|if) paste:       user.find_everywhere(clip.text())
# scout (eve|if) text [<user.text>] [then]: user.find_everywhere(text or "")
scout (eve|if) text [<user.text>]$: user.find_everywhere(text or "")
# scout (eve|if)$:            user.find_everywhere("")

scout (eve|if) last:        user.find_everywhere_previous()
scout (eve|if) next:        user.find_everywhere_next()

# replace
replace paste:              user.find_replace(clip.text())
replace text [<user.text>]$: user.find_replace(text or "")
# replace$:                   user.find_replace("")

replace eve paste:          user.find_replace_everywhere(clip.text())
replace (eve|if) [<user.text>]$: user.find_replace_everywhere(text or "")

# search options
scout case:                 user.find_toggle_match_by_case()
scout word:                 user.find_toggle_match_by_word()
scout expression:           user.find_toggle_match_by_regex()
replace case:               user.find_replace_toggle_preserve_case()

scout hide:
    edit.find("")
    sleep(100ms)
    key(escape)

replace confirm:            user.find_replace_confirm()
replace confirm all:        user.find_replace_confirm_all()

scout file paste:           user.find_file(clip.text())
scout (file|files|filed) [<user.filename>]$:
    user.find_file(filename or "")

# TODO:
# pop <user.text>$:
#     edit.find(text)
#     key(enter)

pop (file|files|filed) <user.filename>$:
    user.find_file(filename)
    sleep(300ms)
    key(enter)
