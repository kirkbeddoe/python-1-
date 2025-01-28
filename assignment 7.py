# Input: Prompt the user to enter a year.
# Processing: Determine whether the entered year is a leap year or not. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
# Output: Display whether the entered year is a leap year or not.

#input
year = int(input("Please enter a year: "))

#processing & output
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
