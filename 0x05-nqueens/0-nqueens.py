#!/usr/bin/python3
"""
n queens implementation
"""
from sys import argv, exit


def main() -> None:
    """entry point"""
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    N = argv[1]
    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)
    col = set()
    pos_diagonal = set()  # r + c
    neg_diagonal = set()  # r - c
    queens = list()
    res = []

    def backtrack(r):
        if r == N:
            copy = [list(row) for row in queens]
            res.append(copy)
            return

        for c in range(N):
            if c in col or (r + c) in pos_diagonal or (r - c) in neg_diagonal:
                continue

            col.add(c)
            pos_diagonal.add(r + c)
            neg_diagonal.add(r - c)
            queens.append([r, c])

            backtrack(r + 1)

            col.remove(c)
            pos_diagonal.remove(r + c)
            neg_diagonal.remove(r - c)
            queens.pop()
    backtrack(0)
    for possible in res:
        print(possible)


if __name__ == '__main__':
    main()
