#!/usr/bin/python3
"""
Generate Pascal's triangle up to the given number of rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists representing the Pascal's triangle.

    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle
