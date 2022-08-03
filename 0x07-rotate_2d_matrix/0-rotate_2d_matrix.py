#!/usr/bin/python3
"""Module for rotate_2d_matrix function"""


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    lengz = len(matrix)
    for i in range(lengz):
        for j in range(i, lengz):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp
    for row in matrix:
        row.reverse()
