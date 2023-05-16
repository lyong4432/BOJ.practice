j = 1
res = []

while j == 1:
    n = int(input())
    pre = 0
    if n == -1:
        j = 2
        break
    else:
        hap = 0
        for i in range(n):
            a,b = map(int, input().split())
            hap += a*(b-pre)
            pre = b
        res.append(f'{hap} miles')

for i in res:
    print(i)
