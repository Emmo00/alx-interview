#!/usr/bin/python3
"""
minimum operations
"""
from typing import Tuple


def factors(n: int) -> Tuple[int, int]:
    """get min and max factors of a number"""
    if n == 1:
        return 1, 1
    if n == 0:
        return 0, 0
    for i in range(2, int(n / 2) + 1):
        if n / i == n // i:
            return i, int(n / i)
    return 1, n


def minOperations(n: int) -> int:
    """
    calculate the minimum operations
    """
    if n == 1:
        return 0
    if n <= 0:
        return 0
    min_factors, max_factors = factors(n)
    if min_factors == 1:
        return max_factors
    if min_factors == 0:
        return 0
    return min_factors + minOperations(max_factors)
