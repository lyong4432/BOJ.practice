a = list(map(int, input().split()))
a.sort()

hap = a[2]-a[1] + a[2] -a[0]

print(hap)
