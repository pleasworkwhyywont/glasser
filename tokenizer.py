from symbols import *

def tonken_converter(text:str):
    tokens = []
    token = ""
    for i in text:
        if i in key_symbols:
            if not token in key_words and not token == "":
                tokens.append((Tokens.TEXT,token))
                token = ""
            tokens.append((Tokens.KEY_SYMBOLS,i))
        else:
            token += i
        TOKEN = None
        if token in key_words:
            TOKEN = (Tokens.KEY_WORDS,token)
        
        if not TOKEN == None:
            token = ""
            tokens.append(TOKEN)

    return tokens
