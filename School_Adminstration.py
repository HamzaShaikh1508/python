# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:33:35 2021

@author: hamza_sk
"""
import csv

def write_info_csv(info_list):
    with open("student_info.csv", "a", newline='' ) as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name", "Age", "Email-id", "contact-no."])
            
        writer.writerow(info_list)
    
if __name__=='__main__':
    condition = True
    student_num = 1
    while (condition):
        student_info = input("Enter students information for student#{} in in the format (Name Age Email-id contact-no.) : ".format(student_num))
        student_info_list = student_info.split(" ")
      
        print("\nEntered info is \nName: {}\nAge: {}\nEmail-id: {}\nContact-no.: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check = input("Enter yes/no if information is correct")
        if choice_check=="yes":
            write_info_csv(student_info_list)
            
            condition_check = input("enter yes/no if you want to enter information of anotherr student : ")
            if condition_check=="yes":
                condition = True
                student_num = student_num + 1
            else:
                condition = False
        elif choice_check=="no":
            print("\nEnter correct info")
    
