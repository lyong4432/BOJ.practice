import sys

input = sys.stdin.readline
n = int(input().strip())
N = list(map(int, input().split()))
set_N = list(set(N))
set_N.sort()
dic = {}
for i,j in enumerate(set_N):
    dic[j] = i
for i in N:
    print(dic[i],end=' ')
