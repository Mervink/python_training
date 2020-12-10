#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Print a rectangle given a width
"""

import sys


def main(args):
    """
    Print a rectangle given a width form args or the user input
    """

    #   get from user(user `input`)

    if len(args) < 1:
        rectangular = int(args[1])
    else:
        rectangular = int(input("Rectanglar width?: "))

    # if width is not in range (1 .. 20)

    if rectangular < 1 or rectangular > 20:
        print("Error. ", rectangular, " is out of range.", file=sys.stderr)
        return 1

    # the `#` will increase every loop
    for _ in range(rectangular):
        print(rectangular * "#")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
