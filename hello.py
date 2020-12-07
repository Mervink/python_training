#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A simple ‘Hello, World’ program in Python
"""

def main():
   """
   Writes generic greeting, and then input a user name,
   whom it also greets.
   """
   print('Hello, World!')
   name = input("What's your name?: ")
   print("Well, hello {0}!".format(name))

if __name__ == '__main__':
   main()