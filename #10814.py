n = int(input())
res = []
for i in range(n):
    a, b = map(str, input().split())
    a = int(a)
    res.append([a,b])

res.sort(key=lambda x: (x[0]))

for i,j in res:
    print(i, j)
