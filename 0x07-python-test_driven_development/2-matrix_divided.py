#!/usr/bin/python3
"""
represent a module which divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
        matrix divided by div
        :parameter
        matrix: list of lists of integers
        div: integer
        :return: list of lists of integers
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    msg1 = "Each row of the matrix must have the same size"
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError(msg)
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise ValueError("matrix cannot be empty")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_one_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_one_len:
            raise TypeError(msg1)
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError(msg)
    updated_matrix = []
    for item in matrix:
        updated_row = [(round(element / div, 2)) for element in item]
        updated_matrix.append(updated_row)
    return updated_matrix
