n = int(input())
res = []

for i in range(n):
    a, b = map(str, input().split())
    dis = 'Distances: '
    for j in range(len(a)):
        aa = ord(a[j])
        bb = ord(b[j])
        if aa > bb :
            dis += f'{bb+26 - aa} '
        else: dis += f'{bb - aa} '
    res.append(dis)

for i in res: print(i)
