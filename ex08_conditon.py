weight = float(input("Please input your weight in kg: "))
height = float(input("Please input your height in m: "))
bmi = weight / (height ** 2)
print("Your BMI is: ", round(bmi,2))
if bmi <= 18.5:
    print("You are underweight")
elif bmi >18.5 and bmi <= 24.9:
    print("You are normal weight")
elif bmi > 24.9 and bmi <= 29.9:
    print("You are overweight")
else:
    print("You are obesity")