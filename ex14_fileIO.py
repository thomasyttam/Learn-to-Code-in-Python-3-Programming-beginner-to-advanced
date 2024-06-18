# Desription: This program demonstrate the use of file I/O.

import pandas as pd

# create a file
fileName = input("Please enter the name of the file you want to create: ")

try:
    file = open(fileName, "x")
    file.close()
except:
    print("The file already exists.")

# read the file
file = open(fileName, "r")

fileContext=file.read()
print(fileContext)

file.close()

# write to the file

file = open(fileName, "w")
fileInput = input("Please enter the text you want to write to the file: ")
file.write(fileInput)
file.close()

excelContent = pd.ExcelFile("sales.xlsx")
print(excelContent)