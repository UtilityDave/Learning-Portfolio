# -*- coding: utf-8 -*-
"""
Doesn't work yet. needs debug.
Created on Wed May 30 18:20:07 2018
Plugboard Function - need to figure 
out better variable names for this 
program.
@author: Utility
"""

def steckerboard(enciphered, steckerin, steckerout):
    [steckerout if x == steckerin else x for x in enciphered]
    return enciphered
    print(enciphered) 
    
    
    