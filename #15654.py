import sys
from itertools import permutations
input = sys.stdin.readline

n,m = map(int, input().split())
N = list(map(int, input().split()))
N.sort()
for p in permutations(N,m):
    print(*p,sep=' ')
