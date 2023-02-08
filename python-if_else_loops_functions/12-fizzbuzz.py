#!/usr/bin/python3
def fizzbuzz():
    for fizzbuzz in range(1, 101):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("Fizzbuzz", end="")
        if (i % 3) == 0:
            print("Fizz", end='')
        if (i % 5) == 0:
            print("Buzz", end='')
        if (i % 3) != 0 and (i % 5) != 0:
            print("{}".format(i), end='')
        print(" ", end='')
