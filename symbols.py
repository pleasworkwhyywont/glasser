import enum
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

class tokens(enum):
    KEY_WORD = 1
    KEY_SYMBOL = 2
    KEY_TYPE = 3