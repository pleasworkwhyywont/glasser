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
    "general"
]

class err:
    def __init__(self,name,tip):
        self.name = name
        self.tip = tip

class Type:
    def __init__(self,name):
        self.name = name
        self.methods = {}
    def add_method(self,method_name):
        self.methods[method_name] = null
    def set_method(self,code,method):
        self.methods[method] = code

class var:
    def __init__(self,name : str,lifetime : int,type : Type):
        self.name = name
        self.type = type
        self.lifetime = lifetime
    def use_var(self) -> null | :
        if self.lifetime
        self.lifetime -= 1
