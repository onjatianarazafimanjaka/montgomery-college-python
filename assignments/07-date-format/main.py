################################################################# 
# Class: CMSC135
# Instructor: Ping Tsai
# Program Assignment: 7
# Program Name:          RAZAFIMANJAKA Onjatiana Chap8 PA7.py
# Author:                         RAZAFIMANJAKA Onjatiana
# Due Date:                           12/01/2022 
# Description: This program is meant to read a string from the user containing 
#                          a date in the form mm/dd/yyyy and print the date in the format March 12, 2018.
#
#                   I pledge that I have completed the programming assignment independently.
#                   I  have not copied the code from a student or any source.
#                   I have not given my code to any student.
#                   Print your Name here: RAZAFIMANJAKA Onjatiana
#                   
# Pseudocode: 
#•	Define a function called main()
#•	Make a variable date, prompting the user for a date in the format mm/dd/yyyy
#•	Create variables mm, dd, yyyy each of them containing the value associated with the month, day, and year respectively, then store them in the variables named m, d, y
#•	Make a Boolean expression that will result to true if the length of the variable date is different from 10, which is the number of characters for a valid date format.  This reset the program if true.
#•	Iterate a for loop turning mm into the corresponding month of the year
#•	Make variables d, y containing the string versions of the day and the year
#•	Display the date in the m d, y format if the respective variables are not empty
#
###################################################################


def main():
             
        date = input("Enter a date in the format mm/dd/yyyy: ")
        mm = date[0:2]
        dd = date[3:5]
        yyyy = date[6:]
        m = ''
        d = ''
        y = ''


        if len(date) != 10:
                print("Please insert a valid date.")
                main()

        for i in range(len(date)):

                if mm == "01":
                        m = "January"
                if mm == "02":
                        m = "February"
                if mm == "03":
                        m = "March"
                if mm == "04":
                   m = "April"
                if mm == "05":
                        m = "May"  
                if mm == "06":
                        m = "June"
                if mm == "07":
                   m = "July"
                if mm == "08":
                        m = "August"
                if mm == "09":
                        m = "September"
                if mm == "10":
                        m = "October"
                if mm == "11":
                        m = "November"
                if mm == "12":
                        m = "December"

        d = dd

        y = yyyy

        if m != "" and d != "" and y != "":
                print(m, d+",", y)
main()

print("press enter")



