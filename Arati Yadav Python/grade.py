# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 19:44:30 2023

@author: Swati Yadav
"""

# Write a program to print grade of the student for MSRCT using marks.

marks=int(input("Enter a number:"))
if(marks>=80) and (marks<=100):
    print("student pass with first class");
elif(marks>=80) and (marks<=75):
    print("student pass with first class with distinction");
elif(marks>=65) and (marks<=75):
    print("student pass with second class");
elif(marks>=55) and (marks<=65):
    print("student pass with third class");
elif(marks>=40) and (marks<=55):
    print("student pass ");
