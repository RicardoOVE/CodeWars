import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
m = int(input())

if n%43 == m%43:
    print(m%43)
else:
    print("The digitwise products are NOT the same")
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

