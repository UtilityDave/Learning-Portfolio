# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 17:33:13 2018

@author: Utility
"""

class RaceCar:
    laps = 0 

    def __init__ (self, color, fuel_remaining, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        for attribute, values in kwargs.items():
            setattr(self, attribute, values)

    def run_lap(self, length):
        self.fuel_remaining -= length * 0.125 
        self.laps += 1