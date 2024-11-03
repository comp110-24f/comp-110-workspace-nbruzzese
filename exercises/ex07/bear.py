"""File to define Bear class."""

__author__ = "730649404"


class Bear:
    """Makes new class of Bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """New bear."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """What happens every day for bear."""
        self.age = self.age + 1
        self.hunger_score = self.hunger_score - 1
        # lowers hunger_score once a day
        return None

    def eat(self, num_fish: int):
        """Increases hunger score by number of fish eaten."""
        self.hunger_score = self.hunger_score + num_fish
        # increases hunger_score by how many fish eaten
