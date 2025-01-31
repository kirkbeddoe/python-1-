# create a loop to check for valid input

while True:

    # ask the user to enter a string
    user_input = input("Enter a string: ")

    # remove spaces and convert the string to lowercase
    convert_input = user_input.replace(" ", "").lower()

    # check if the input is empty
    if convert_input == "":
        print("Please enter a valid string!")
        continue

    # create 2 pointers to check the left and right of your string
    left = 0
    right = len(convert_input) - 1

    plindrome = True

    while left < right:
        if convert_input[left] != convert_input[right]:
            plindrome = False
            break

        # move the pointers closer to the center
        left += 1
        right -= 1

    if plindrome:
        print("The string is plindrome -> ", user_input)
    else:
        print("The string is not plindrome -> ", user_input)

    break