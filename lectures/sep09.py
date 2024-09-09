"""Practice with conditionals"""


def less_than_10(num: int) -> bool:
    """tell me if num is less than 10."""
    if num < 10:
        print("Small Number")
    else:
        print("Big Number")
    print("Have a nice day!")


# less_than_10(num=11)


def should_i_eat(hungry: bool) -> None:
    """Tells me whether to eat based on hunger."""
    if hungry:  # conditional/bool expression
        print("eat food")  # then block
    else:
        print("do comp110 hw instead")  # else block
    print("ur welcome")


# should_i_eat(hungry=True)


def check_first_letter(word: str, letter: str) -> str:
    """checks to see if first letter matches letter"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
