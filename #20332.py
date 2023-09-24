a = int(input())
nums = list(map(int, input().split()))
if sum(nums)%3 == 0: print('yes')
else: print('no')
