# Description: This progrma asks the user for their name and adds it to a list of names.

nameList =["Alfie", "Beatrice", "Clare", "Thomas", "Vanessa"]
print("The current name list is",nameList)
newName = input("Please enter your name: ")
nameList.append(newName)
print("The new name list is",nameList)