#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in range(len(matrix)):
        for line2 in range(len(matrix[line])):
            print("{:d}".format(matrix[line][line2]), end="")
            if line2 < len(matrix[line]) - 1:
                print(" ", end="")
        print('')
