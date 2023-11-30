#!/usr/bin/python3
"""module
"""


def island_perimeter(grid):
    perimeter = 0
    for i in range(len(grid)):
        start = True
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if start:
                    start = False
                    perimeter += 2
                if grid[i-1][j] != 1:
                    perimeter += 2
    return perimeter