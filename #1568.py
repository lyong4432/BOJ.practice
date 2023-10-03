import sys

input = sys.stdin.readline
n = int(input().strip())
cnt = 0
i = 1
while True:
    if i > n:
        i = 1
    n -= i
    cnt += 1
    i += 1
    if n == 0: break
print(cnt)
