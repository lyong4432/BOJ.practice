n, k = map(int, input().split())
arr = [[1]]*n
arr[0] = [1]

for i in range(1,n):
    res = [1,1]
    for j in range(i-1):
        res.insert(1,arr[i-1][j+1]+arr[i-1][j])

    arr[i] = res

print(arr[n-1][k-1])
