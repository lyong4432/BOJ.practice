import sys
n, m = map(int, sys.stdin.readline().split())
s = []
cnt = 0
s = [sys.stdin.readline().strip() for i in range(n)]
a = [sys.stdin.readline().strip() for i in range(m)]

for i in a:
    if i in s:
        cnt += 1

print(cnt)
