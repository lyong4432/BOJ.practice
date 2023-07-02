import sys
input = sys.stdin.readline
res = []

while True: 
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    nums.pop(0)
    arr = []
    for i in nums:
        if len(arr) >= 1:
            if arr[-1] != i:
                arr.append(i)
        else: arr.append(i)
    arr.append('$')
    res.append(arr)

for i in res: 
    for j in i: 
        print(j, end=' ')
    print()
