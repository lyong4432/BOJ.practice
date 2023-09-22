import sys

input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().split()))

up = [0]
hap = 0
for i in range(n-1):
    if nums[i] < nums[i+1]:
        hap += (nums[i+1]-nums[i])
        up.append(hap)
    else: 
        
        hap = 0
        
print(max(up))
