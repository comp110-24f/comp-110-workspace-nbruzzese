"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730679404"


def input_word() -> str:
    """takes word and finds out if 5 letters"""
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
        # if word is 5 letters, continues with program
    else:
        print("Error: Word must contain 5 characters.")
        quit()
        # exits out of program


def input_letter() -> str:
    """takes letter and finds out if it is only 1 letter"""
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
        # if letter is only 1 letter, continues with program
    else:
        print("Error: Character must be a single character.")
        quit()
        # exits out of program


def contains_char(word: str, letter: str) -> None:
    """checks if letter matches letters in word"""
    count: int = 0
    print("Searching for " + letter + " in " + word)
    if letter == word[0]:
        count = count + 1
        print(letter + " found at index 0")
        # checks if letter matches index, adds 1 to count of letters that match
    if letter == word[1]:
        count = count + 1
        print(letter + " found at index 1")
        # checks if letter matches index, adds 1 to count of letters that match
    if letter == word[2]:
        count = count + 1
        print(letter + " found at index 2")
        # checks if letter matches index, adds 1 to count of letters that match
    if letter == word[3]:
        count = count + 1
        print(letter + " found at index 3")
        # checks if letter matches index, adds 1 to count of letters that match
    if letter == word[4]:
        count = count + 1
        print(letter + " found at index 4")
        # checks if letter matches index, adds 1 to count of letters that match
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    if count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    """brings all functions together"""
    contains_char(word=input_word(), letter=input_letter())
    # calls all functions in program


if __name__ == "__main__":
    main()
