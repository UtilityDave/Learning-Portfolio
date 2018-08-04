# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 13:13:19 2018

@author: Utility
"""
import datetime


class Person (object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastname = name.split(' ')[-1]
    
    def setBirthday(self,month,day,year):
        self.birthday = datetime.date(year, month, day)
        
    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday.days)
    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
    def __gt__(self, other):
        if self.lastName == other.lastName:
            return self.name > other.name
        return self.lastName > other.lastName
    
    def __str(self):
        return self.name
        