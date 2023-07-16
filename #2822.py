res = []
for i in range(8):
    res.append(int(input()))


res1 = sorted(res,reverse=True)

hap = sum(res1[:5])
print(hap)
for i,j in enumerate(res):
    if j >= res1[4]:
        print(i+1,end=' ')
