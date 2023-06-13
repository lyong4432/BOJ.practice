import sys
from math import gcd
input = sys.stdin.readline
a = list(map(int, input().split()))
a.sort()
if a[0] == a[1]:
    hap = a[0]
else: hap = (a[0]+a[1])*(a[1]-a[0]+1)//2
print(int(hap))
