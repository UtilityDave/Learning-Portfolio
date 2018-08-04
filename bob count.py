# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:11:19 2018

@author: Utility
"""

sb = 'bob'
results = 0
sub_bob = len(sb)
for i in range(len(s)):
    if s[i:i+sub_bob] == sb:
        results += 1
print(results)