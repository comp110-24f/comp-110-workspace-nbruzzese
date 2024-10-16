"""Function that finds and removes max value(s) of a input list"""

__author__ = "730649404"


def find_and_remove_max(input: list[int]) -> int:
    """Finds/removes max value of list"""
    if input == []:
        # if list is empty
        return -1
    max_int: int = input[0]
    # keeps track of max value of list
    index: int = 0
    while index < len(input):
        if input[index] > max_int:
            max_int = input[index]
            # updates max value of list if value is greater than previous
            index = index + 1
        else:
            index = index + 1
    second_index: int = 0
    # new index starting at 0
    while second_index < len(input):
        if input[second_index] == max_int:
            input.pop(second_index)
            # removes value from list if it is highest value
            second_index = 0
        else:
            second_index = second_index + 1
    return max_int
