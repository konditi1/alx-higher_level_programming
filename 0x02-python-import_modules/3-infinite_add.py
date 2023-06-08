#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    def value_of_argv(*argv):
        sum_of_argv = 0
        for arg in argv:
            sum_of_argv += int(arg)
        print(sum_of_argv)

    value_of_argv(*sys.argv[1:])
