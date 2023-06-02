n = int(input())
res = []
for i in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    if a == b:
        if a[2]**2 == a[1]**2 + a[0]**2:
            res.append('YES')
        else: res.append('NO')
    else: res.append('NO')

for i in res:print(i)
