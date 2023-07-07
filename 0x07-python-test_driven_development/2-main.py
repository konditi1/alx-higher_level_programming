#!/usr/bin/python3
""" Doc """

matrix_divided = __import__('2-matrix_divided').matrix_divided

try:
    matrix = [[3, 9], [12, 15]]
    print(matrix_divided(matrix, 0))
except Exception as e:
    print(e)
