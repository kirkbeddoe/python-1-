# Develop a program that prompts the user to enter the number of rows for a pattern and then prints a pattern of asterisks (*) in the form of a right triangle.

while True:

    # prompt the user to enter a number of rows
    user_input = input("Enter a number of rows:")

    # check if input is a valid positive number
    if user_input.isdigit():
        # convert the string value to an integer
        rows = int(user_input)

        # check to see if the number is greater than 0
        if rows > 0:
            print("Right triangle pattern: /n")

            # loop to generate the pattern
            for i in range(1, rows + 1):
                print("*" * i) #print * i times

            break

        else:
            print("Please enter a positive number!")

    else:
        print("Invalid input, please enter a valid number.")







