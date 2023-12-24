#!/usr/bin/python3
"""making change
"""
from typing import List


def makeChange(coins: List, total: int):
    """making change
    """
    if total <= 0:
        return 0
    count = 0
    while total > 0:
        biggest = total + 1
        while biggest > total:
            if len(coins) == 0:
                return -1
            biggest = max(coins)
            if biggest > total:
                coins.remove(biggest)
        total = total - biggest
        count += 1
    if total == 0:
        return count
    return -1
