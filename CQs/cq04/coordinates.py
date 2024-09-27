"""A function for finding coordinates of words (imported to visualize.py)"""

__author__ = "730649404"


def get_coords(xs: str, ys: str) -> None:
    """Prints formatted pairs of each character of input strings"""
    xs_count: int = 0
    # count for first str
    while xs_count < len(xs):
        ys_count: int = 0
        # count for second str
        while ys_count < len(ys):
            print(f"({xs[xs_count]},{ys[ys_count]})")
            # prints letters of second str for one letter of first str
            ys_count = ys_count + 1
        xs_count = xs_count + 1
