from math import gcd
import sys
input = sys.stdin.readline

n = int(input().strip())
if n == 2:
    a,b = map(int, input().split())
    g = gcd(a,b)
elif n == 3: 
    a,b,c = map(int, input().split())
    g = gcd(a,gcd(b,c))


for i in range(1,g+1):
    if g%i == 0: print(I)


# python3로 제출하면 계속 시간초과라고 뜨는데 pypy3로 제출하니까 괜찮았음. 왜지?
