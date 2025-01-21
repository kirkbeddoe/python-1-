# prompt the user to enter or input 3 different amounts for 3 different variables

principal = float(input("enter the principal amount: "))

# prompt the user to enter the interest rate

rate = input("Enter the interest rate: ")
interest_rate = float(rate)

# prompt the user to enter the time period

time = float(input("enter the time period: "))

# calculate and process the simple interest

simple_interest = (principal * interest_rate * time) / 100

# output the simple interest

print("the calculated simple interest is:", simple_interest)
