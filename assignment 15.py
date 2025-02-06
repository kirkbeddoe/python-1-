import math

def is_prime(number):
    # if number is less than 2 that means it is a prime number
    if number <= 1:
        return False
    # if the number is 2 then it is prime
    if number == 2:
        return True

    # skip even numbers greater than 2
    if number % 2 == 0:
        return False

    # check the divisibility up to the square root of number
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False

    return True

print(is_prime(29))
