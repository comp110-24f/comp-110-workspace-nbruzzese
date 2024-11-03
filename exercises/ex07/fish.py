"""File to define Fish class."""

__author__ = "730649404"


class Fish:
    """Makes new class of Fish."""

    age: int

    def __init__(self):
        """New fish."""
        self.age = 0
        return None

    def one_day(self):
        """What happens every day for fish."""
        self.age = self.age + 1
        return None
