import sys
from itertools import permutations 

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

perms = list(permutations(arr,n))

hap = 0
for i in perms: 
    s = 0
    for j in range(n-1):
        s += abs(i[j]-i[j+1])
    
    hap = max(hap,s)
print(hap)
