from talon import Module

mod = Module()


# Declare a capture "<user.repeater_phrase>" (due to "repeater_phrase" function definition below)
@mod.capture(rule="twice | trice | <number_small> times")
def repeater_phrase(m) -> int:
    """Repeater string. Returns an integer for number of times to repeat"""
    if m[0] == "twice":
        return 2
    if m[0] == "trice":
        return 3
    return m.number_small


# Declare a capture "<user.repeater_phrase_sub_one>" (due to "repeater_phrase_sub_one" function definition below)
@mod.capture(rule="<user.repeater_phrase>")
def repeater_phrase_sub_one(m) -> int:
    """Repeater string. Returns an integer for number of times to repeat. Subtracts one"""
    return m.repeater_phrase - 1


# Declare a capture "<user.repeater_phrase_all>" (due to "repeater_phrase_all" function definition below)
@mod.capture(rule="<user.repeater_phrase> | breed")
def repeater_phrase_all(m) -> int:
    """Repeater string. Returns an integer for number of times to repeat, including all"""
    try:
        return m.repeater_phrase
    except AttributeError:
        return -1
