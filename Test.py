# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:20:33 2018

@author: Utility
"""

n = 0
while (n < 1):
    if type (varA) == str or type (varB) == str:
        print("string involved")
        n = n + 1
    elif varA > varB:
        print("bigger")
        n = n + 1
    elif varA == varB:
        print("equal")
        n = n + 1
    elif varA < varB:
        print("smaller")
        n = n + 1
    else:
        print("I'm sorry, I didn't understand")
        n = n + 1
        break