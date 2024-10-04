"""Mutating Functions."""

__author__ = "730649404"

list_1: list[int] = [1, 2, 3]
# global variable
list_2: list[int] = list_1
# global variable


def manual_append(input_list: list[int], new_number: int) -> None:
    """Adds new_number to list"""
    input_list.append(new_number)
    # append = add (for lists)


def double(double_list: list[int]) -> None:
    "Doubles values of list"
    index: int = 0
    while index < len(double_list):
        # Repeats until the index is the same as the length of list
        double_list[index] = 2 * (double_list[index])
        # doubles each index of double_list
        index = index + 1


double(double_list=list_2)

print(list_1)
print(list_2)
