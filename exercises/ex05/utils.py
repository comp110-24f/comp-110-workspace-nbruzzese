"""ex 05 (Practice modifying/returning lists)"""

__author__ = "730649404"


def only_evens(input_list1: list[int]) -> list[int]:
    """Returns list of even values of input list"""
    index: int = 0
    even_list: list[int] = []
    # starting with empty list
    while index < len(input_list1):
        if input_list1[index] % 2 == 0:
            # even numbers
            even_list.append(input_list1[index])
            # adds even numbers to new list
            index = index + 1
        else:
            # odd numbers
            index = index + 1
    return even_list
    # new list


def sub(input_list2: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns list of values between certain indexes of input list"""
    sub_list: list[int] = []
    if len(input_list2) == 0 or start_index >= len(input_list2) or end_index <= 0:
        # list is empty, or indexes start too high/low
        return sub_list
    if start_index < 0:
        # index is negative
        start_index = 0
    if end_index >= len(input_list2):
        # index is larger than list
        end_index = len(input_list2)
    while start_index < end_index:
        sub_list.append(input_list2[start_index])
        # adds values between indexes to new list
        start_index = start_index + 1
    return sub_list
    # new list


def add_at_index(input_list3: list[int], added_int: int, index_added: int) -> None:
    """Places added_int at index in list"""
    if index_added < 0 or index_added > len(input_list3):
        # index is negative or larger than list length
        raise IndexError("Index is out of bounds for the input list")
        # type of error
    input_list3.append(0)
    # makes extra space in list
    index: int = len(input_list3) - 1
    while index > index_added:
        input_list3[index] = input_list3[index - 1]
        # replaces number in list with previous number
        index = index - 1
    input_list3[index_added] = added_int
    # adds desired integer to list
