# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 15:22:29 2018

@author: Utility
"""

import json

with open('148.json') as artfile:
    art = json.load(artfile)
    print(art['description'])
    