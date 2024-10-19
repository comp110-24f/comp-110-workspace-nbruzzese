"""ex05 (practice testing imported functions)"""

__author__ = "730649404"

from exercises.ex05.utils import only_evens, sub, add_at_index

import pytest

# imports functions from utils.py and pytest


def test_only_evens_empty() -> None:
    """checks empty list"""
    example_list: list[int] = []
    assert only_evens(example_list) == []
    # desired response is an empty list


def test_only_evens_return_only_evens() -> None:
    """checks returned list"""
    example_list: list[int] = [2, 5, 6, 9]
    assert only_evens(example_list) == [2, 6]
    # desired response is [2,6]


def test_only_evens_original() -> None:
    """checks original list"""
    example_list: list[int] = [3, 5, 6, 8]
    only_evens(example_list)
    assert example_list == [3, 5, 6, 8]
    # desired response is [3,5,6,8]


def test_sub_large_index() -> None:
    """checks given starting index larger than list"""
    example_list: list[int] = [1, 3, 9, 12]
    assert sub(example_list, 6, 10) == []
    # desired response is an empty list


def test_sub_return_sub_list() -> None:
    """checks returned list"""
    example_list: list[int] = [2, 5, 6, 9, 10]
    assert sub(example_list, 1, 4) == [5, 6, 9]
    # desired response is [5, 6, 9]


def test_sub_original() -> None:
    """checks original list"""
    example_list: list[int] = [2, 5, 6, 8]
    sub(example_list, 1, 3)
    assert example_list == [2, 5, 6, 8]
    # desired response is [2,5,6,8]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    example_list: list[int] = [2, 3, 4]
    # your object to pass to add_at_index function
    with pytest.raises(IndexError):
        add_at_index(example_list, 5, 7)
        # an IndexError is raised for the case when the add_at_index is given an <index_to_insert_num>
        # that is greater than the length of our <list_object>
        # desired response is an error


def test_add_at_index_return():
    """checks return"""
    example_list: list[int] = [7, 2, 8]
    assert add_at_index(example_list, 2, 1) == None
    # desired response is None (no return)


def test_add_at_index_original():
    """checks original list"""
    example_list: list[int] = [2, 3, 4, 5]
    add_at_index(example_list, 1, 0)
    assert example_list == [1, 2, 3, 4, 5]
    # desired response is [1,2,3,4,5]
