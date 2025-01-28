# Input: Ask the user to enter their marks for three subjects.
# Processing: Calculate the average of the marks. Determine the grade based on the average:
# 90 and above: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
# Output: Display the calculated grade.

#input
mark1 = float(input("Enter you mark for your first class:"))
mark2 = float(input("Enter your mark for your second class:"))
mark3 = float(input("Enter your mark for your third class:"))

#processing - calculate the average
average = (mark1 + mark2 + mark3) / 3

#output
print(f"The average of {mark1}, {mark2} and {mark3} is {average}." )