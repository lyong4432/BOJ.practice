import sys

input = sys.stdin.readline

for _ in range(int(input().strip())):
    n = int(input().strip())
    N = list(map(int, input().split()))
    N.sort()
    print((N[-1]-N[0])*2)
