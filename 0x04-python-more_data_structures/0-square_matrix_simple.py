#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_mat = []
    for row in matrix:
        sqr_row = []
        for element in row:
            sqr_row.append(element ** 2)
        sqr_mat.append(sqr_row)
    return sqr_mat
