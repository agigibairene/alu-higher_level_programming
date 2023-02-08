#!/usr/bin/python3
for x in range(-ord('z'), -ord('a') -1):
    if (x % 2) !=0:
        x = x -(ord('A') - ord('a'))
    print("{}".format(chr(-x) ), end="")
