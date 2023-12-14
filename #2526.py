import sys
input = sys.stdin.readline


n, p = map(int, input().split())
M = []

k = n
cnt = 0
while True: 
    k = (k * n) % p
    if k in M: 
        print(len(M)-M.index(k))
        break
    M.append(k)
