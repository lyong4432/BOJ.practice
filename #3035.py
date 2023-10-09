import sys

input = sys.stdin.readline
r,c,zr,zc = map(int, input().split())
N = []
for i in range(r):
    a = input().strip()
    a = list(a)
    N.append(a)

k = 0
cnt = 0
for i in range(r*zr):

    for j in range(c):
        print(N[k][j]*zc,end='')
    print()
    cnt += 1
    if cnt == zr: 
        cnt = 0
        k += 1
