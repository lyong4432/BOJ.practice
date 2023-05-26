j = 1
res = []

while j == 1:
    h1, m1, h2, m2 = map(int, input().split())
    if h1 ==0 and m1 == 0 and h2 == 0 and m2 == 0:
        j = 2
    else: 
        time1 = h1 * 60 + m1
        time2 = h2 * 60 + m2
        if time2 >= time1:
            res.append(time2 - time1)
        else:
            res.append((h2+24)*60 +m2 - time1)

for i in res:
    print(i)
