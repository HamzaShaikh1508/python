# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 22:44:22 2021

@author: hamza_sk
"""
list1 = []
n=int(input("Enter the number of elements : "))
for i in range (0,n):
    ele = int(input())
    list1.append(ele)
print(list1)    
for i in list1:
    if i>=0:
        print(i, end = " ")

    
