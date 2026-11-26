def enterName():
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    print("Your name is: ", firstname, lastname)
    reverseName(firstname, lastname)
    
def reverseName(first, last):
    print("Your name reversed is: ", last, first)
    
enterName()

    
