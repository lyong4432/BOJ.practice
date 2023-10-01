import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
N = {}
cnt = 0
for i in range(n):
    a = input().strip()
    N[a] = 0
for i in range(m):
    a = input().strip()
    if a in N.keys():
        N[a] = 1
        cnt += 1

N = dict(sorted(N.items(), key=lambda x:x[0]))

print(cnt)
for k,v in N.items():
    if v == 1:
        print(k)
