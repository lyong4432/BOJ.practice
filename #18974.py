import itertools
import sys 
input = sys.stdin.readline


n = int(input())
arr = [i for i in range(1,n+1)]
nPr = itertools.permutations(arr, n)

for i in nPr: 
    print(*i)
