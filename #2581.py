m = int(input())
n = int(input())
res = []
for i in range(m,n+1):
    hap = 0
    if i>1:
        for j in range(2,i):
            if i%j == 0:
                hap += 1
        if hap == 0:
            res.append(i)
    
if res == []:
    print(-1)
else:
    print(sum(res))
    print(res[0])
    
