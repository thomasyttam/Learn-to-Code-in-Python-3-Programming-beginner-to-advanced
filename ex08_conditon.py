print("Exercise 08 - Conditional Statements - Calculate BMI")
weight = float(input("Please input your weight in kg: "))
height = float(input("Please input your height in m: "))

bmi = weight / (height ** 2)

print("Your BMI is: ", round(bmi,2))
if bmi <= 18.5:
    bmiclass = "underweight"
elif bmi >18.5 and bmi <= 24.9:
    bmiclass = "normal weight"
elif bmi > 24.9 and bmi <= 29.9:
    bmiclass = "overweight"
else:
    bmiclass = "obesity"
print("The classification of your BMI is: ", bmiclass)