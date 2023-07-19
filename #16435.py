n, length = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for i in nums: 
    if i <= length:
        length += 1

print(length)
