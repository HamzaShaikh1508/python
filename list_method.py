# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 20:56:32 2021

@author: hamza_sk
"""

#LIST METHODS
#APPEND
cars = ['Bugati Veyron','Pagani','Lamborghini']
cars.append("Supra")
print(cars)

#CLEAR
cars.clear()
print("Clear : ",cars)

#COPY
cars = ['Bugati Veyron','Pagani','Lamborghini']
print("Copy : ",cars.copy())

#COUNT
print("Count : ",cars.count('Pagani'))

#EXTEND
fruits = ['apple', 'banana', 'cherry']
cars.extend(fruits)
print("Extend : ",cars)

#INDEX
print("Index",cars.index("apple"))

#INSERT
cars.insert(2,"BMW")
print("Insert : ",cars)

#POP
cars.pop(2)
print("pop : ",cars)

#REMOVE
cars.remove('apple')
print("Remove : ",cars)

#REVERSE
cars.reverse()
print("REverse : ",cars)

#SORT
cars.sort()
print("Sort : ",cars)