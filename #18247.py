n = int(input())
res =[]
for i in range(n):
    a, b = map(int, input().split())
    if a <12 or b<4:
        res.append(-1)
    else:
        res.append(b*11+4)

for i in res:
    print(i)
