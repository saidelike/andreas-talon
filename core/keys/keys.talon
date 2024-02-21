# Letters [A-Z]
{user.letter}:              key(letter)

# Symbol keys: !, %, _
{user.symbol}:              key(symbol)

# Digits [0-9]
# NOTE: commenting so "list one two three" outputs "one, two, three"
# and "list number one number two number three" outputs "1, 2, 3"
# and it also matches disabling "<user.number_dd>" in text_and_dictation.py
# {user.digit}:               key(digit)

# Special keys.
enter | okay:               key(enter)
tab:                        key(tab)
# speed up navigating in reverse order between fields
shab:                       key(shift-tab)

# Special symbols
new line [symbol]:          "\\n"
tab symbol:                 "\\t"

# Add symbol at end of line and then insert line below
spike {user.symbol}:        user.insert_symbol_and_break_at_end(symbol)

# Modifier(s) + key: "control air" or "control win left"
<user.key_modifiers> <user.key_unmodified>:
    key("{key_modifiers}-{key_unmodified}")

# Single key. Including Modifiers, [a-z], [0-9], [F1-F12], arrow, symbols
press <user.key_any>:       key(key_any)
