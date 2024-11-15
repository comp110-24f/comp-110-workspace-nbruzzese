"""Practice with recursive functions."""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a str representation of a linked list."""
        rest: str = "TODO"
        # TODO: figure out the rest of the list
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))
print(one)
print(str(courses))
print(courses)


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # Base case: When head is the "last" node
    if head.next is None:
        return head.value
    else:
        # Recursive case:
        rest: int = last(head.next)
        return rest


print(last(courses))  # Expect to print 301


def recursive_range(start: int, end: int) -> Node | None:
    """Build a list recursivly from start to end."""
    if start > end:
        raise ValueError("Invalid arguements")
    if start == end:
        # Base Case
        return None
    else:
        # Recursive Case
        # 1. Handle the first value in your new list here!
        first: int = start
        # 2. Let the rest of the list be handled recursively!
        rest: Node | None = recursive_range(start + 1, end)
        # 3. Return a new node which is first followed by rest
        return Node(first, rest)


a_list: Node | None = recursive_range(110, 113)
print(a_list)
