'''
Bob is preparing to pass IQ test. The most frequent task in this test is to find out 
which one of the given numbers differs from the others. Bob observed that one number 
usually differs from the others in evenness. Help Bob — to check his answers, he needs 
a program that among the given numbers finds one that is different in evenness, and 
return a position of this number.
! Keep in mind that your task is to help Bob solve a real IQ test, which means 
indexes of the elements start from 1 (not 0)
'''
def iq_test(numbers):
    numbers_list = numbers.split(" ")

    list_mod = [int(s)%2 for s in numbers_list ]
    if list_mod.count(1) > 1:
        poss = list_mod.index(0)
    else:
        poss = list_mod.index(1)
    
#    num = numbers_list[poss]

    return (poss+1)

numbers = "2 4 7 8 10"

print(iq_test(numbers))
