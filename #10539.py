import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().split()))
result = []
pre = 0
for i,k in enumerate(nums):
    now = k * (i+1)
    result.append(now-pre)
    pre = now

print(*result,sep=' ')
