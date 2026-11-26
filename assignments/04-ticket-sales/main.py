################################################################# 
# Class: CMSC135
# Instructor: Ping Tsai
# Program Assignment:  ## Programming Assignment 4
# Program Name:     RAZAFIMANJAKA_Onjatiana_PA_4.py
# Author:             RAZAFIMANJAKA Onjatiana
# Due Date:               10/25/2022
# Description: This program is meant to ask how many tickets for each class of seats were sold,
#              then displays the amount of income generated from ticket sales.
#
#   I pledge that I have completed the programming assignment independently.
#   I have not copied the code from a student or any source.
#   I have not given my code to any student.
#   Print your Name here: RAZAFIMANJAKA Onjatiana
            
# Pseudocode:
#   •	Set global constants
#   •	Define and call showIncome function
#   •	Create accumulators
#   •	Prompt for seat count for each class
#   •	Do calculations
#   •	Display results

###################################################################


# 1- Setting Global Constants                    

a = 20
b = 15
c = 10

# 2- Calculation and Result Display

def showIncome():

    incomeA = 0
    incomeB = 0
    incomeC = 0
    Total = 0

    inputA = int(input("Enter counts of A seats: "))
    inputB = int(input("Enter counts of B seats: "))
    inputC = int(input("Enter counts of C seats: "))

    incomeA += inputA * a
    incomeB += inputB * b
    incomeC += inputC * c
    Total += (incomeA + incomeB + incomeC)

    print("Income for class A seats: $", format(incomeA, ".2f"), sep="")
    print("Income for class B seats: $", format(incomeB, ".2f"), sep="")
    print("Income for class C seats: $", format(incomeC, ".2f"), sep="")
    print("Total income: $", format(Total, ".2f"), sep="")
   
# 3- Calling the Function

showIncome()

input("press enter")
