n = int(input())
res = []
for i in range(n):
    a = int(input())
    cnt = 0
    for i in range(1,a+1):
        if a%i == 0:
            cnt += 1
    res.append(f'{a} {cnt}')

for i in res:
    print(i)
