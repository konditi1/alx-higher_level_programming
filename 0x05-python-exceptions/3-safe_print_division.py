#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        result = a/b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
