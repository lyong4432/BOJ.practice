j = 1
res = []
while j == 1:
    c, d = map(int, input().split())
    if c == 0 and d == 0:
        j =2
    else:
        price = [c*30 + d*40, c*35+d*30, c*40+d*20]
        price.sort()
        res.append(price[0])

for i in res:
    print(i)
