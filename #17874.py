n, h, v = map(int, input().split())

a = [h,n-h]
b = [v,n-v]

a.sort()
b.sort()

print(a[1]*b[1]*4)
