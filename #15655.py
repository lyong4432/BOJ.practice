import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int, input().split())
N = list(map(int, input().split()))
N.sort()
for p in combinations(N,m):
    print(*p,sep=' ')
