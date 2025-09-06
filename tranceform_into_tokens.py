from symbols import *

def is_any_element_of_a_list_is_in_str(List,str):
    for i in List:
        if i in str:
            return True
    return False
def tonken_converter(text:str):
    tokens = []
    token = ""
    for i in text:
        token += i
        if token in key_words:
            tokens.append((Tokens.KEY_WORDS,token))
            token = ""
        if i in key_symbols:
            tokens.append((Tokens.KEY_SYMBOLS,i))
            if not token in key_symbols:
                token = token[0:len(token)-1]
                tokens.append((Tokens.TEXT,token))
            token = ""
        if token in Basic_types:
            tokens.append((Tokens.KEY_TYPES,token))
            token = ""

    return tokens
a = tonken_converter("def var test | int = 1 life_time = 1 |")