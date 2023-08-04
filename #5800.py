import sys
input = sys.stdin.readline
n = int(input().strip())
for i in range(n):
    nums = list(map(int, input().split()))
    k = nums[0]
    nums = nums[1:]
    nums.sort()
    print(f'Class {i+1}')
    arr = []
    for j in range(k-1):
        arr.append(nums[j+1]-nums[j])
    arr.sort()

    print(f'Max {nums[-1]}, Min {nums[0]}, Largest gap {arr[-1]}')
