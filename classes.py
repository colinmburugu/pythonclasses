#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 19:00:15 2018

@author: collo
"""

class Student:
    no_of_students =0
    
    def __init__(self,fname,lname,regno,age):
        self.name=fname
        self.lname=lname
        self.regno=regno
        self.age=age
        
        Student.no_of_students=+1
        
    
        
     
    @property  
    def get_firstname(self):
        return self.name
    @property 
    def get_lastname(self):
        return self.lname
    @property 
    def get_regno(self):
        return self.regno
    
    def get_age(self):
        return self.age
    gett_age=property(get_age)
    
    
    def set_firstname(self,fname):
        self.name = fname
    set_firstname=property(fset=set_firstname)
    

    def set_lastname(self,lname):
        self.lname=lname
    set_lastname=property(fset=set_lastname)
    
    @set_regno.setter
    def set_regno(self,reg):
        self.regno=reg    

    
    def set_age(self,age):
        self.age=age
    set_age=property(fset=set_age)
    
    @property
    def students_details(self):
        return  'student\'s name is' +' '+self.name +' '+self.lname +' and registration number is'+' ' +self.regno 
    
        
    