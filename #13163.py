n = int(input())
res = []
for i in range(n):
    names = list(map(str,input().split()))
    name = 'god'
    for i in names[1:]:
        name += i
    res.append(name)
    
for i in res: print(i)
