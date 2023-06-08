n = int(input())
res = []
for i in range(n):
    a = list(map(str, input().split()))
    hap = float(a[0])
    for i in a[1:]:
        if i == '@':
            hap *= 3
        elif i == '%':
            hap += 5
        elif i == '#':
            hap -= 7
    res.append(f'{hap:.2f}')

for i in res: print(i)
