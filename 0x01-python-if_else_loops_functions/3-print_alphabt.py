#!/usr/bin/python3
for char in range(97, 123):
    if char == ord('e') or char == ord('q'):
        continue
    print("{}".format(chr(char)), end='')
