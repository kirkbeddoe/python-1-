# Input: Prompt the user to enter their weight in kilograms and height in meters.
# Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
# Output: Display the calculated BMI

weight = float(input("enter your weight in kilograms: "))
height = float(input("enter your height in meters: "))

# processing

bmi = weight / (height ** 2)

# output

print("Your BMI is: ", bmi)
