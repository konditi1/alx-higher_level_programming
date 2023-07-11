#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
    function that writes a text file (UTF8)
    parameter
        filename: str
            the name of the file to be created
        text: str
            the text to be written
    returns:
        the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
