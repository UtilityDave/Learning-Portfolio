# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:33:25 2018
FizzBuzz
@author: Utility
"""
count = 1

while count <= 100:
    if count % 3 == 0 and count % 5 == 0:
        print ("FizzBuzz")
        count += 1
    elif count % 5 == 0:
        print ("Buzz")
        count += 1
    elif count % 3 == 0:
        print ("Fizz")
        count += 1
    else:
        print (count)
        count += 1
        
