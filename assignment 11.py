# Write a program that generates the Collatz sequence for a given positive integer entered by the user. The Collatz sequence is generated iteratively by repeatedly applying the following rules:
# If the current number is even, divide it by 2.
# If the current number is odd, multiply it by 3 and add 1.

#Create a loop to go through the numbers until it reaches 1

while 'true':
    # prompt the user to enter a positive number
    user_input = input("Enter a positive number: ")

    #check if the input is a number
    if user_input.isdigit():
        # convert the string value to an integer
        num = int(user_input)

        # check if the number is a positive number
        if num > 0:
            print("Collatz sequence starting from: ", num)

            # create a loop to handle the collatz sequence
            while num != 1:

                print(num, end=" -> ")

                # check if the number is even
                if num % 2 == 0:

                    # if its even
                    num //= 2
                else:
                    num = 3 * num + 1
            print(1)
            break

        else:
            print("Please reenter a positive number! ")

    else:
        print("Invalid input. Please enter a valid number")