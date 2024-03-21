from talon import Module, Context, actions
from ..tags.code_operators import CodeOperators

mod = Module()
ctx = Context()

ctx.matches = r"""
code.language: lua
"""

# fmt: off
ctx.lists["user.code_operator"] = CodeOperators(
    op_assign        = " = ",
    op_sub           = " - ",
    op_add           = " + ",
    op_mult          = " * ",
    op_div           = " / ",
    op_mod           = " % ",
    # TODO: is exponential the same?
    # op_pow           = " ^ ",
    is_equal         = " == ",
    is_not_equal     = " ~= ",
    is_less          = " < ",
    is_greater       = " > ",
    is_less_equal    = " <= ",
    is_greater_equal = " >= ",
    is_not           = "not ",
    is_null          = " == nil",
    is_not_null      = " ~= nil",
    op_and           = " and ",
    op_or            = " or ",
)
access_modifiers = {
    "local"
}
ctx.lists["user.code_class_modifier"] = {}
ctx.lists["user.code_function_modifier"] = {
    *access_modifiers
}
ctx.lists["user.code_variable_modifier"] = {
    *access_modifiers,
}
ctx.lists["user.code_data_type"] = {
}
ctx.lists["user.code_call_function"] = {
    "error": "error",
    "to number": "tonumber",
    "I pairs": "ipairs",
    "print": "print",
    "print F": "printf",
    "type": "type",
    "assert": "assert",
    "get meta table": "getmetatable",
    "set meta table": "setmetatable",
    "collect garbage": "collectgarbage",
    # io
    "I O write": "io.write",
    "I O read": "io.read",
    "I O open": "io.open",
    # table
    "table unpack": "table.unpack",
    "table insert": "table.insert",
    "tabel get N": "table.getn",
    "tabel sort": "table.sort",
    # math
    "math max": "math.max",
    # json
    "jason parse": "json.parse",
    # http
    "H T T P get": "http.get",
    "web get": "http.get",
    # os
    "O S date": "os.date",
    "O S time": "os.time",
    "O S clock": "os.clock",
    "O S rename": "os.rename",
    "O S remove": "os.remove",
    "O S getenv": "os.getenv",
    "O S execute": "os.execute",
    # struct
    "unpack": "struct.unpack",
    # string
    "format": "string.format",
    "string G find": "string.gfind",
    "string find": "string.strfind",
    "string len": "string.strlen",
    "string upper": "string.strupper",
    "string lower": "string.strlower",
    "string sub": "string.strsub",
    "string G sub": "string.gsub",
    "string match": "string.match",
    "string G match": "string.gmatch",
}
ctx.lists["user.code_insert"] = {
    "true"      : "true",
    "false"     : "false",
    "nil"      : "nil",
    "return"    : "return ",
    "require"    : "require ",
    "local"    : "local ",
    "break"     : "break",
    "end": "end",
}
# fmt: on


@ctx.action_class("user")
class UserActions:
    # Class statement
    # TODO: https://www.lua.org/pil/16.1.html
    # def code_class(name: str, modifiers: list[str]):
    #     actions.user.insert_snippet_by_name("classDeclaration", {"name": name})

    # Constructor statement
    # TODO: https://www.lua.org/pil/16.1.html
    # def code_constructor(modifiers: list[str]):
    #     actions.user.insert_snippet_by_name("constructorDeclaration")

    # Function statement
    def code_function(name: str, modifiers: list[str]):
        actions.user.insert_snippet_by_name(
            "functionDeclaration",
            {"name": f"{''.join(modifiers)}{name}"},
        )

    # Variable statement
    def code_variable(
        name: str, modifiers: list[str], assign: bool, data_type: str = None
    ):
        text = name
        if modifiers:
            text = f"{' '.join(modifiers)} {text}"
        if assign:
            text += " = "
        actions.insert(text)

    # Formatting getters
    # TODO: https://www.lua.org/pil/16.1.html
    # def code_get_class_format() -> str:
    #     return "PASCAL_CASE"

    def code_get_function_format() -> str:
        return "SNAKE_CASE"

    def code_get_variable_format() -> str:
        return "SNAKE_CASE"
