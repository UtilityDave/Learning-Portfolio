# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:30:39 2018

@author: Utility
"""

def polysum(n , s ):
    import math    
    """
    This function takes 2 arguments n and s. This function sums the 
    area and square of the perimeter of the regular polygon. it returns 
    the sum, rounded to 4 decimal places.
    """
    area = 0.25 * n * s ** 2 / ( math.tan ( math.pi / n ))
    perimeter = ( n * s ) ** 2
    return round( area + perimeter,4)