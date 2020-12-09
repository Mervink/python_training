#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program that prints the multiplication table from 1..12
"""

import sys

def main(args):
   """
   Get `multiplier` from command-argument, else, prompt the user.
   """
   
   if len(args) > 1:
      multiplier = int(args[1])
   else:
      multiplier = int(input("Multiplier?: "))

   # Validate that `multiplier` is in the range `1`..`12` inclusive.

   if multiplier < 1 or multiplier > 12: 
      print("Error. Out of range.", file=sys.stderr)
      return 1

   for n in range(1, 12+1):
      print('{:2} x {:2} = {:3}'.format(n, multiplier, n * multiplier))

   return 0

if __name__ == '__main__':
   sys.exit(main(sys.argv))