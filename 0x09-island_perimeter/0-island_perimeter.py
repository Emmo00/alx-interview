#!/usr/bin/python3
"""module
"""


def island_perimeter(grid):
    """island perimeter
    """
    perimeter = 0
    if grid is None or len(grid) == 0 or len(grid[0]) == 0:
        return 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if grid[i][j - 1] == 0:
                    perimeter += 1
                if i == 0 or grid[i-1][j] != 1:
                    perimeter += 1
                if grid[i + 1][j] == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
