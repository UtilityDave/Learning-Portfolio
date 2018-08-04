# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 18:46:18 2018

@author: Utility
"""

from dice import D20


class Hand(list):
    def __init__(self, new_hand):
        super().__init__()
        self.extend(new_hand)

    @classmethod
    def roll(cls, size, die_class=D20):
        new_hand = []
        for _ in range(size):
            new_hand.append(die_class())
        return cls(new_hand)

    @property
    def total(self):
        return sum(self)