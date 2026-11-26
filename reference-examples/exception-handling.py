# This program displays the contents
# of a file.
def main():
    # Get the name of a file.
    filename = input('Enter a filename: ')
    try:
        # Open the file.
        infile = open(filename, 'r')
        # Read the file's contents.
        contents = infile.read()
        # Display the file's contents.
        print(contents)
        # Close the file.
        infile.close()
    except ValueError:
        print('Unsupported content found')
    except FileNotFoundError:
        print('There was an error while trying to open the file', filename)
# Call the main function.
main()
