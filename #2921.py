import sys

input = sys.stdin.readline
n = int(input().strip())
hap = 0
for i in range(1,n+1):
    for j in range(0,i+1):
        # print(i,j)
        hap += (i+j)

print(hap)
