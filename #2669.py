import sys 
input = sys.stdin.readline
N = [[0]*101 for _ in range(101)]
hap = 0
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1,x2):
        for k in range(y1,y2): 
            N[j][k] = 1


print(sum(sum(N,[])))
