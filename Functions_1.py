# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 18:18:54 2021

@author: NikhilJ
"""
import math
import cmath
import numpy as np
import pandas as pd
# Basic Function in Python

# 1. Absolute Value : Mod Function only positive values : abs()

a = -1.5 #negative float integer taken
print(abs(a)) #returns positive values

b= 1 -5j #Complex Value taken
print(abs(b)) #returns the magnitude of complex vector

c = 6+8j
print(abs(c))
print(cmath.polar(c))

# 2. all() : returns bool True iff all elements are iterable
# Iterable: It is an iterable object such as a dictionary,tuple,list,set,etc.
# Empty are also TRUE but 0 and FALSE are returned as false

ls = ('None') # this is not None it is a String
print(all(ls)) # Hence result is True
 
ls_1=['Nikhil',1,2,3,False,0]
print(all(ls_1))

t1 =(12,34,24,0,34,56) 
print(all(t1))#helpful to find 0 or False values in list returns False in such case

# 3. bool(): convert an iterable to boolean value 
# differs from all() in empty and None both returns False
print(bool(ls))
print(bool(ls_1))
t2 =() # Empty value is returned False
print(bool(t2))
t3 =False
print(bool(t3))
t4 = None
print(bool(t4))

# 4.Sum : sums up contents of list only iter
# divmod(a,b): performs division a/b : returns (quotient,remainder)

ls_2 =[2,4,6,8,10,12,14,16,18,20]
print(sum(ls_2))
print(divmod(ls_2[-3],ls_2[2]))
# using numpy module to perform basic operation
print(np.mean(ls_2))
print(np.median(ls_2))
print(np.max(ls_2))
# using lambda #user defined function
ls_3 = list(map(lambda x:x*3,ls_2)) #triplicate values in list
print(ls_3)
ls_4 = list(map(lambda x:x+10,ls_3))
print(ls_4)
ls_5 = list(filter(lambda y:y%4==0,ls_4))
ls_6 =ls_5(zip(ls_6[0:0:1]))
