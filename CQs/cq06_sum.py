"""Summing the elements of a list using different loops"""

__author__ = "730649404"


def w_sum(vals: list[float]) -> float:
    """Adds all values of list with while loop"""
    index: int = 0
    # keeps track of index being added
    total: float = 0.0
    # each value will add to this variable
    while index < len(vals):
        total = total + vals[index]
        # adds the value of each index to total variable
        index = index + 1
    return total


def f_sum(vals: list[float]) -> float:
    """Adds all values of list with for... in... loop"""
    total: float = 0.0
    # each value will add to this variable
    for number in vals:
        total = total + number
        # adds each element in list to total variable
    return total


def f_range_sum(vals: list[float]) -> float:
    """Adds all values of list with for... in range()... loop"""
    total: float = 0.0
    # each value will add to this variable
    for idx in range(0, len(vals)):
        total = total + vals[idx]
        # adds the value of each index to total variable from the range 0 to list length
    return total
