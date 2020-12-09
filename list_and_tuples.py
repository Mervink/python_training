#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
os.system("bash --login")
import sys


"""
My examples of lists & turples
"""

#number one example

a = ['bmw', 'mercedes', 'audi', 'toyota', 'vw', 'ford']

print(a[5])
print(a[2:5])

#number two example

businessname = input ('please input your business name: ')
domain = businessname[0:-1]

print("www."+ businessname + ".com")


#example threee
mydatabase = [
    ['Mervin', '8523314'],
    ['Neville', '9769278267'],
    ['Adam', '89237889823'],
    ['Brilliant', '97238323093']
]

username = input('username: ')
password = input('Enter yoru password: ')

if [username, password] in mydatabase: print('Welcome to Sheer Driving Pleasure')
else:
    print('You do not belong here!!!!!!')



#example four 
names = ['Joburg', 'Durban', 'Cape Town', 'Eastern Cape', 'Mplumalanga']
del names[-1]
print(names)



#example five
my_list = ['soweto', 'alex', 'tembisa']
my_list.append('kagiso')
print(my_list)