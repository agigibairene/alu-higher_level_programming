#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for x in matrix:
            for y in x:
                if y == x[0]:
                    print("{:d}".format(y), end="")
                else:
                    print("{:d}".format(y), end="")
            print()
    else:
        print()
