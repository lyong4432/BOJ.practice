import sys
input = sys.stdin.readline

N = [[0 for _ in range(1001)] for _ in range(1001)]

test = int(input())

for t in range(test):
    a, b, w, h = map(int, input().split())
    for i in range(a, a+w):
        for j in range(b,b+h):
            N[i][j] = t+1



for t in range(test):
    cnt = 0
    for i in range(1001):
        cnt += N[i].count(t+1)
    print(cnt)
