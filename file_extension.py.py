# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 12:45:46 2021

@author: hamza_sk
"""

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
