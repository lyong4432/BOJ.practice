import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
d = a-b
c = b-a
print(len(c)+len(d))
