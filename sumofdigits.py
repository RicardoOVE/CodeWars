''' Given n, take the sum of the digits of n. If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. The input 
will be a non-negative integer. '''
'''
def digital_root(n):
    
    digits = [int(x) for x in str(n)]
    digits_sum = sum(digits)
    if len(str(digits_sum)) > 1:
        return digital_root(digits_sum)

    return digits_sum
'''
def digital_root(n):
    print(n%9)
    print(n and 9)
    return n%9 or n and 9 

n = 1599
print(f"n= " + str(n) + ", digits sum = " + str(digital_root(n)))

