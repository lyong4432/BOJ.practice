import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    cnt = 0 
    for j,num in enumerate(a): 
        if j%5 + 1 == num:
            cnt += 1
    if cnt == 10: 
        print(i+1)
