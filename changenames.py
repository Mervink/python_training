#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Using changes names
"""

import sys


def change(n):
    n[0] = "Mr Mervin"
    print(n)


names = ["mervin", "neville", "brillaint"]
change(names)
print(names)

names = ["warder", "moeta", "herman"]
change(names[:])
print(names)
