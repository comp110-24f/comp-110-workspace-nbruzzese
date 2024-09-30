"""Basic Syntax of lists."""

my_numbers: list[float] = []  # literal

my_numbers: list[float] = list()  # constructor

my_numbers.append

# print(my_numbers)

# String Analogy
# my_name: str = "" #literal
# my_name: str = mmstr() # contructor

my_numbers.append(1.5)  # adds to list
my_numbers.append(2.3)  # adds to list

# print(my_numbers)

# Creating an already populated list
game_points: list[int] = [182, 86, 94]
print(game_points)

# Subscription Notation/Indexing
# print (game_points[2])
last_game: int = game_points[2]
# print(last_game)

# Modifying by Index
game_points[1] = 72
print(game_points)

# Getting the Length
(len(game_points))

# Removing an item
game_points.pop(1)
print(game_points)

# Function name: display
# Parameter: list of integers
# RV: None
# Print every element in the input list
# Call display on game_points


def display(int_list: list[int]) -> None:
    """Displays all elements of int_list"""
    index: int = 0
    while index < len(int_list):
        print(int_list[index])
        index += 1


display(int_list=game_points)
