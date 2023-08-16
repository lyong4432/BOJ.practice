import sys
input = sys.stdin.readline

arr = []
n = int(input().strip())

for i in range(n):
    arr.append(int(input().strip()))

arr.sort()

for i in arr: print(i)
