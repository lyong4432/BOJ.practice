n = int(input())
res = []

for i in range(n):
    a = input()
    hap = 0
    cnt = 1
    for j in a:
        if j == 'O':
            hap += cnt
            cnt += 1
        else: 
            cnt = 1
    res.append(hap)

for i in res: print(i)
