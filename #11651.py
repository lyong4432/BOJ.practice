import sys
import math
input = sys.stdin.readline
t = int(input().strip())
res = []
for i in range(t):
    a,b = map(int, input().split())
    res.append([a,b])

res.sort(key=lambda x: (x[1], x[0]))

for i,j in res:
    print(i, j ,sep =' ')
