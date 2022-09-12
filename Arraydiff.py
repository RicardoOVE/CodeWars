'''Your goal in this kata is to implement a difference function, which 
subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b 
keeping their order.
array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:
array_diff([1,2,2,2,3],[2]) == [1,3]'''

def array_diff(a,b):
    
    c = a.copy()

    for item_a in a:
        for item_b in b:
            if item_a == item_b and item_a in c:
                c.remove(item_a) #remove by value in c
    
    if not a or not b:
        c = a
        
    return c

#Clever
def array_diff2(a,b):
    return [x for x in a if x not in b]

print(array_diff([1,2,2], [2]))
print(array_diff2([1,2,2], [2]))