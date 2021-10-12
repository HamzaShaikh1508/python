# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:28:03 2021

@author: hamza_sk
"""

print("SELECT OPERATION")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter a choice (1/2/3/4) : "))
x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

if (choice == 1):
    print("The Addition is = ",(x+y))
elif (choice == 2):
    print("The subtraction is = ",(x-y))
elif (choice == 3):
    print("The multiplication is = ",(x*y))
elif (choice == 4):
    print("The divison is = ",(x/y))
else:
    print("Invalid choice")    