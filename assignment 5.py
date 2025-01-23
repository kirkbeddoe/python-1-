# Input: Prompt the user to enter a time duration in hours.
# Processing: Convert the time duration to minutes and seconds.
# Output: Display the converted time duration in minutes and seconds.

#input

hours = float(input("Enter a time duration in hours: "))

#processing

minutes = hours * 60
seconds = hours * 3600

#output

print(f"The time duration is {minutes} minutes and {seconds} seconds.")