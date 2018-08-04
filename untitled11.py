# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:17:01 2018

@author: Utility
"""
balance = 42
annualInterestRate = 0.2
monthlyInterestRate = (annualInterestRate/12)
minimumMonthlyPayment = (0.4)
month = 0
while month <= 12:
    balance = ((balance - minimumMonthlyPayment) * (1 + monthlyInterestRate))
     month = 1 + month
    if balance <= 0 and month == 12:
        break
    elif balance > 0 and month == 12:
        month = 0
        minimumMonthlyPayment + 1.00

print str('Lowest Payment: ' + str(round(minimumMonthlyPayment, 2)))