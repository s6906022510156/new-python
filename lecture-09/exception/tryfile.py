filename = input('enter a filename: ')

try:
    infile = open(filename, 'r')
    contents = infile.read()
    print(contents)
    infile.close()

except IOError :
    print('an error occurred trying to read')
    print('the file',filename)

print("end of program")