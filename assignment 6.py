# Input: Ask the user to enter an amount in one currency (e.g., USD).
# Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
# Output: Display the converted amount in the target currency.

# input

currency_usd = float(input("Enter an amount in USD currency: "))

#processing

exchange_rate = 0.85
currency_eur = currency_usd * exchange_rate

#output

print(f"The amount in EUR is {currency_eur}.")
