#!/usr/bin/python3
"""
module which multiplys two matrixs
"""


def matrix_mul(m_a, m_b):
    """
    param m_a: list of lists of integers
    param m_b: list of lists of integers
    return: list of lists of integers
    """
    try:
        if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
            raise TypeError("m_a must be a lists")
        if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
            raise TypeError("m_b must be a lists")
        if not all(isinstance(row, list) for row in m_a):
            raise TypeError("m_a must be a lists of lists")
        if not all(isinstance(row, list) for row in m_b):
            raise TypeError("m_b must be a lists of lists")
        if len(m_a) == 0 or len(m_a[0]) == 0:
            raise ValueError("m_a cannot be empty")
        if len(m_b) == 0 or len(m_b[0]) == 0:
            raise ValueError("m_b cannot be empty")
        if not all(isinstance(num, (int, float)) for row in m_a for num in row):
            raise ValueError("m_a should contain only integers or floats")
        if not all(isinstance(num, (int, float)) for row in m_b for num in row):
            raise ValueError("m_b should contain only integers or floats")
        if not all(len(row) == len(m_a[0]) for row in m_a):
            raise TypeError("Each row of m_a must be of the same size")
        if not all(len(row) == len(m_b[0]) for row in m_b):
            raise TypeError("Each row of m_b must be of the same size")
        if len(m_a[0]) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")
        return [[sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
                 for j in range(len(m_b[0]))]
                for i in range(len(m_a))]
    except (TypeError, ValueError) as e:
        return e
