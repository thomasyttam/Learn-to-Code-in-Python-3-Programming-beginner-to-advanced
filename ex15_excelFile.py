# Desription: This program demonstrate how to access excel file.

import pandas as pd

excelContent = pd.ExcelFile("sales.xlsx") # read the excel file
listName =excelContent.sheet_names # get the list of sheet names


# print the content of the excel file of each sheet
for i in listName:
    print(excelContent.parse(i))
    print("*********************************")

sheet=[]
for i in listName:
    sheet.append(excelContent.parse(i))

print(type(excelContent))
print(type(listName))
print(type(excelContent.parse(listName[0])))
print(type(sheet))

print(sheet[0].loc[0])