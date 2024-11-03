"""File to define River class."""

__author__ = "730649404"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Makes new class of River."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Makes sure fish are young enough to live."""
        bears_alive: list[Bear] = []
        # keeps track of alive bears
        fish_alive: list[Fish] = []
        # keeps track of alive fish
        for a_bear in range(0, len(self.bears)):
            if (self.bears[a_bear]).age <= 5:
                bears_alive.append(self.bears[a_bear])
                # adds bear to list if they are <= 5 old
        for a_fish in range(0, len(self.fish)):
            if (self.fish[a_fish]).age <= 3:
                fish_alive.append(self.fish[a_fish])
                # adds fish to list if they are <= 3 old
        self.bears = bears_alive
        # updates list to only alive bears
        self.fish = fish_alive
        # updates list to only alive fish
        return None

    def remove_fish(self, amount: int):
        """Removes amount of fish from front of list."""
        count: int = 0
        while count < amount:
            # removes amount of fish count specifies
            self.fish.pop(0)
            # removes fish from front
            count = count + 1
        return None

    def bears_eating(self):
        """Removes eaten fish."""
        for a_bear in self.bears:
            if len(self.fish) >= 5:
                # if there are still 5 fish left
                self.remove_fish(3)
                # removes 3 fish for every bear
                a_bear.eat(3)
                # adds 3 to hunger_score for bear
        return None

    def check_hunger(self):
        """Checks if bear has starved -> remove bear."""
        bears_alive: list[Bear] = []
        # keeps track of alive bears
        for a_bear in self.bears:
            if a_bear.hunger_score >= 0:
                # if bear did not starve
                bears_alive.append(a_bear)
                # adds bear to survivor list
        self.bears = bears_alive
        # updates list to only survivor bears
        return None

    def repopulate_fish(self):
        """Models reproduction of fish."""
        new_fish: int = (len(self.fish) // 2) * 4
        # how many new fish will be produced based on current fish population
        for pair_fish in range(0, new_fish):
            self.fish.append(Fish())
            # adds new fish to overall fish list
        return None

    def repopulate_bears(self):
        """Models reproduction of bears."""
        new_bears: int = len(self.bears) // 2
        # how many new bears will be produced based on current bear population
        for pair_bear in range(0, new_bears):
            self.bears.append(Bear())
            # adds new bears to overall bear list
        return None

    def view_river(self):
        """Prints status of river."""
        print(f"~~~ Day {self.day}: ~~~")
        # hot many days have passed
        print(f"Fish population: {len(self.fish)}")
        # population of fish
        print(f"Bear population: {len(self.bears)}")
        # population of bears
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Calls one_river_day 7 times."""
        count: int = 0
        while count < 7:
            # repeats 7 days
            self.one_river_day()
            # one day of activities
            count = count + 1
