#!/usr/bin/python3
""" returns a list of lists of integers representing
     the Pascals triangle of n"""


def pascal_triangle(n):
    """ returns a list of lists of integers """
    triangle = []
    if n <= 0:
        return triangle

    triangle = [[1 for i in range(row)] for row in range(1, n + 1)]

    for x in range(2, n):
        for i in range(1, x):
            triangle[x][i] = triangle[x - 1][i] + triangle[x - 1][i - 1]
    return triangle
