# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 16:18:30 2018

@author: Qiao Yu
"""

def polysum(n,s):
    """
    n is the number of a regular polygon's sides.
    s is the length of each side.
    """
    import math
    # The area of a regular polygon:
    def area(n,s):
        return 0.25 * n * s**2 /math.tan(math.pi/n)
    # The perimeter of a polygon:
    def perimeter(n,s):
       return n * s
    return round(area(n,s)+perimeter(n,s)**2, 4)
