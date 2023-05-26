t = int(input())
res = []
a,b,c = 0,0,0
for i in range(t):
    pack = list(map(int, input().split()))
    a += pack[0]
    b += pack[1]
    c += pack[2]

    if a <30 or b <30 or c<30:
        res.append('NO')
    else:
        mid = [a,b,c]
        mid.sort()
        res.append(mid[0])

        a -= mid[0]
        b -= mid[0]
        c -= mid[0]

for i in res:
    print(i)
