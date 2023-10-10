import sys

input = sys.stdin.readline
n = int(input().strip())
hap = 0
for i in range(1,n):
    hap += (i*n+i)

print(hap)
