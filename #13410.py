n, k = map(int, input().split())
res = []
for i in range(1,k+1):
    a = str(n*i)[::-1]
    res.append(int(a))
res.sort(reverse=True)
print(res[0])
