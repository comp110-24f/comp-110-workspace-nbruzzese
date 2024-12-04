"""Turtle art!"""

from .turtle import Turtle
from math import pi

__template__ = "https://24ss2.comp110.com/static/turtle/"

DEGREE: float = -pi / 180.0


def main() -> None: ...


def click(x: float, y: float) -> Turtle:
    """Moves turtle to wherever we click on the canvas!"""
    t: Turtle = Turtle()
    t.setSpeed(10)
    t.moveTo(x, y)
    t.turnTo(90 * DEGREE)

    # code to paint flower
    # length: float = 150.0
    # while length > 0:
    #    t.forward(float(length))
    #    t.left(pi / 2.0 - pi / 8.0)
    #    length = length - 2.0
    branch(t, y * 0.15, 90 * DEGREE)

    return t


def branch(t: Turtle, length: float, angle: float) -> None:
    t.turnTo(angle)
    t.forward(length)
    # magic happens here
    if length > 3.0:  # We are going to branch!
        branch(t, length * 0.75, angle + (35 * DEGREE))
        branch(t, length * 0.75, angle - (35 * DEGREE))
    t.turnTo(angle + pi)
    t.forward(length)
