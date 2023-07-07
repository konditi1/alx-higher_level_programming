#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    :param m_a: list of lists of integers
    :param m_b: list of lists of integers
    :return: NumPy array
    """
    try:
        np_a = np.array(m_a)
        np_b = np.array(m_b)
        result = np.matmul(np_a, np_b)
        return result.tolist()
    except ValueError as e:
        return str(e)
