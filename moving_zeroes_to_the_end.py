'''Write an algorithm that takes an array and moves all of the zeros to the end,
 preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]'''

def move_zeros(array):

    correct_array = []
    zeros_array = []

    for number in range(len(array)):
        if array[number] != 0:
            correct_array.append(array[number])
        elif array[number] == 0:
            zeros_array.append(array[number])

    return correct_array+zeros_array

#clever
def move_zeros2(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

#clever
def move_zeros3(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)

#print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))

