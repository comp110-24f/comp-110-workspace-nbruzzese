"""My first CQ in COMP110!"""

__author__ = "730649404"


def mimic(message: str) -> str:
    """Will return message back"""
    return message


def main() -> None:
    """print result of mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
