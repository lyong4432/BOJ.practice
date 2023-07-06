import sys
import math
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    new = str(math.factorial(n))
    for i in new[::-1]:
        if i != '0':
            print(i)
            break
