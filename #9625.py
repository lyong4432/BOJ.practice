k = int(input())
arr = [0] * (k+1)
arr[1] = 1

for i in range(2, k+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[k-1],arr[k])
