# Description: This program asks the user for their age and then compares it to the author's age.

myAge = 45
yourAge = int(input("Enter your age: "))
if yourAge > myAge:
    print("You are older than me.")
elif yourAge < myAge:
    print("You are younger than me.")
else:
    print("We are the same age.")