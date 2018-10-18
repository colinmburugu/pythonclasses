#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 11:42:50 2018

@author: collo
"""

class Circle:
    
    def __init__(self,radius):
        self.radius=radius
    
    @property
    def mradius(self):
        return self.radius
    
    #@gradius.setter
    
    def gradius(self,radius):
        if radius < 0:
            print('radius can\'t be negative')
        else:
            self.radius=radius
    gradius = property(fset=gradius)
    
    @property
    def area(self):
        return  3.142 * (self.radius **2)
    
    @property
    def circumfrence(self):
        return 3.142 *2*self.radius
    
    
c1=Circle(-10)
print(c1.mradius)
    