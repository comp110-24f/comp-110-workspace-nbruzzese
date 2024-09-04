"""A program for planning a tea party"""

__author__ = "730649404"


def main_planner(guests: int) -> None:
    """Brings all functions together and prints output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # concatenates str, guests: int (as str), and then another str
    print("Tea Bags: " + str(tea_bags(people=guests)))
    # calls tea_bags function
    print("Treats: " + str(treats(people=guests)))
    # calls treats function
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))
    # calls tea_bags and treats functions


def tea_bags(people: int) -> int:
    """number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """number of treats needed"""
    return int(tea_bags(people) * 1.5)
    # calls tea_bags function


def cost(tea_bags: int, treats: int) -> float:
    """Total cost of treats and tea bags"""
    return (tea_bags * 0.50) + (treats * 0.75)
    # calls tea_bags function and treats function


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
