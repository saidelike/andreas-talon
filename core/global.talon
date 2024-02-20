then:                       skip()
stop:                       user.stop_app()

# NOTE: "pick" gives to much false positive with "pit" so we instead use the word "choose"
choose <number_small>:      user.pick_item(number_small)
choose to:                  user.pick_item(2)
# choose text <user.word>:
choose <user.word>:
    "{word}"
    sleep(100ms)
    key(enter)
# choose letter <user.letters>:
choose <user.letters>:
    "{letters}"
    sleep(100ms)
    key(enter)
