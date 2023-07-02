import sys
input = sys.stdin.readline
cnt = 1
res = []

while True: 
    a, buho, b = map(str, input().split())
    a = int(a)
    b = int(b)
    t ="false"
    if buho == "E":
        break
    elif buho == ">":
        if a>b: t = "true"
    elif buho == ">=":
        if a>=b: t = "true"
    elif buho == "<":
        if a<b: t = "true"
    elif buho == "<=":
        if a<=b: t = "true"
    elif buho == "==":
        if a==b: t = "true"
    elif buho == "!=":
        if a!=b: t = "true"
    res.append(f'Case {cnt}: {t}')
    cnt += 1

for i in res: print(i)



    
