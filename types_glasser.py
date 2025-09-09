from enum import Enum, auto
class err:
    def __init__(self,id):
        self.id = id

class Type:
    def __init__(self,name):
        self.name = name
        self.methods = {}
    def add_method(self,method_name):
        self.methods[method_name] = None
    def set_method(self,code,method):
        self.methods[method] = code

class var:
    def __init__(self,name : str,lifetime : int | None,type : Type):
        self.name = name
        self.type = type
        self.lifetime = lifetime
    def use_var(self) -> None | err :
        if self.lifetime == None:
            return None
        if self.lifetime > 0:
            self.lifetime -= 1
            return None
        return err(1)

class func:
    def __init__(self,name):
        self.name = name
        self.code = None
    def set_code(self,code):
        self.code = code

class conditionals(Enum):
    IF = auto()
    ELSE = auto()
    WHILE = auto()

class comparations(Enum):
    GREATER = auto()
    LESSER = auto()
    EQUAL = auto()
    GREATER_EQUAL = auto()
    LESSER_EQUAL = auto()


class type_of_instructions(Enum):
    CONDITIONALS = auto()
    COMPARATIONS = auto()
    FUNC = auto()
    TYPE = auto()
    VAR = auto()
    MACRO = auto()
    GENERAL = auto()
    DECLARATION = auto()

class oporations(Enum):
    ADDITION = auto()
    SUBTRACTION = auto()
    MULTIPLICATION = auto()
    DIVITION = auto()
    NOT = auto()
    AND = auto()
    OR = auto()
    SET = auto()
    