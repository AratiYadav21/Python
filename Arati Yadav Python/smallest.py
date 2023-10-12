# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 19:45:12 2023

@author: Swati Yadav
"""

# Write a program to print smallet number between 4 numbers.

a=int(input("Enter the any number:"));
b=int(input("Enter the any number:"));
c=int(input("Enter the any number:"));
d=int(input("Enter the any number:"));
if(a<b) and(a<c) and(a<d):
    print("a is smallest number");
elif(b<a) and(b<c)and(b<d):
    print("b is smallest number");
elif(c<a) and(c<b) and(c<d):
    print("c is smallest number");
else:
    print("d is smallest number");
