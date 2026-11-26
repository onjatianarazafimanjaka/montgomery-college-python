################################################################# 
# Class: CMSC135
# Instructor: Ping Tsai
# Program Assignment: Program Assignment 6
# Program Name:      RAZAFIMANJAKA Onjatiana PLab6.py
# Author:             RAZAFIMANJAKA Onjatiana
# Due Date:               01/21/2022 
# Description: This program is meant to ask for 20 numbers from the user,
#              put them in a list.  Then, it is supposed to display the lowest,
#              the highest, the total and the average.
#
#      I pledge that I have completed the programming assignment independently.
#      I have not copied the code from a student or any source.
#      I have not given my code to any student.
#      Print your Name here: RAZAFIMANJAKA Onjatiana
#
# Pseudocode: 
#
#•	Create an empty list named numList.
#•	Create an accumulator named total.
#•	Make a for loop to iterate a prompt asking user to enter a number; this will iterate 20 times.
#•	Use the functions min() and max() to find the lowest number as well as the highest number inside the list numList
#•	Calculate the average and store it in a variable named avg
#•	Display all the calculation results
#
#
#
###################################################################

# creates a list to store inputs
numList = []
# accumulator used for total 
total = 0

# iterates a loop for prompting user input, also does other calculations
for i in range(20):    
    number = float(input("Enter number {} of 20: ".format(i+1)))
    numList.append(number)
    total += number
    i += 1

# finding lowest and highest number inside of numList    
low = min(numList)
high = max(numList)

# calculating the average
avg = format(float(total / i), '.2f')

# displaying all results
print("Low: ", low)
print("High: ", high)
print("Total: ", format(float(total), '.2f'))
print("Average: ", avg) 

# asking user to press enter
input("press enter")