################################################################# 
# Class: CMSC135
# Instructor: Ping Tsai
# Program Assignment: 3
# Program Name:      RAZAFIMANJAKA_Onjatiana_PLab3.py
# Author:            RAZAFIMANJAKA Onjatiana
# Due Date:               10/10/2022
#
# Description:
#
#   This program is meant to ask for user input on the 
#   amount of rain for each months of every input number of years 
#   and display the total rainfall in inches, as well as the monthly everage.
#
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Print your Name here: RAZAFIMANJAKA Onjatiana
#            
# Pseudocode:
#
# •  Prompt user input on numbers of years
# •  Run outer loop iterating based on the number of years entered
# •  Run a loop iterating 12 times with prompt for monthly rain
# •  Add up the total numbers of months and display the result
# •  Add up the total of rainfall and display the result in inches
# •  Calculate the average rainfall per month and display the result in inches
# •  Convert results to float and format numbers up to 2 decimal places
###################################################################


y = int(input("Enter number of years:"))                                 # prompt for number of years
m = 1                                                                                            
year = 1                                                                 
numMonths = y * 12                                                       # variable used later to display the total of months based on the numbers of years from user input                                           
totalRain = 0                                                            

while year <= y :                                                        # starts a conditional loop that will iterate based on the number of years inputed by user                                       
    print("For year", year,":", sep =" ")
    year += 1
                                                                         
    for m in range(12):                                                  # starts a count-based loop iterating until amount of rain is promted 12 times
        rain = float(input("Enter the rainfall amount for the month:"))           
        totalRain += rain            

        everageRain = (totalRain) / (numMonths)   
    m = 1                                                                # resets the value of m to 1 so the main/outer loop runs again as long as condition year <= y is still true

# The following simply display the results    
print("For", numMonths, "months")
print("Total rainfall:", format(totalRain, '.2f'), "inches")           
print("Average per month:", format(everageRain, '.2f'), "inches") 

      
    


