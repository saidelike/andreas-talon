# eg "three times" in "air three times"
<user.repeater_phrase_sub_one>: core.repeat_command(repeater_phrase_sub_one)
repeat <user.repeater_phrase>: core.repeat_command(repeater_phrase)

# TODO: what is this for?
phrase <user.repeater_phrase_sub_one>: core.repeat_partial_phrase(repeater_phrase_sub_one)
repeat phrase <user.repeater_phrase>: core.repeat_partial_phrase(repeater_phrase)
