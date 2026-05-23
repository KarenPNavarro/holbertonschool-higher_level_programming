#!/usr/bin/python3
"""Module that defines the matrix_divided function.

This module provides a function that divides all elements of a
matrix by a given number, rounded to 2 decimal places. The
original matrix is not modified; a new one is returned.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Validates input types and structure, then returns a new matrix
    where each element is divided by div and rounded to 2 decimals.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)
    row_len = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_msg)
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(error_msg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)
    return new_matrix
