import sys
from itertools import product
input = sys.stdin.readline

n,m = map(int, input().split())
N = list(map(int, input().split()))
N.sort()
for p in product(N,repeat=m):
    print(*p,sep=' ')
