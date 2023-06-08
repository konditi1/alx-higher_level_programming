#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    def num_of_args(*argv):

        print("{} argument{}{}".format(
            len(argv),
            "s" if len(argv) != 1 else "",
            "." if len(argv) == 0 else ":"
        ))
        for index, arg in enumerate(argv):
            print("{}: {}".format(index + 1, arg))

    num_of_args(*sys.argv[1:])
