
def power(base, exponent):
    # if the exponent is 0, any based raised to 0 is 1
    if exponent == 0:
        return 1

    # if the exponent is negative, calculate the reciprocal of the positive power
    if exponent < 1:
        return 1 / power(base, -exponent)
    
    # multipy base by itself exponent times
    result =1
    for _ in range(exponent):
        result *= base

    return result

print(power(2, 3))
print(power(5,0))
print(power(2, -2))