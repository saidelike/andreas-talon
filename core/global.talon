then:                       skip()
stop:                       user.stop_app()

pick <number_small>:        user.pick_item(number_small)
pick to:                    user.pick_item(2)
# pick <user.word>:
pick text <user.word>:
    "{word}"
    key(enter)
# pick <user.letters>:
pick letter <user.letters>:
    "{letters}"
    key(enter)
