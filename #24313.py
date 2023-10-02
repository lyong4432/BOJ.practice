import sys

input = sys.stdin.readline
a1,a0 = map(int, input().split())
c = int(input().strip())
n0 = int(input().strip())

# f(n) = a1n + a0 / g(n) = n / f(n) <= c*g(n)
if a1 * n0 + a0 <= c * n0 and c >= a1:
    print(1)
else: print(0)
