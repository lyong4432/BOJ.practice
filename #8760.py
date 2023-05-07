z = int(input())
res = []
for i in range(z):
    w, k = map(int, input().split())
    res.append(f'{(w*k)//2}')


for i in res:
    print(i)
