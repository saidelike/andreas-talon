code.language: markdown
-
# tag(): user.code_generic_language

snip link [<user.text>]:    user.code_markdown_link(text or "")

# Formatter wrappers
{user.markdown_pair} this:
    user.set_selection_on_word_if_none()
    user.delimiters_pair_wrap_selection_with(markdown_pair, markdown_pair)
{user.markdown_pair} token:
    edit.select_word()
    user.delimiters_pair_wrap_selection_with(markdown_pair, markdown_pair)
{user.markdown_pair} line:
    edit.select_line()
    user.delimiters_pair_wrap_selection_with(markdown_pair, markdown_pair)

# Titles levels
level one:
    edit.line_start()
    "# "
level two:
    edit.line_start()
    "## "
level three:
    edit.line_start()
    "### "
level four:
    edit.line_start()
    "#### "
