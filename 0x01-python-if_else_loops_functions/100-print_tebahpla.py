#!/usr/bin/python3
for i in range(90, 64, -1):
    print(chr(i) + chr(i + 32) if i % 2 == 0 else chr(i), end='')
