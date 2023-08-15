import sys
input = sys.stdin.readline
n, q = map(int, input().split())
res = [0]*n
for _ in range(q):
    l, i = map(int, input().split())
    for j in range(l-1,n,i):
        res[j] = 1

print(res.count(0))
