from talon import Context, Module, actions

mod = Module()
ctx = Context()

# Declare a new global "user.extensions" tag
mod.tag("extensions", desc="Enable extension commands")


# Declare a capture "<user.extension>" (due to "extension" function definition below)
@mod.capture(rule="dot ({user.code_extension} | {user.file_extension})")
def extension(m) -> str:
    return f".{m[-1]}"


# Declare a capture "<user.filename>" (due to "filename" function definition below)
@mod.capture(rule="[{user.formatter_code}] <user.text> [<user.extension>]")
def filename(m) -> str:
    try:
        text = actions.user.format_text(m.text, m.formatter_code)
    except AttributeError:
        text = m.text
    try:
        extension = m.extension
    except AttributeError:
        extension = ""
    return f"{text}{extension}"


# fmt: off

# Declare a new global "user.file_extension" list
mod.list("file_extension", "List of (non-code) file extensions")
# Initialize the "user.file_extension" list
ctx.lists["user.file_extension"] = {
    "exe":            "exe",
    "bin":            "bin",
}

extension_siblings = {
    "talon":        "py",
    "py":           "talon",
    "c":            "h",
    "cpp":          "h",
    "h":            "c",
    "tsx":          "ts",
    "jsx":          "js",
    "ts":           "tsx",
    "js":           "jsx",
}

# fmt: on


# we define new actions that are "extensions" related
@mod.action_class
class UserActions:
    def get_extension_sibling(extension: str) -> str:
        """Get matching sibling for extension"""
        if extension in extension_siblings:
            return extension_siblings[extension]
        return None
