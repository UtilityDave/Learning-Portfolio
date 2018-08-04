# -*- coding: utf-8 -*-
"""
Created on Thu May 31 18:02:48 2018

@author: Utility
"""

def y_or_n(question):
    answer = input(question + "(y/n): ").lower().strip()
    print("")
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        print("Input y or n")
        answer = input(question + "(y/n):").lower().strip()
        print("")
    if answer[0] == "y":
        return True
    else:
        return False

def 
    
