''' Your task is to write a function which returns the sum of following series 
upto nth term(parameter). 
You need to round the answer to 2 decimal places and return it as String.
If the given value is 0 then it should return 0.00
You will only be given Natural Numbers as arguments'''

#def series_sum(n):
#    return str("{:.2f}".format(sum(n)))  #when given a defined series i.e n = [1, 0.25]

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

#def series_sum(n):
#    answer = 0
#    for numbers in range(n):
#        answer += 1.0/(3 * numbers + 1)
#    return '{:.2f}'.format(answer)

n = 3

#n = [1, 0.25]
#print(series_sum(n))
#n = [0]
print(series_sum(n))