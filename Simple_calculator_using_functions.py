# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 22:23:44 2021

@author: hamza_sk
"""
def add_numbers(x,y):
    sum = x+y
    return sum

def subtract_numbers(x,y):
    sub = x-y
    return sub

def product_numbers(x,y):
    product = x*y
    return product

def division_numbers(x,y):
    division = x/y
    return division

print("SELECT OPERATION")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter a choice (1/2/3/4) : "))
x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

if (choice == 1):
    print("The Addition is = ",add_numbers(x,y))
elif (choice == 2):
    print("The subtraction is = ",subtract_numbers(x,y))
elif (choice == 3):
    print("The multiplication is = ",product_numbers(x,y))
elif (choice == 4):
    print("The divison is = ",division_numbers(x,y))
else:
    print("Invalid choice")