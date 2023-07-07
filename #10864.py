import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(m):
    a, b = map(int, input().split())
    arr.append(a)
    arr.append(b)
    
for i in range(n):
    print(arr.count(i+1))
