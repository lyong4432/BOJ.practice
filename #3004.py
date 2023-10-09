import sys

input = sys.stdin.readline
n = int(input().strip())

# n이 짝수일 때 
if n%2 == 0:
    n //=2
    print((n+1)**2)


# n이 홀수일 때 
else:
    n //= 2
    print((n+1)*(n+2))




