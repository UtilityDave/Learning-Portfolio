# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:11:37 2018

@author: Utility
"""

long = ''
c = ''
for char in s:
    if (c == ''):
        c = char
    elif (c[-1] <= char):
        c += char
    elif (c[-1] > char):
        if (len(long) < len(c)):
            long = c
            c = char
        else:
            c = char
if (len(c) > len(long)):
    long = c
print(long)