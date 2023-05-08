a, b, c, d = map(int, input().split())
coming = list(map(int, input().split()))
res = []

for i in coming:
    cnt = 0
    if 0< i % (a+b) <=a:
        cnt += 1
    if 0 < i % (c+d) <=c:
        cnt += 1
    res.append(cnt)

for i in res:
    print(i)
