import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n,m = map(int, input().split())
N = list(map(int, input().split()))
N.sort()
for p in combinations_with_replacement(N,m):
    print(*p,sep=' ')
