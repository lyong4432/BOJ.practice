import sys
from itertools import product
input = sys.stdin.readline
# 중복 순열 
n,m = map(int, input().split())
N = [i for i in range(1,n+1)]

for p in product(N,repeat=m):
    print(*p,sep=' ')
