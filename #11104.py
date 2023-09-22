import sys

input = sys.stdin.readline

n = int(input().strip())
for i in range(n):
    a = input().strip()
    a = int(a,2)
    print(a)
