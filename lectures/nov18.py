"""Recursive Factorial Function."""


def factorial(n: int) -> int:
    """Calculates factorial of int n."""
    # Base Case
    if n == 0 or n == 1:
        return 1
    # Recursive Case
    else:
        return n * factorial(n - 1)


# Example Usage
print(factorial(3))
