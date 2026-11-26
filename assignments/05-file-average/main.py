################################################################# 
# Class: CMSC135
# Instructor: Ping Tsai
# Program Assignment:  ## Programming Assignment 5
# Program Name:     RAZAFIMANJAKA Onjatiana Programming Assignment 5.py
# Author:             RAZAFIMANJAKA Onjatiana
# Due Date:               11/07/2022
# Description: This program is meant to read string of numbers in a file named numbers.txt,
#              then to calculate and display their everage.
#              
#
#   I pledge that I have completed the programming assignment independently.
#   I have not copied the code from a student or any source.
#   I have not given my code to any student.
#   Print your Name here: RAZAFIMANJAKA Onjatiana
#
# Pseudocode:
#•	Create a middleman ‘integer’ for reading “numbers.txt”
#•      Calculate the numbers of lines containing a number using another middleman called 'integer2' (avoids calculation error)
#•	Tell program to read lines of “numbers.txt” as long as a line is not empty
#•	Make accumulator called 'add' containing the sum of the all the numbers
#•	Calculate and display the average 
#•	Close the middleman    
#     
###################################################################


add = 0
average = 0
linecount = 0

## reads the integers line by line  
integer = open("numbers.txt", 'r')
reading = integer.readline()
#print(reading)

## conts the number of lines in the file, to serve as a way to count how many numbers we have
integer2 = open('numbers.txt', 'r')
linecount = len(integer2.readlines())
#print(linecount)

## while loop meant to iterate until the last number is read
while reading != '':
    add += int(reading)
#    print(add)
    reading = integer.readline()
average += (add / linecount)

## prints and converts average to float limited to 2 decimal places        
print('Average: ', float(format((average), '.2f')))

integer.close()
input('press enter')






    
    













