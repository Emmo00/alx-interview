#!/usr/bin/python3
"""
validate utf8
"""


def validUTF8(data):
    try:
        for i in range(len(data)):
            if data[i] >= 192:
                if data[i + 1] >= 192:
                    return False
                if data[i] > 224:
                    if data[i + 2] >= 192:
                        return False
    except IndexError:
        return False
    return True
