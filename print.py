#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
All my print options
"""

import os
os.system("bash --login")
import keyword
import sys


"""
Print blank lines
"""
print(5 * "\n")

print("\n\n\n\n\n")

print(''' I am bsy with python training 1
I am bsy with python training 2
I am bsy with python training 3
I am bsy with python training 4
I am bsy with python training 5
''')


"""
Printing a list
"""

print([1, 2, 3])


"""
Printing dict
"""

print({'name': 'Mervin', 'age': 94})


"""
Printing str
"""

print('hello world')


"""
Printing a tuple
"""

x = ("adam", "brilliant", "abram")
print(x)


"""
Not which value you are printing here
"""

number = 100

print(number)
print('number')


"""
Printing Keywords
"""

print(keyword.kwlist)


"""
Formated string literals
"""

uname = 'Mervin'
text = f'User: {(uname + " ") * 3}'
print(text)
