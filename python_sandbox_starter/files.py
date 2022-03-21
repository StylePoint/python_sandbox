# Python has functions for creating, reading, updating, and deleting files.

# Open a file (mode of file W = write)
myFile = open('myFile.txt', 'w')

# Get info
print('Name:', myFile.name)
print('Is closed:', myFile.closed)
print('Opening mode:', myFile.mode)

# Write to file
myFile.write("I love Python")
myFile.write(" and JavaScript")
myFile.close()

# Append to file mode = "a" for append, if we use "w" it will just overwrite it
myFile = open("myFile.txt", "a")
myFile.write(" I also like phgp")
myFile.close()

# Read from file
myFile = open("myFile.txt", "r+")
text = myFile.read(100)
print(text)