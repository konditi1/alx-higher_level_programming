#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        first_letter = None
    else:
        first_letter = sentence[0]
    my_tuple = (len(sentence), first_letter)
    return my_tuple
