import sys

input = sys.stdin.readline

n = int(input())
for i in range(n):
    k = int(input())
    
    print(2**k-1)
