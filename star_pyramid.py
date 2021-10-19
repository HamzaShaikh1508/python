# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 23:03:54 2021

@author: hamza_sk
"""
n = int(input("Enter  range : ")) 
k = 2*n - 2
for i in range (0,n):
    for j in range (0,k):
        print(end = " ")
    k = k - 1
    for j in range (0,i+1):
        print("*",end = " ")
    print("\r")   
    
    
        
        
    