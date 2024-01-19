# TODO: change all of these with "scout google ..."
search for <user.text>$:
    user.browser_search(text)

search for (this | dis | is | ness):
    user.browser_search_selected()
search for line:
    edit.select_line()
    user.browser_search_selected()
search for (word | token):
    edit.select_word()
    user.browser_search_selected()

# TODO: change all of these with "scout dictionary ..."
define word <user.word>$:
    user.browser_search("https://www.merriam-webster.com/dictionary/{word}")
define phrase <user.text>$:
    user.browser_search("https://www.merriam-webster.com/dictionary/{text}")
