from symbols import *
from treelib import tree

def creatparsetree(tokens : any):
    parsetree = tree()
    instructions = []
    while not tokens == []:
        token = tokens[0]
        type_of_token = token[0]
        if type_of_token == Tokens.KEY_WORDS:
            instructions.append(Tokens.KEY_WORDS)
            if token[1] == "if":
                instructions.append