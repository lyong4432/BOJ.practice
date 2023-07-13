t = int(input())
res = []
for i in range(t):
    res.append(input())

for i in res: 
    if i[::-1] in res:
        print(len(i), i[len(i)//2])
        break
