#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return None
    First_character = sentence[0]
    Total_length = 0
    for length in sentence:
        Total_length += 1
