#!/usr/bin/python3
"""module
"""


def isPrime(number):
    """is prime
    """
    if number == 1:
        return False
    limit = number // 2
    for i in range(2, limit):
        if number % i == 0:
            return False
    return True


def lowest_prime_number(numbers):
    """lowest prime number
    """
    sorted_numbers = sorted(numbers)
    for i in sorted_numbers:
        if isPrime(i):
            return i
    return None


def toggle_turn(current_player):
    """toggle turn
    """
    return 'Ben' if current_player == 'Maria' else 'Maria'


def winner(players: dict):
    """winner
    """
    keys = list(players.keys())
    values = list(players.values())
    if values[0] == values[1]:
        return None
    max_player = max(values)
    winner_index = values.index(max_player)
    return keys[winner_index]


def isWinner(x, nums):
    """prime game
    """
    if x <= 0 or not nums:
        return None
    if x < len(nums):
        return None
    players = {
        'Maria': 0,
        'Ben': 0,
    }
    for round in range(x):
        turn = 'Maria'
        if nums[round] < 1:
            continue
        numbers = list(range(1, nums[round] + 1))
        try:
            while numbers:
                choice = lowest_prime_number(numbers)
                if choice is None:
                    raise Exception()
                # remove multiples
                numbers = [num for num in numbers if num % choice != 0]
                turn = toggle_turn(turn)
        except Exception:
            # other person wins round
            turn = toggle_turn(turn)
            players[turn] += 1
            continue
    return winner(players)
