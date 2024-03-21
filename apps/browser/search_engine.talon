# TODO: change all of these with "scout google ..."
search for <user.text>$:
    user.browser_search(text)

search for (this | dis | is | ness):
    user.browser_search_selected()
search for line:
    edit.select_line()
    user.browser_search_selected()
search for token:
    edit.select_word()
    user.browser_search_selected()

scout dictionary word <user.word>$:
    user.browser_define(word)
scout dictionary phrase <user.text>$:
    user.browser_define(text)
scout dictionary (this | dis):
    user.set_selection_on_word_if_none()
    user.browser_define_selected()
