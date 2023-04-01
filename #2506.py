n = int(input())
arr = list(map(int, input().split()))
combo = 1
sum = 0
for i in arr:
    sum += (combo * i)
    if i == 0 :
        combo = 1
    else:
        combo += 1

print(sum)
