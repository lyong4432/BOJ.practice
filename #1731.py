import sys

input = sys.stdin.readline
n = int(input().strip())
N = []
for i in range(n):
    a = int(input().strip())
    N.append(a)

if N[2]-N[1] == N[1]-N[0]:
    d = N[1]-N[0]
    print(N[-1]+d)
elif N[2]//N[1] == N[1]//N[0]:
    r = N[1]//N[0]
    print(N[-1]*r)
