#!/usr/bin/python3
for x in range(ord('a'), ord('b') + 1):
    if chr(x) != 'q' and chr(x) != 'e':
        print("{}".format(chr(x)), end="")
