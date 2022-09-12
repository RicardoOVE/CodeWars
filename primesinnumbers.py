'''Given a positive number n > 1 find the prime factor decomposition of n. 
The result will be a string with the following form :
 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.
Example: n = 86240 should return "(2**5)(5)(7**2)(11)"'''

'''Define a function that takes one integer argument and returns logical value 
true or false depending on if the integer is a prime.
Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 
that has no positive divisors other than 1 and itself.
Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given 
negative numbers as well (or 0).
note on performance: There are no fancy optimizations required, but still the 
most trivial solutions might time out. Numbers go up to 2^31 (or similar, depends 
on language version). Looping all the way up to n, or n/2, will be too slow.'''

def is_prime(n):

    if n <=1:
        return False

    for i in range(2, n+1):
        if n%i == 0:
            return True
        else:
            return False

print(is_prime(73))