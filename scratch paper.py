# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 17:03:24 2018

@author: Utility
"""
import datetime
def minutes(dtime1, dtime2):
    deltat = dtime2 - dtime1
    return round(deltat.total_seconds() / 60)

def to_string(datetime):
	return datetime.strftime("%d %B %Y")

def from_string(date, string): 
  return datetime.datetime.strptime(date, string)

moscow = datetime.timezone(datetime.timedelta(hours=4))
pacific = datetime.timezone(datetime.timedelta(hours=-8))
india = datetime.timezone(datetime.timedelta(hours=+5.5))

import datetime
import pytz

fmt = '%m-%d %H:%M %Z%z'
starter = datetime.datetime(2015, 10, 21, 4, 29)

pacific = pytz.timezone('US/Pacific')
local = pacific.localize(starter)
pytz_string = local.strftime(fmt)

import re

def first_number(string):
    return(re.search(r'\d',string))
    
def find_emails(string):
    return re.findall(r'[-\w\d+.]+@[\w\d.]+', string)  

print(re.findall(r'''
  ^([-\w ]*,\s[\w ]+?)\t
  ([-\w\d.]+@[-\w\d.]+)\t #email
  ([\(?\d{3}\)\s?\d{3}-?\d{4}])\t #Phone
  ([\w\s.]+,\s[\w\s.]+)\t? # Job and company
  (@[\w\d]+)?$ #Twitter
''', data, re.X|re.MULTILINE))
  