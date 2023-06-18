k = int(input())
res = []
for i in range(k):
    p, m = map(int, input().split())
    arr = []
    cnt = 0
    for j in range(p):
        a = int(input())
        if a <=m: 
            if a in arr: 
                cnt += 1
            else: arr.append(a)
        else: cnt += 1
    res.append(cnt)

for i in res: print(i)
