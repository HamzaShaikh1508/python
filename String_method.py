# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 19:53:11 2021

@author: hamza_sk
"""
#STRING METHODS
#1:CAPITALIZE
msg = "Hello, My name is Hamza Shaikh"
print("capitalize : ",msg.capitalize())

#2:CASEFOLD
print("casefold : ",msg.casefold())

#3:CENTER
y = "Hamza"
print("center : ",y.center(20))

#4:COUNT
print("Count : ",msg.count("a"))

#5:ENDSWITH
print("Endswith : ",msg.endswith("."))

#6:EXPANTABS
txt = "H\te\tl\tl\to"
print("Expandtabs : ",txt.expandtabs(2))

#7:FIND
print("Find : ",msg.find("name"))

#8:FORMAT
txt = "For only {price:.2f} dollars!"
print("Format : ",txt.format(price = 49))

#9:INDEX
print("INDEX : ",msg.index("is"))

#10:ISALNUM
print("Isalnum : ",msg.isalnum())

#11:ISALPHA
print("Isaplha : ",msg.isalpha())

#12:ISASCII
print("Isascii : ",msg.isascii())

#13:ISDECIMAL 
print("Isdecimal : ",msg.isdecimal())

#14:ISDIGIT
print("Isdigit : ",msg.isdigit())

#15:ISIDENTIFIER
print("Isidentifier : ",msg.isidentifier())

#16:ISLOWER
print("Islower : ",msg.islower())

#17:ISNUMERIC
print("Isnumeric : ",msg.isnumeric())

#18:ISPRINTABLE
print("Isprintable : ",msg.isprintable())

#19:ISSPACE
print("Isspace : ",msg.isspace())

#20:ISTITLE
print("Istitle : ",msg.istitle())

#21:ISUPPER
print("Isupper : ",msg.isupper())

#22:JOIN
tuple1 = ('Hamza','Nazim','Shaikh')
print("Join : ",'_'.join(tuple1))

#23:LOWER
print("Lower : ",msg.lower())

#24:MAKETRANS
mytable = msg.maketrans("Shaikh", "Sheikh")
print("Maketrans : ",msg.translate(mytable))

#25:PARTITION
print("Partition : ",msg.partition("is"))

#26:REPLACE
print("Repalce : ",msg.replace('Hello','Hi'))

#27:RFIND
print("Rfind : ",msg.rfind('a'))

#28:SPLIT
print("Split : ",msg.split(","))

#29:UPPER
print("Upper : ",msg.upper())

















