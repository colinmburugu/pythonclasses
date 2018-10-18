#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:06:24 2018

@author: collo
"""

class Point:
    
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
    def distance_from_origin(self):
        return math.hypot(self.x,self.y)
    
    def __eq__(self,other):
        return self.x == other.x and self.y==self.y
    
    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)
    
    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)
    
    