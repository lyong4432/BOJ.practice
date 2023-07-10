n = int(input())
for i in range(n):
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    print(nums[2])
