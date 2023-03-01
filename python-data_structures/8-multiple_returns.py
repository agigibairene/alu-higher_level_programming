#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first_character = None
    else:
        first_character = sentence[0]
    Tuple = (len(sentence),first_charcacter)
    return Tuple
