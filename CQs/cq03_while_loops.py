"""A program for practicing while loops"""

__author__ = "730649404"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    # keeps tally of of how many letter have been checked
    count_of_letter: int = 0
    # keeps tally of how many letters are the same as search_char
    while count < len(phrase):
        if search_char == phrase[count]:
            count_of_letter = count_of_letter + 1
            count = count + 1
            # adds 1 if letter matches and adds 1 to amount of letter checked
        else:
            count = count + 1
            # adds 1 to amount of letters checked

    # loop runs until there is no more characters in the word to check
    return count_of_letter
    print(count_of_letter)
