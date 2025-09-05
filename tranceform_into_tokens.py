from symbols import *
def tonken_converter(text:str):
    tokens = []
    token = ""
    for i in text:
        token += i
        if token in key_words:
            tokens.append((tokens.KEY_WORDS))
        if token in key_symbols:
            tokens.append((tokens.KEY_SYMBOLS))
        if token in Basic_types:
            tokens.append((tokens.KEY_TYPES))
