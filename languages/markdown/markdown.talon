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
section one:
    edit.line_start()
    "# "
section two:
    edit.line_start()
    "## "
section three:
    edit.line_start()
    "### "
section four:
    edit.line_start()
    "#### "
