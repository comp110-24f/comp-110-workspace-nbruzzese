"""Practice with conditionals, variables, and elif"""


def less_than_10(num: int) -> bool:
    """tell me if num is less than 10."""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small Number")
    else:
        print("Big Number")
    print("Have a nice day!")


# less_than_10(num=5)


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


# print(check_first_letter(word="happy", letter="h"))


def get_weather_report() -> str:
    """tells the weather instructions"""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
