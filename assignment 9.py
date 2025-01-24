# Input: Ask the user to enter a single character.
# Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
# Output: Display whether the entered character is a vowel or a consonant.

#input
char = input("Please enter a single character: ")

#processing and output
if len(char) == 1 and char.isalpha():
    # convert the letter to lowercase
    char = char.lower()

    # check if the char is a vowel
    if char in 'aeiou':
        print("The character is a vowel")
    else:
        print("The character is a consonant")
else:
    if len(char) != 1:
        print("Please enter only 1 character")
    else:
        print("Error: The character is not a letter")
