import sys

input = sys.stdin.readline
n = int(input().strip())
for i in range(n):
    N = list(map(int, input().split()))
    N.sort()
    if N[3]-N[1] >=4:
        print('KIN')
    else: print(sum(N[1:4]))
