################################################################# 
# Class: CMSC135
# Instructor: Ping Tsai
# Program Assignment: 2
# Program Name:      LastNameFirstNamePLab2.py
# Author:             RAZAFIMANJAKA Onjatiana
# Due Date:               01/22/2022 
# Description: This program is meant to tell the user whether the date made with their input is a magic day or not.
#      I pledge that I have completed the programming assignment independently.
#  	#     I have not copied the code from a student or any source.
#  I have not given my code to any student.
#   Print your Name here: RAZAFIMANJAKA Onjatiana
#            
# Pseudocode:
#   •  Ask for user input, convert to string
#   •  Compare input with 06 /10 / 60 and 6 / 10 / 60
#   •  Display the date according to input with format (mm / dd/ yy)
#   •  Display whether the number is magic or not
###################################################################

#This asks for the user input
month = str(input("Enter the month in numeric form: "))
day = str(input("Enter the day in numeric form: "))
year = str(input("Enter the year in numeric form: "))

#This displays the date based on user input, as well as tells the user if the date is magic or not

date = month+" / "+day+" / "+year
print("The date is", date)

dateFormat1 = "06 / 10 / 60" #This needs to be string otherwise python will give an error because of the leading 0 before 6
dateFormat2 = "6 / 10 / 60"

if date == dateFormat1 or date == dateFormat2:
    print("This is a magic date.")
else:
    print("This is not a magic date.")

    
    


    


