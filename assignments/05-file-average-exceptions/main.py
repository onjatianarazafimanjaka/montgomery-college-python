################################################################ 
# Class: CMSC135
# Instructor: Ping Tsai
# Program Assignment:  ## Programming Assignment 5_2
# Program Name:     RAZAFIMANJAKA Onjatiana Programming Assignment 5_2.py
# Author:             RAZAFIMANJAKA Onjatiana
# Due Date:               11/07/2022
#
# Description: This program is meant to be an improvement that adds a few layers of codes the work done in Programming Assignment 5_1.  It will consist of handling some of the               
#              the possible errors that could occure whhile running the program, including the presense non-numeric data in numbers.txt file, or when the file just won't open.
#
#   I pledge that I have completed the programming assignment independently.
#   I have not copied the code from a student or any source.
#   I have not given my code to any student.
#   Print your Name here: RAZAFIMANJAKA Onjatiana
#
# Pseudocode:
#   •	Add statements allowing exception handling for when non-numeric data is present in the text saying: “Non-numeric data found in the file”
#   •	Add statements allowing exception for when the file cannot be opened   
#     
###################################################################

try:    

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

except ValueError: 
    print("Non-numeric data found in the file")
except FileNotFoundError:
    print("An error occured while trying to read the file")
    


 
    
    

       








    
    













