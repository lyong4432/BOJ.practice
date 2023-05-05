t = int(input())
res = []
for i in range(t):
    s = int(input())
    for i in range(s):
        a, b = map(int, input().split())
        res.append(f'{a+b} {a*b}')

for i in res:
    print(i)
