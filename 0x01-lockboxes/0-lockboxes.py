#!/usr/bin/python3
"""lockboxes problem module"""


def extract_keys(box_keys, boxes):
    """extract keys from boxes"""
    found = list(box_keys)
    for key in found:
        if key >= len(boxes):
            continue
        for i in boxes[key]:
            if i not in found:
                found.append(i)
    return found


def canUnlockAll(boxes):
    """checks if a list of boxes can all be unlocked"""
    keys = []
    locked_boxes = [i for i in range(1, len(boxes))]
    keys.extend(extract_keys(boxes[0], boxes))
    keys = set(keys)
    for box in locked_boxes:
        if box not in keys:
            return False
    return True
