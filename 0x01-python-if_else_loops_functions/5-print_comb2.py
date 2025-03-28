#!/usr/bin/python3

for i in range(0, 100):
    if i < 99:
        if i < 10:
            i = f"0{i}"
        print(i, end=", ")
print(99) 
    