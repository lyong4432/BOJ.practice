import sys


input = sys.stdin.readline

a,b = map(int, input().split())
N = []
temp = cnt = 1

for i in range(b):
    N.append(temp)
    if temp == cnt : 
        cnt = 0
        temp += 1
    cnt += 1
print(sum(N[a-1:b]))
