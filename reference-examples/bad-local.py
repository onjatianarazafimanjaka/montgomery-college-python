# Definition of the main function.
def main():
    name = get_name()
    print('Hello', name)     

# Definition of the get_name function.
def get_name():
    name = input('Enter your name: ')
    return name

# Call the main function.
main()
