#!/usr/bin/python3
def uppercase(str):
    for c in str:
        new_c = chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c
        print("{}".format(new_c), end="")
    print()
