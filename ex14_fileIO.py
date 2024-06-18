# Desription: This program demonstrate the use of file I/O.

# create a file
# try to create a file
fileName = input("Please enter the name of the file you want to create: ")
try:
    file = open(fileName, "x")
    file.close()
except:
    print("The file already exists.")

file = open(fileName, "r")

fileContext=file.read()
print(fileContext)