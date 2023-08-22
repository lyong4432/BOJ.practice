import sys
from math import sqrt
input = sys.stdin.readline
n = int(input().strip())
res = {}
for i in range(n):
    w, h = map(int, input().split())
    ppi = sqrt(w**2+h**2)/24
    res[i+1] = ppi

res = dict(sorted(res.items(), key=lambda x: x[0]))
res = dict(sorted(res.items(), key=lambda x: x[1], reverse=True))

for i in res.keys():
    print(i)
