n = int(input())
nums = list(map(int, input().split()))
nums.sort()
cnt = 0
for i in range(len(nums)):
    if i+1 != nums[i]:
        print(i+1)
        cnt = 1
        break
if cnt == 0: print(n+1)
