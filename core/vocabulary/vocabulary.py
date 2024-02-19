from talon import Context, Module, app, actions
from typing import Sequence
from pathlib import Path
from .phrase_replacer import PhraseReplacer

mod = Module()

mod.list("vocabulary", "Additional vocabulary words")

ctx_en = Context()

phrase_replacer_en = None


@ctx_en.action_class("dictate")
class DictateActionsEn:
    def replace_words(words: Sequence[str]) -> Sequence[str]:
        return phrase_replacer_en.replace(words)


# we define new actions that are "vocabulary" related
@mod.action_class
class Actions:
    def edit_words_to_replace():
        """Edit words to replace csv"""
        andreas_settings = actions.user.andreas_settings()
        file = Path(andreas_settings) / "words_to_replace_en.csv"
        actions.user.edit_text_file(file.absolute())

    def edit_vocabulary():
        """Edit vocabulary Talon list"""
        andreas_settings = actions.user.andreas_settings()
        file = Path(andreas_settings) / "vocabulary_en.talon-list"
        actions.user.edit_text_file(file.absolute())


# Words to replace is used by `actions.dictate.replace_words` to rewrite words
# Talon recognized. Entries don't change the priority with which Talon
# recognizes some words over others.
def words_to_replace_en_update(csv_dict: dict):
    global phrase_replacer_en
    phrase_replacer_en = PhraseReplacer(csv_dict)


def on_ready():
    andreas_settings = Path(actions.user.andreas_settings())
    actions.user.watch_csv_as_dict(
        andreas_settings / "words_to_replace_en.csv",
        words_to_replace_en_update,
    )


app.register("ready", on_ready)
