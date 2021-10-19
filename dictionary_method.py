# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 22:13:41 2021

@author: hamza_sk
"""

#DICTIONAR METHODS
dict1 = {"Name" : "Hamza",
      "Gender " : "Male",
      "Branch" : "CS"}
#1 : CLEAR
dict1.clear()
print("Clear : ",dict1)

#2 : COPY
dict1 = {"Name" : "Hamza",
      "Gender " : "Male",
      "Branch" : "CS"}
x=dict1.copy()
print("Copy : ",x)

#3 : FROMKEYS
subjects = {'Fundamentals of data strucutre','Discrete mathematics','OOP'}
marks = 95
thisdict = dict.fromkeys(subjects,marks)
print("Fromkeys : ",thisdict)

#4 : GET
print("Get : " , dict1.get("Name"))

#5 : ITEMS
print("Items : ", dict1.items())

#6 : KEYS
print("Keys : ",dict1.keys())

#7 : POP
x=dict1.pop("Branch")
print("Pop : ",x)

#8 : SETDEFAULT
dict1 = {"Name" : "Hamza",
      "Gender " : "Male",
      "Branch" : "CS"}
print("Setdeafault : ",dict1.setdefault("Branch", "CSE"))

#9 : UPDATE
dict1.update({"DOB" : 2002})
print("Update : ",dict1)

#10 : VALUES
print("Values : ",dict1.values())