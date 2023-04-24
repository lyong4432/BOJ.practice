import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in range(n):
    if a[i] != (1+i) :
        cnt += 1

print(cnt)
