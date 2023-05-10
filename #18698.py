n = int(input())
res = []
for i in range(n):
    a = input()
    cnt = 0
    for i in a:
        if i == 'U':
            cnt += 1
        if i =='D':
            break
    res.append(cnt)

for i in res:
    print(i)
