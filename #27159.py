n = int(input())
nums = list(map(int, input().split()))
pre = nums[0]
hap = pre
for i in nums[1:]:
    if pre + 1 != i:
        hap += i
    pre = i

print(hap)
