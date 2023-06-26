#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        if value is None:
            raise TypeError
        print("{:d}".format(value))
    except (ValueError, TypeError, NameError) as err:
        error_message = "Exception: {}".format(err)
        sys.stderr.write(error_message + '\n')
        return False
    else:
        return True
