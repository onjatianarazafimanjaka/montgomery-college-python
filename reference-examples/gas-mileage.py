print("Enter quit to exit.")

miles = ""

while miles != "quit":
    miles = input("Enter miles traveled: ")
    if miles != "quit":
        miles = int(miles)
        gallons = input("Enter gallons used: ")
        gallons = float(gallons)
        try:
            mpg = miles/gallons
        except:
            print ("\nPlease enter a non-zero value for gallons.\n")
        else:
            print ("Miles per gallon: ", mpg)
            print
    
print("Have a nice day!")