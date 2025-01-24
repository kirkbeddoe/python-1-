# Input: Prompt the user to enter their age.
# Processing: Classify the age into different categories:
# Output: Display the category based on the entered age.

#input
age_input = input("Please enter your age:")

# check if the input is a number and is not empty
if age_input.isdigit():
    age = int(age_input)

    # ensure that the age is positive
    if age > 0:
        # start classification
        if age < 18:
            print("Minor")
        elif 18 <= age <= 65:
            print("adult")
        else:
            print("Senior Citizen")
    else:
        print("Age must be a positive integer")
else:
        print("Error: Invalid Input, please enter a positive number")

