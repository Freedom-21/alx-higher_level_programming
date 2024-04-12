#!/usr/bin/python3

"""
Module for matrix operations. Currently includes a function to divide all elements of a matrix by a number.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and rounds to 2 decimal places.

    Args:
    matrix (list of lists of int/float): The matrix to be divided.
    div (int/float): The divisor.

    Returns:
    list of lists of float: New matrix with all elements divided.

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats, if rows are of different sizes,
               or if div is not a number.
    ZeroDivisionError: If div is zero.
    """
    if matrix is None or not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(not isinstance(row, list) or not row for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
