# Description: This program demonstrats the use of random module and lists.

import random

nameList=[]

print("Please input eight names and I will print one of them randomly.")

while len(nameList) < 8:
    newName = input("Please enter a name: ")
    nameList.append(newName)

randomName = nameList[random.randint(0,7)]

print("One of the name you entered is: ", randomName)