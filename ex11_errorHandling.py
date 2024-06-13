# Description: This program demonstrates how to handle errors in Python.

data_valid = False

while data_valid == False:
    try:
        grade1 = float(input("Enter the grade of the first test: "))
        if grade1 < 0 or grade1 > 10:
            print("Grade should be between 0 and 10")
        else:
            data_valid = True
    except:
        print("Invalid input. Only numbers between 0 and 10 are accepted.")

data_valid = False

while data_valid == False:
    try:
        grade2 = float(input("Enter the grade of the second test: "))
        if grade2 < 0 or grade2 > 10:
            print("Grade should be between 0 and 10")
        else:
            data_valid = True
    except:
        print("Invalid input. Only numbers between 0 and 10 are accepted.")

data_valid = False

while data_valid == False:
    try:
        total_classes = float(input("Enter the total number of classes: "))
        if total_classes <= 0:
            print("The number of classes can't be zero or less")
        else:
            data_valid = True
    except: 
        print("Invalid input. Only numbers greater than zero are accepted.")
        

data_valid = False

while data_valid == False:
    try:
        absences = float(input("Enter the number of absences: "))
        if absences < 0 or absences > total_classes:
            print("The number of absences can't be less than zero or greater than the total number of classes")
        else:
            data_valid = True
    except:
        print("Invalid input. Only numbers between 0 and", total_classes, "are accepted.")

avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) / total_classes

print("Average grade: ", round(avg_grade,2))
print("Attendance rate: ", str(round((attendance * 100),2))+'%')

if avg_grade >= 6 and attendance >= 0.8:
    print("The student has been approved")
elif avg_grade < 6 and attendance < 0.8:
    print("The student has failed due to an average grade lower than 6.0 and an attendance rate lower than 80%")
elif avg_grade >= 6 and attendance < 0.8:
    print("The student has failed due to an attendance rate lower than 80%")
else:
    print("The student has failed due to an average grade lower than 6.0")
