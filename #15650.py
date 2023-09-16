import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int, input().split())
N = [i for i in range(1,n+1)]

for p in combinations(N,m):
    print(*p,sep=' ')
