n = int(input())
arr = []
for i in range(2*n):
    arr.append(input())
cnt = 0
for i in range(n):
    if arr[i] == arr[i+n]:
        cnt += 1

print(cnt)
