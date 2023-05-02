a = list(map(int, input().split()))

b = list(map(int, input().split()))

hap = 0
for i in range(3):
    if b[i] - a[i]> 0:
        hap += (b[i]-a[i])

print(hap)
