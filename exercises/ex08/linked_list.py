"""Practice with recursive functions."""

from __future__ import annotations


class Node:
    """Creates a new class of Node."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """New Node with values and next Node."""
        self.value = value
        self.next = next


two: Node = Node(2, None)
# makes a Node "two"
one: Node = Node(1, two)
# makes a Node "one"
courses: Node = Node(110, Node(210, Node(301, None)))
# makes chain of Nodes "courses"


def value_at(head: Node | None, index: int) -> int:
    """Returns data stored at the given index."""
    if head is None:  # edge case if head is None
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:  # base case if index is 0
        return int(head.value)
    return value_at(head.next, index - 1)
    # recursive case that calls function again at next node with lower index


def max(head: Node | None) -> int:
    """Returns maximum data value in linked list."""
    if head is None:  # edge case
        raise ValueError("Cannot call max with None")
    if head.next is None:  # base case if is last node
        return head.value
    max_value: int = int(max(head.next))
    # recursive case that calls function with next node
    if head.value > max_value:
        return head.value  # returns value if it is larger than previous value(s)
    else:
        return max_value  # if new value isn't larger


def linkify(items: list[int]) -> Node | None:
    """Returns a Linked List of Nodes with the same values/order as imput."""
    if len(items) == 0:  # base case if list is empty
        return None
    return Node(items[0], linkify(items[1:]))
    # recursive case creates node w/ first item of list and calls again w/o first item


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a new list of Nodes where each value is multiplied by scaling factor."""
    if head is None:  # base case if head is None
        return None
    return Node((head.value) * factor, scale(head.next, factor))
    # recursive case multiplies node value by factor/calls again with new value/factor
    # (same factor every time)
