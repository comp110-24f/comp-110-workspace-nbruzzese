"""Practice Concatenating Variables (imported to visualize.py)"""

__author__ = "730649404"

word1: str = "happy"
word2: str = "tuesday"
# global variables


def concat(word_one: str, word_two: str) -> str:
    "Concatenates two strings"
    return word_one + word_two


if __name__ == "__main__":
    # only runs when concatenation file is "main" function
    print(concat(word_one=word1, word_two=word2))
