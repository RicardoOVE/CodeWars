'''A Narcissistic Number is a positive number which is the sum of its own digits, 
each raised to the power of the number of digits in a given base. In this Kata, 
we will restrict ourselves to decimal (base 10).
For example, take 153 (3 digits), which is narcisstic:
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1652 (4 digits), which isn't:
    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938'''


def narcissistic(value):

    sum_of_digits = 0

    for digit in str(value):
        digits = [int(digit)]
        for number in digits:
            pow_of_digits = pow(number, len(str(value)))
            sum_of_digits += pow_of_digits

    if sum_of_digits == value:
        narcissistic = True
    elif sum_of_digits != value:
        narcissistic = False
    return narcissistic

# Clever:
#def narcissistic(value):
#    return value == sum(int(x) ** len(str(value)) for x in str(value))

value = 153

print(narcissistic(value))
