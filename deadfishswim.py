'''Wrie a simple parser that will parse and run Deadfish:
i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
'''

def parse(data):
    value = 0
    res=[]
    for c in data:
        if c=="i": value+=1
        elif c=="d": value-=1
        elif c=="s": value*=value
        elif c=="o": res.append(value)
    return res