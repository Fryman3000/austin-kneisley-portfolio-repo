#BMI Calculator

#program that calculates the Body Mass Index (BMI) from a user's weight and height.
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi_float = float(weight) / float(height)**2

bmi = int(bmi_float)
print(bmi)