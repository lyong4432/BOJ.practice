a,b = map(int, input().split())
a = [a+b,a-b]
a.sort()

print(a[1])
print(a[0])
