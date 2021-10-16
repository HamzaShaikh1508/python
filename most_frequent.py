# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 10:30:54 2021

@author: hamza_sk
"""
word = input("Enter a String : ")
def most_frequent(string):
    dict1 = dict()
    for key in string:
        if key not in dict1:
            dict1[key] = 1
        else:
            dict1[key] += 1
    return dict1
print (most_frequent(word))
    
    