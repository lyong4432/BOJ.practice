j = 1
res = []
while j == 1:
    ini,wd,money = map(str, input().split())
    ini = int(ini)
    money = int(money)
    if ini == 0 and wd == 'W' and money == 0:
        j = 0
    else:
        acc = 0
        if wd == 'W':
            acc = ini - money
        elif wd == 'D': acc = ini + money
        if acc <-200:
            res.append('Not allowed')
        else: res.append(acc)

for i in res:
    print(i)

