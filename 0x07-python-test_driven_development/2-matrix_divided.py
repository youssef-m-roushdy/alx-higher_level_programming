#!/usr/bin/python3
""""Modulr for divides each element of the matrix by the given divisor."""


def matrix_divided(matrix, div):
    """
    Divides each element of the matrix by the given divisor.

    Args:
        matrix (list[list[int or float]]): The matrix to
        be divided. Must be a matrix
            (list of lists) of integers or floats.
        div (int or float): The divisor used for division.

    Returns:
        list[list[float]]: A new matrix with each element
        rounded to 2 decimal places
            after division.

    Raises:
        TypeError: If the matrix is not a matrix of integers/floats
        or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("Matrix must be a matrix (list of lists)"
                            " of integers/floats.")
        row_size = len(matrix[0]) if matrix else 0
        if not all(len(row) == row_size for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")

        if type(div) not in [int, float]:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")

        new_matrix = [
            [round(element / div, 2) for element in row]
            for row in matrix]
        return new_matrix
