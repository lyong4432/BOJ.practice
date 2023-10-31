import sys
input = sys.stdin.readline
n = int(input().strip())
m = int(input().strip())
N = list(map(int,input().split()))

cnt = 0

for i in N:
    if m-i in N:
       cnt +=1


print(cnt//2)

# 정답을 보고 추론했다고 해야되나.. 
