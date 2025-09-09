from symbols import *
from types_glasser import *
from treelib import tree

def creatparsetree(tokens : any):
    parsetree = tree()
    instructions = []
    consumingtoken = tokens
    while not consumingtoken == []:
        token = consumingtoken[0]
        type_of_token = token[0]
        if type_of_token == Tokens.KEY_WORDS:
            if token[1] == "if":
                instructions.append(type_of_instructions.CONDITIONALS)
                instructions.append(conditionals.IF)
            elif token[1] == "else":
                instructions.append(type_of_instructions.CONDITIONALS)
                instructions.append(conditionals.ELSE)
            elif token[1] == "while":
                instructions.append(type_of_instructions.CONDITIONALS)
                instructions.append(conditionals.WHILE)
            elif token[1] == "def":
                instructions.append(type_of_instructions.DECLARATION)
            elif token[1] == "func":
                instructions.append(type_of_instructions.FUNC)
            elif token[1] == "type":
                instructions.append(type_of_instructions.TYPE)
            elif token[1] == "macro":
                instructions.append(type_of_instructions.MACRO)
            elif token[1] == "general":
                instructions.append(type_of_instructions.GENERAL)
        elif type_of_token == Tokens.KEY_SYMBOLS:
            if token[1] ==