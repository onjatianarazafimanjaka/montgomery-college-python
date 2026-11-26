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
#
#
#
###################################################################

numList = []
total = 0
n = 0

for i in range(20):    
    number = int(input("Enter number: "))
    numList.append(number)
    total += number
    n += 1
    
low = min(numList)
high = max(numList)
avg = format(float(total / n), '.2f')

print("Low: ", low)
print("High: ", high)
print("Total: ", total)
print("Average: ", avg) 

input("press enter")

    

