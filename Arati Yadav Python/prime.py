# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 19:45:47 2023

@author: Swati Yadav
"""

# Write a program to print enterd number is prime or not.
n=int(input("Enter a number:"))
if n>1:
    for i in range (2,n):
        if (n % i) == 0:
            print(n,"is not a prime number");
            break
            
        else:
            print(n,"is a prime number");
else:
    print(n,"is a prime number");
