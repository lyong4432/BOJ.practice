n = int(input())
res = []
ans = []
for i in range(n):
    a = input()
    res.append(a[0])

res_ = set(res)

for i in res_:
    if res.count(i) >= 5:
        ans.append(i)

if len(ans) == 0:
    print('PREDAJA')
else: 
    ans.sort()
    for i in ans:
        print(i,end='')
