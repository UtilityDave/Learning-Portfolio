# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 18:25:40 2018

@author: Utility
"""

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)

clock = Clock('5:30')
clock.print_time()