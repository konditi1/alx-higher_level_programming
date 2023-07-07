#!/usr/bin/python3
""""
module which contains the function def text_indentation(text):
"""


def text_indentation(text):
    """
    text_indentation prints a text with 2 new lines after
    each of these characters . , ? and :
    parameter
    text: str
        the text to be printed
    return: None
    """
    try:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        if len(text) == 0:
            raise ValueError("text cannot be empty")
        punctuation = [".", "?", ":"]
        for char in punctuation:
            if char + " " in text:
                text = text.replace(char + " ", char + "\n\n").strip()
            else:
                text = text.replace(char, char + "\n\n").strip()
        print(text, end="")
    except (TypeError, ValueError) as e:
        print(e)
