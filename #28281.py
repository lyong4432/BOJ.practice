n, x = map(int, input().split())
nums = list(map(int, input().split()))
arr = []
for i in range(n-1):
    a = (nums[i] + nums[i+1]) * x
    arr.append(a)

arr.sort()
print(arr[0])
