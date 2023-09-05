# 블로그 참고한 코드 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
start, end, cnt, hap = 0,0,0,0

while True:
    if hap >=m:
        hap -= nums[start]
        start += 1
    elif end == n: break
    else: 
        hap += nums[end]
        end += 1
    if hap == m: cnt += 1

print(cnt)

# 원래 코드 (시간초과) 
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
for i in range(1,n+1):
    for j in range(n-i+1):
        if sum(nums[j:i+j]) == m:
            cnt += 1



print(cnt)"""
