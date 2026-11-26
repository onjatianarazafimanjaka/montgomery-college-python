# This program writes three lines of data
# to a file.
def main():
    # Open a file named philosophers.txt.
    outfile = open('names.txt', 'w')
    # Write the names of three philosphers
    # to the file.
    outfile.write('1.John Wick\n')
    outfile.write('2. David Blaine\n')
    outfile.write('3. Edmund Freud\n')
    # Close the file.
    outfile.close()
# Call the main function.
main()
