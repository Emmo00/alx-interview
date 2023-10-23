#!/usr/bin/python3
"""
validate utf8
"""


def validateUTF8(data):
    for i in range(len(data)):
        if data[i] > 192:
            if data[i + 1] > 128 or (data[i + 1] > 192:
                    return false
            if data[i] > 224:

