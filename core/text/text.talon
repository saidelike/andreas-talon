# Formatted prose phrase: "sentence hello there" -> Hello there
{user.formatter_prose} <user.prose>$:
    user.insert_formatted(prose, formatter_prose)
{user.formatter_prose} <user.prose> {user.phrase_ender}:
    user.insert_formatted(prose, formatter_prose)
    "{phrase_ender}"

# Formatted code phrase: "camel hello there" -> helloThere
{user.formatter_code} <user.text_code>:
    user.insert_formatted(text_code, formatter_code)
{user.formatter_code} <user.text_code> {user.phrase_ender}:
    user.insert_formatted(text_code, formatter_code)
    "{phrase_ender}"

# Only words, no symbols or numbers
escape <user.phrase>$:      "{phrase}"
escape <user.phrase> over:  "{phrase}"

# Single word: "word up" => up, "proud up" => Up
{user.formatter_word} <user.word>:
    user.insert_formatted(word, formatter_word)
# Single abbreviated word. "proud brief app" => App
{user.formatter_word} <user.abbreviation>:
    user.insert_formatted(abbreviation, formatter_word)
# Abbreviated word without formatter: "brief application" => app, "brief app" => app
<user.abbreviation>:        "{abbreviation}"

# Upper case characters
ship <user.letters> [over]:
    user.insert_formatted(letters, "ALL_UPPERCASE")
