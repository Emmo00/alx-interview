#!/usr/bin/python3
"""
validate utf8
"""


def validUTF8(data):
    bytes_to_check = 0
    for byte in data:
        if bytes_to_check == 0:
            if (byte & 0x80) == 0:
                bytes_to_check = 0
            elif (byte & 0xE0) == 0xC0:
                bytes_to_check = 1
            elif (byte & 0xF0) == 0xE0:
                bytes_to_check = 2
            elif (byte & 0xF8) == 0xF0:
                bytes_to_check = 3
            else:
                return False
        else:
            if (byte & 0xC0) != 0x80:
                return False
            bytes_to_check -= 1
    return bytes_to_check == 0
