"""Practicing with list Utility Functions."""

__author__ = "730649404"


def all(integer_list: list[int], integer: int) -> bool:
    """Checks if all values in list match integer"""
    index: int = 0
    if len(integer_list) == 0:
        # if list is empty
        return False
    while index < len(integer_list):
        if integer_list[index] != integer:
            # if integer does not match index of list
            return False
        else:
            index = index + 1
    return True


def max(integer_list: list[int]) -> int:
    """Returns max value of list"""
    index: int = 0
    if len(integer_list) == 0:
        # if list is empty
        raise ValueError("max() arg is an empty List")
        # raises error (Value Error)
    max_val: int = integer_list[index]
    # highes value in list(updated)
    while index < len(integer_list):
        if integer_list[index] >= max_val:
            max_val = integer_list[index]
            # updates variable to higher value
            index = index + 1
        else:
            index = index + 1
    return max_val


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Checks if every index of two lists are equal"""
    if list_one == list_two:
        # if lists are exactly the same (length and values)
        return True
    else:
        return False


def extend(list_one: list[int], list_two: list[int]) -> None:
    """Extends list by combining two seperate lists"""
    index: int = 0
    while index < len(list_two):
        list_one.append(list_two[index])
        # adds value of indexed list to first list
        index = index + 1
