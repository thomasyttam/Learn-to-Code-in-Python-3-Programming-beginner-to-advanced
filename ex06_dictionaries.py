# Description: This progmram demonstrates the use of dictionaries in Python.

person = {"name":"Thomas", "gender":"male", "age":25, "address": "Norh York", "phone":"416-123-4567"}
key = input("Please enter the information you want to know about the person: ").lower()
inforequest = person.get(key,"Sorry, I don't know that information.")
print(inforequest)