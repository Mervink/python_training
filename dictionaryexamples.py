#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Multiples ways to attend to dictionaries
"""
import sys


# Create and print a dictionary
testdict = {"brand": "BMW", "model": "M8", "year": 2020}
print(testdict)


# Print the "brand" value of the dictionary
testdict = {"brand": "BMW", "model": "M8", "year": 2020}
print(testdict["brand"])


# Overwrite existing values
testdict = {"brand": "BMW", "model": "M8", "year": 2012, "year": 2019}
print(len(testdict))


# String, int, boolean, and list data types
testdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
}
print(testdict)


# Print the data type of a dictionary:
testdict = {"brand": "BMW", "model": "M8", "year": 2020}
print(type(testdict))


# List of tuples
listofTuples = [("Hello", 7), ("hi", 10), ("there", 45), ("at", 23), ("this", 77)]
print(listofTuples)
