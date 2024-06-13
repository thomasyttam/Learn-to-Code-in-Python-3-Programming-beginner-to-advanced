# Description: This program asks the user for their date of birth in the format DD-MM-YYYY, and then prints the month they were born in.

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

DoB = input("Enter your date of birth in the format DD-MM-YYYY: ")
month = int(DoB[3:5])
print("You were born in ", months[month-1])