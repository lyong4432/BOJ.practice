import sys
from math import sqrt
input = sys.stdin.readline
m = int(input().strip())
n = int(input().strip())

sum1 = 0
cnt = 0
min1 = 0
for i in range(m,n+1):
    if sqrt(i)%1 == 0:
        sum1 += i
        cnt += 1
        if cnt == 1: min1 = i
    
if sum1: 
    print(sum1)
    print(min1)
else: print(-1)





     
