n = int(input())
res = []
for i in range(n):
    x = int(input())
    if abs(x)%2 == 0:
        res.append(f'{x} is even')
    else:
        res.append(f'{x} is odd')

for i in res:
    print(i)
