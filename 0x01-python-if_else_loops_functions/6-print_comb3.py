#!/usr/bin/python3
# print(", ".join("{}{}".format(i, j) for i in range(10) for j in range(1, 10)
# if i < j))
for i in range(10):
    for j in range(i + 1, 10):
        print("{:d}{:d}".format(i, j), end="")
        if i != 8 or j != 9:
            print(", ", end="")
print()
