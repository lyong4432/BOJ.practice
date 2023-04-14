a = list(map(int, input().split()))
a.sort()
d1 = a[1] - a[0]
d2 = a[2] - a[1]

if d1 == d2:
    print(a[2]+d1)
elif d1>d2:
    print(a[0]+d2)
else:
    print(a[1]+d1)
