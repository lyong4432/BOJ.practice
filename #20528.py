n = int(input())
nums = list(map(str, input().split()))
j = 1
for i in range(1,len(nums)):
    if nums[i-1][-1] != nums[i][0]:
        j = 0
        break
print(j)
