#!/usr/bin/python3
"""Module for add_integer method."""


def matrix_divided(matrix, div):
    """Divide matrix."""
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("Matrix must be a matrix (list of lists) of integers/floats.")
        row_size = len(matrix[0]) if matrix else 0
        if not all(len(row) == row_size for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")

        if type(div) not in [int, float]:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")

        new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
        return new_matrix
    
    


