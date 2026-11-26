################################################################# 
# Class: CMSC135
# Instructor: Ping Tsai
# Program Assignment: 1
# Program Name:      Assignment1.py
# Author: Razafimanjaka Onjatiana
# Due Date:               09/12/2022 
# Description: This program is meant to display the user's information as well as calculate the amount of each ingredients needed to cook a certain number of cookies. 
#
#   I pledge that I have completed the programming assignment independently.
#   I have not copied the code from a student or any source.
#   I have not given my code to any student.
#   Print your Name here: Razafimanjaka Onjatiana
#           
# Pseudocode:
#
#   Note that the amount of each ingredient needed for 1 cookie is the amounts given in the instruction divided by 48.
#
#   Set value 1.5/48 to a variable "sugar".
#   Set value 1/48 to a variable "butter" to value 1/48.
#   Set value 2.75/48 to a variable "flour".
#
#   Prompt user input with the message "What is your name" and store it in a variable named a.
#   Prompt user input with the message "What is your street address:" and store it in a variable named b.
#   Prompt user input with the message "What is your city:" and store it in a variable named c.
#   Prompt user input with the message "What is your state:" and store it in a variable named d.
#   Prompt user input with the message "What is your ZIPCODE:" and store it in a variable named e.
#   Prompt user input with the message "Enter your cell number:" and store it in a variable named f.
#   Prompt user input with the message "Enter Major:" and store it in a variable named g.
#
#   Display a, b, c, d, e, f, g line by line.
#
#   Create a variable named h containing a prompt for user input on the number of cookies with the message "Enter the number of cookies:” and convert it to float. (Put it with other variables on the top.)
#
#   Prompt user for the number of cookies with the message “Enter the number of cookies:”.
#
#   Calculate the amount for each ingredient and display the results in 3 different lines without forgetting to set the decimanl number limit to 2.
###################################################################

name= input("What is your name:")
address= input("What is your street address:")
city= input("What is your city:")
state= input("What is your state:")
zipcode= input("What is your ZIPCODE:")
number= input("Enter your cell number:")
major= input("Enter Major:")

sugar= 1.5/48    # amount of sugar needed for 1 cookie
butter= 1/48     # amount of butter needed for 1 cookie
flour= 2.75/48   # amount of flour needed for 1 cookie

cookies= int(input("Enter the nunber of cookies:"))    # conversion to integer ensures that the calculations work without error

print(name, address, city, state, zipcode, number, major, sep='\n')

print("To make", cookies, "cookies, you will need:")

print((format(cookies * sugar, '.2f')), "cups of sugar")
print((format(cookies * butter, '.2f')), "cups of butter")
print((format(cookies * flour, '.2f')), "cups of flour")
      















      


