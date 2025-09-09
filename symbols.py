from enum import Enum, auto

key_symbols = [
    "/",
    " ",
    "+",
    "-",
    "*",
    "=",
    "{",
    "}",
    "(",
    ")",
    ">",
    "<",
    "=",
    "\\",
    "|",
    "\n",
    "\t",
    ";",
    ","
]
key_words = [
    "def",
    "macro",
    "func",
    "type",
    "var",
    "if",
    "else",
    "swich",
    "case",
    "add", #this is to add a general to a type
    "general",
    "import"
]

class Tokens(Enum):
    KEY_WORDS = auto()
    KEY_SYMBOLS = auto()
    TEXT = auto()
