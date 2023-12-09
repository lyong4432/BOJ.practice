import sys
import math
input = sys.stdin.readline

n = int(input())
N = list(map(int, input().split()))

for i in range(n-1):
    c = math.gcd(N[0],N[i+1])
    print(f'{N[0]//c}/{N[i+1]//c}')
