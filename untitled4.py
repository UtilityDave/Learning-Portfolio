# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 18:45:43 2018

@author: Utility
"""

import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

#print(re.match(r'Love', data))
#print(re.search(r'Kenneth', data))
#print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))
#print(re.findall(r'\w*, \w+', data))
#print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
#print(re.findall(r'\b[trehous]{9}\b', data, re.I))
#print(re.findall(r'''
#    \b@[-\w\d.]*  # First a word boundary, an @, and then any number of characters
#    [^gov\t]+  # Ignore 1+ instances of the letters 'g', 'o', or 'v' and a tab.
#    \b  # Match another word boundary
#''', data, re.VERBOSE|re.I))
#print(re.findall(r"""
#    \b[-\w]+,  # Find a word boundary, 1+ hyphens or characters, and a comma
#    \s  # Find 1 whitespace
#    [-\w ]+  # 1+ hyphens and characters and explicit spaces
#    [^\t\n]  # Ignore tabs and newlines
#""", data, re.X))
line = re.compile(r'''
    ^(?P<name>[-\w ]*,\s[-\w ]+)\t  # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?  # Job and company
    (?P<twitter>@[\w\d]+)?$  # Twitter
''', re.X|re.M)
for match in line.finditer(data):
  print(match.group('name'))

import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'''
  (?P<last_name>[\w ]*)
  ,\s
  (?P<first_name>[\w ]*)
  :\s
  (?P<score>[\d]*)
''', string, re.X | re.M)

class Player:
  def __init__(self, last_name, first_name, score):
    self.last_name = last_name
    self.first_name = first_name
    self.score = score