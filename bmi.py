# create a program that calculates your bmi

height=float(input("Enter your height in metres: "))
weight=float(input("Enter your weight in kilograms: "))
bmi=weight/height**2
print("Your BMI is:",bmi)
if bmi<18.5:
    print("Your are underweight")
elif 18.5 <= bmi < 29.9:
    print("Your are normal weight")
else:
    print("Your are overweight")