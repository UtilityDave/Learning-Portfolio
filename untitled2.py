# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 17:29:03 2018

@author: Utility
"""

import random



class Die:
    def __init__(self,sides=2,value=0):
        if not sides >=2:
            raise ValueError("Must have at least 2 sides")
        if not isinstance(sides, int):
            raise TypeError("Sides must be a whole number")
        if not isinstance(value, int):
            raise TypeError("Value must be a whole number")
        self.value = value or random.randint(1,sides)
        
    def __int__(self):
        return self.value    
    def __eq__(self, other):
        return int(self) == other    
    def __ne__(self, other):
        return int(self )!= other
    def __gt__ (self, other):
        return int(self) > other
    def __lt__ (self, other):
        return int(self) < other
    def __ge__(self, other):
        return int(self) > other or int(self) == other
    def __le__ (self, other):
        return int(self) < other or int(self) == other
    def __add__ (self, other):
        return int(self) + other
    def __radd__(self, other):
        return int(self) + other
    def __repr__(self):
        return(self.value)
            
        
class D6(Die):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)
        
class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You Must Provide a Die class")
        super().__init__()
        """
        This loop could work in the machine cipher class.
        """
        for _ in range(size):
            self.append(die_class)()
        
    def _by_value(self, value):
        dice = []
        for die in self:
            if die == value:
                dice.append(die)
        return dice
    
            

class YatzyHand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size=5, die_class=D6, *args, **kwargs)
        
    @property
    def ones(self):
        returnself._by_value(1)
    @property
    def ones(self):
        returnself._by_value(2)
    @property
    def ones(self):
        returnself._by_value(3)
    @property
    def ones(self):
        returnself._by_value(4)
    @property
    def ones(self):
        returnself._by_value(5)
    @property
    def ones(self):
        returnself._by_value(6)
    @property
    def _sets(self):
        return {
                1: len(self.ones),
                2: len(self.twos),
                3: len(self.threes),
                4: len(self.fours),
                5: len(self.fives),
                6: len(self.sixes)
                }
        
class YatzyScoresheet:
    def score_ones(self,hand):
        return sum(hand.ones)
    def score_twos(self,hand):
        return sum(hand.twos)
    def score_threes(self,hand):
        return sum(hand.threes)
    def score_fours(self,hand):
        return sum(hand.fours)
    def score_fives(self,hand):
        return sum(hand.fives)
    def score_sixes(self,hand):
        return sum(hand.sixes)
    
    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, countr in hand._sets.items():
            if count == set_size:
                scores.append(worth*set_size)
        return max(scores)
    
    def score_one_pair(self, hand):
        return self._score_set(hand, 2)
    
    def score_yatzy(self, hand):
        if len(set(hand)) == 1:
            return 50
        else:
            return 0
        
class CapitalismHand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size=2, die_class=D6, *args, **kwargs)
        
    @property
    def ones(self):
        return self._by_value(1)
    
    @property
    def twos(self):
        return self._by_value(2)
    
    @property
    def threes(self):
        return self._by_value(3)
    
    @property
    def fours(self):
        return self._by_value(4)
    
    @property
    def fives(self):
        return self._by_value(5)
    
    @property
    def sixes(self):
        return self._by_value(6)
    
    @property
    def _sets(self):
        return {
            1: len(self.ones),
            2: len(self.twos),
            3: len(self.threes),
            4: len(self.fours),
            5: len(self.fives),
            6: len(self.sixes)
        }
    @property
    def doubles(self):
        if self[0] == self[1]: # was 'if self._by_value[0] =self._by_value[1]:'
            return True # was 'True'
        else:
            return False 
    @classmethod
    def reroll(self):
        ch = CapitalismHand()
        return ch