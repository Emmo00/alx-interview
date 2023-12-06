#!/usr/bin/python3
"""module
"""


def isPrime(number):
    limit = number // 2
    for i in range(limit):
        if number / i == number // i:
            return False
    return True


def lowest_prime_number(numbers):
    sorted_numbers = sorted(numbers)
    for i in sorted_numbers:
        if isPrime(i):
            return i
    raise Exception('No Prime number found')


def toggle_turn(current_player):
    return 'Ben' if current_player == 'Maria' else 'Maria'


def winner(players: dict):
    keys = list(players.keys())
    values = list(players.values())
    max_player = max(values)
    winner_index = values.index(max_player)
    return keys[winner_index]


def isWinner(x, nums):
    """prime game
    """
    players = {
        'Maria': 0,
        'Ben': 0,
    }
    for round in range(x):
        turn = 'Maria'
        numbers = list(range(1, round + 1))
        try:
            choice = lowest_prime_number(numbers)
            # remove multiples
            j = 1
            while j < max(numbers):
                if choice * j in numbers:
                    numbers.remove(choice * j)
                j += 1
            turn = toggle_turn(turn)
        except Exception:
            # other person wins round
            turn = toggle_turn(turn)
            players[turn] += 1
            continue
    return winner(players)
