# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 20:43:26 2018

@author: Utility
"""

import re

def firstAndLast(string):
    re.sub(r'/s[^-/w/d/s]/s)]',string,"")
    print(string)