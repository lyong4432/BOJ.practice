import sys
input = sys.stdin.readline


n = int(input())
N = list(map(int, input().split()))
k = int(input())
M = []
hap = 0
for i in N: 
    hap += i
    M.append(hap)
for _ in range(k):
    a,b = map(int, input().split())
    if a != 1:
        print(M[b-1] - M[a-2])
    else: print(M[b-1])
