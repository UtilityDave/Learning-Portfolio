# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 17:56:49 2018

@author: Utility
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

larg_item = ['',0]
if len(aDict) ==0:
    return None 
for (k,v) in aDict.items():
    if len(v)>larg_item[1]:
       larg_item[0]=k
       larg_item[1]=len(v)

return larg_item[0]