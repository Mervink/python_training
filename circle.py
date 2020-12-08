#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculate area and circumference of a circle, given a radius. The
user is prompted for the radius. No error checking or validation!
"""

import sys
import math


def main(args):
    """
    The `main` function prompts the user for the radius, and without
    error checking calculate and print the circle's attributes.
    """
    # Use a command-line argument if available.
    if len(args) > 1:
        radius = to_float(args[1])
    else:  # Prompt user and input a `radius`.
        radius = to_float(input("Radius?: "))

    # Validate the input. Must be a positive number.
    if radius is None:
        sys.stderr.write("Error. Bad input.")
        return 1
    if radius < 0.0:
        sys.stderr.write("Error. Negative radius.")
        return 2

    # Calculate and save the circumference (C = 2¶R).
    circum = circ_circum(radius)
    # Calculate and save the area (A = ¶R^2).
    area = circ_area(radius)

    # Print the circumference and area.
    print("Circum:", circum)
    print("Area  :", area)

    return 0


def to_float(instr, fail=None):
    """
    An exception-free “conversion” from a string to a `float`. Optionally,
    caller can specify what to return for invalid input (a default).
    """
    try:
        return float(instr)
    except ValueError:
        return fail


def circ_circum(radius):
    """
    Calculate the circumference of a circle given a radius.
    """
    assert radius >= 0.0
    return 2.0 * math.pi * radius


def circ_area(radius):
    """
    Calculate the area of a circle given a radius.
    """
    assert radius >= 0.0
    return math.pi * radius ** 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
