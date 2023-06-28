nums = list(map(int, input().split()))

sorted_nums = sorted(nums)

if nums == sorted_nums:
    print("Good")
else: print("Bad")
