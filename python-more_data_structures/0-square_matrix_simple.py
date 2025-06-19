#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        row_values = []
        for val in row:
            row_values.append(val**2)
        new_matrix.append(row_values)
    print(new_matrix)
