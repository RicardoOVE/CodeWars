'''Write a program that will calculate the number of trailing zeros in a 
factorial of a given number.'''

def zeros(n):

    number_of_zeros = 0

    while (n>=5):
        n //=5
        number_of_zeros += n

    return number_of_zeros

#Clever
def zeros2(n):
    x = n/5
    return round(x+zeros2(x)) if x else 0

n = 12
print(zeros(n))
print(zeros2(n))

