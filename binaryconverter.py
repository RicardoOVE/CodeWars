'''
Write a function that takes an integer as input, and returns the number of bits that
 are equal to one in the binary representation of that number. You can guarantee that
  input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return
 5 in this case'''

def count_bits(n):
    one_sum = 0
    for x in bin(n)[2:].zfill(8):
        if x == str(1):
            one_sum += 1
    return one_sum


n = 15
print(bin(n)[2:].zfill(8))
print(count_bits(n))