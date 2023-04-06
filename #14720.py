n = int(input())
#0 1 2 
a = list(map(int, input().split()))
for i in range(0,n):
    if a[i] == 0:
        k = i
        pre = 0
        count = 1
        break

for i in range(k,n):
    if pre == 0:
        if a[i] == 1:
            count += 1
            pre = 1
    elif pre == 1:
        if a[i] == 2:
            count +=1
            pre = 2
    elif pre == 2:
        if a[i] == 0:
            count += 1
            pre = 0

print(count)
