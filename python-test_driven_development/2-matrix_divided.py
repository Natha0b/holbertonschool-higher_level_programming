#!/usr/bin/python3
"""function that divides all elements of a matrix."""


def matrix_divided(matrix, div):

    """that divides all elements of a matrix"""

    if not all(list(map(lambda x: all(list(map(lambda num:
               isinstance(num, (int, float)), x))), matrix))):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(val/div, 2) for val in row] for row in matrix]
