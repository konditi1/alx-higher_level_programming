#!/usr/bin/python3
def square_matrix_simple(matrix=None):
    if matrix is None:
        matrix = []
    changed_matrix = [row[:] for row in matrix]
    for row in range(len(changed_matrix)):
        changed_matrix[row] = list(map(lambda item: item ** 2,
                                   changed_matrix[row]))
    return changed_matrix
