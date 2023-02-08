#!/usr/bin/python3
i = 0
for a in range(ord('z'), ord('a')-1, -1):
    print("{}".format(chr(a-i) if i == 32 else i = 32 ), end="")
