'''Write a function that counts how many different ways you can make change for 
an amount of money, given an array of coin denominations. For example, there are 
3 ways to give change for 4 if you have coins with denomination 1 and 2:

1+1+1+1, 1+1+2, 2+2.
The order of coins does not matter:

1+1+2 == 2+1+1
Also, assume that you have an infinite amount of coins.

Your function should take an amount to change and an array of unique denominations
 for the coins:

  count_change(4, [1,2]) # => 3
  count_change(10, [5,2,3]) # => 4
  count_change(11, [5,7]) # => 0'''

import itertools
def count_change(n,l):
    count = [a for i in [itertools.product(l,repeat=x) for x in range(1,n+1)] for a in i if sum(a) == n]

    return len(set([tuple(sorted(i)) for i in count]))

#def count_change(n, l):
#    change_option = set(change(n,l))
#
#    return change_option

print(count_change(4, [1,2]))