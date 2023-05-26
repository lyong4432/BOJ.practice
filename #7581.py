j = 1
res = []
while j == 1:
    l, w, h, v = map(int, input().split())
    if l == 0 and w == 0 and h == 0 and v == 0:
        j = 2
    else:
        if v == 0:
            v = l * w * h
        elif l == 0:
            l = int(v / (w * h))
        elif w == 0:
            w = int(v / (l * h))
        elif h == 0:
            h = int(v / (w * l))
        res.append(f'{l} {w} {h} {v}')

for i in res:
    print(i)
