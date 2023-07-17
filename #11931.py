import sys
input = sys.stdin.readline

n = int(input().strip())
res = []
for i in range(n):
    res.append(int(input().strip()))

res.sort(reverse=True)
for i in res: print(i)
