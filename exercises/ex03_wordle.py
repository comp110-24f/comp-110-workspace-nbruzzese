"""EX03 - Wordle - The word guessing game"""

__author__ = "730649404"


def input_guess(secret_word_len: int) -> str:
    """Checks if word guess matches word length"""
    word_guess: str = input(f"Enter a {secret_word_len} character word: ")
    # f{} allows arguement to be concatinated more easily
    while len(word_guess) != secret_word_len:
        word_guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
        # f{} allows arguement to be concatinated more easily
    return word_guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if any letters in word match letter guess"""
    assert len(char_guess) == 1
    # guessed char must be only 1 char
    count: int = 0
    while count < len(secret_word):
        if secret_word[count] == char_guess:
            return True
            # if word containes letter
        else:
            count = count + 1
    return False
    # if word does not contain letter


def emojified(guess: str, secret: str) -> str:
    """Concatinates string of emojis corresponding to checked letters of a word"""
    assert len(guess) == len(secret)
    # length of guessed word and secret word must be the same
    WHITE_BOX: str = "\U00002B1C"
    # Code for emoji
    GREEN_BOX: str = "\U0001F7E9"
    # Code for emoji
    YELLOW_BOX: str = "\U0001F7E8"
    # Code for emoji
    count: int = 0
    added_emojis: str = ""
    # emojis will be added to this string as while loop works
    while count < len(secret):
        if guess[count] == secret[count]:
            added_emojis = added_emojis + (GREEN_BOX)
            # correct letter, right place
        elif contains_char(secret_word=secret, char_guess=guess[count]) == True:
            added_emojis = added_emojis + (YELLOW_BOX)
            # correct letter, wrong place
        else:
            added_emojis = added_emojis + (WHITE_BOX)
            # wrong letter
        count = count + 1
    return added_emojis


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    # keeps track of how many turns have passed
    word_guess: str = input_guess(secret_word_len=len(secret))
    # word player guessed on turn
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        print(emojified(guess=word_guess, secret=secret))
        if word_guess == secret:
            print(f"You won in {turn}/6 turns!")
            # if game is won
        else:
            word_guess = input_guess(secret_word_len=len(secret))
            turn = turn + 1
            # if player got word wrong but still has guesses

    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")
        quit()
        # game lost (out of turns)


if __name__ == "__main__":
    main(secret="codes")
