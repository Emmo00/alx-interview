#!/usr/bin/python3
"""module.
"""


def rotate_2d_matrix(matrix):
    """rotate 2d matrix
    """
    rows = len(matrix)
    rotated = set()
    for i in range(rows):
        for j in range(rows):
            if not((i, j) in rotated or (j, i) in rotated):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                rotated.add((i, j))
                rotated.add((j, i))
    for i in range(rows):
        matrix[i].reverse()
