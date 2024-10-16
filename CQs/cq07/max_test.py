"""tests for find_max"""

__author__ = "730649404"

from CQs.cq07.find_max import find_and_remove_max

# imports function from find_max.py file


def test_return_value_goodinput() -> None:
    """find_and_remove max should return max value of list"""
    example_list: list[int] = [1, 1, 3, 3, 5]
    assert find_and_remove_max(example_list) == 5
    # desired response is 5


def test_updated_list() -> None:
    """find_and_remove max should mutate list to remove max values"""
    example_list: list[int] = [1, 1, 3, 3, 5]
    find_and_remove_max(example_list)
    assert example_list == [1, 1, 3, 3]
    # desired response is [1,1,3,3] (5 is removed)


def test_return_value_badinput() -> None:
    """find_and_remove_max should return -1 if list is empty"""
    example_list: list[int] = []
    assert find_and_remove_max(example_list) == -1
    # desired response is -1
