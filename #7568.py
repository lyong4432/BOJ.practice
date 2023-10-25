import sys

input = sys.stdin.readline
N = []
Y = []
n = int(input().strip())
for i in range(n):
    x,y=map(int, input().split())
    N.append([x,y])

for i in range(n):
    cnt = 1
    for j in range(n):
        if N[j][0] > N[i][0] and N[j][1] > N[i][1]:
            cnt += 1
    Y.append(cnt)

print(*Y,sep=' ')
