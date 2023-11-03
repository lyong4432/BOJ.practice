import sys


input = sys.stdin.readline
n = int(input().strip())

for i in range(n):
    N = list(map(str, input().split()))
   
    print(*N[2:],*N[:2],end=' ')
