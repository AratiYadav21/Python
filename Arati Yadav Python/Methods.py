# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 19:24:38 2023

@author: Swati Yadav
"""

# Demonstrate the use of list methods.

L1 = [123,'xyz','zara','abc',123]
L2 = [2011,'sai']
print(L1)

L1.append(2009)           # Append() Method
print("Updated list:",(L1))

print ("Count for 123:",(L1.count(123)))      # Count() Method

L1.extend(L2)               # extend() Method
print ("Extended list:",(L1))

print ("Index for zara:",(L1.index('zara')))    # Index() Method

L2.insert(3,2008)           # Insert() Method
print ("Final list:",(L2))

print ("List:",(L2.pop(1)))           # pop() Method

L1.remove('xyz')           # remove() Method
print ("List:",(L1))

L1.reverse()               # revrerse() Method
print ("List:",(L1))

L2.sort()                 # Sort() Method
print ("List:",(L2))

