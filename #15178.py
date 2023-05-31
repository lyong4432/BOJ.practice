n = int(input())
res = []
for i in range(n):
    a,b,c = map(int, input().split())
    if a+b+c != 180:
        res.append(f'{a} {b} {c} Check')
    else: res.append(f'{a} {b} {c} Seems OK')

for i in res: print(i)
