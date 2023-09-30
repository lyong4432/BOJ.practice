import sys
from itertools import combinations
input = sys.stdin.readline

n = input().strip()
N = list(n)
arr = []
def com(a,i):
    for j in range(0,len(n)-i+1):
        b = N[j:j+i]
        b = str.join("",b)
        
        arr.append(b)
    
for j in range(1,len(n)+1):
    com(N,j)
   
arr = set(arr)

print(len(arr))

