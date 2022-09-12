'''Write a function

triple_double(num1, num2)
which takes numbers num1 and num2 and returns 1 if there is a straight 
triple of a number at any place in num1 and also a straight double of the 
same number in num2.
If this isn't the case, return 0
'''

def triple_double(num1, num2):
    num1_split = [int (digits) for digits in str(num1)]
    num2_split = [int (digits) for digits in str(num2)]
    
    recent_element_num1 = None
    recent_element_num2 = None

    for digit in num1_split:
        pass

    return num1_split

print(triple_double(555,122))