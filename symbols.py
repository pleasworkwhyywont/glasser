from enum import Enum, auto
Basic_types = [
    "int8"
    "uint8"
]

key_symbols = [
    "/"
    "+"
    "-"
    "*"
    "{"
    "}"
    "("
    ")"
    ">"
    "<"
    "="
    "\\"
    "|"
    "\n"
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
    "add", #this is to add a method to a type
    "general",
    "import"
]

class tokens(Enum):
    KEY_WORDS = auto()
    KEY_SYMBOLS = auto()
    KEY_TYPES = auto()