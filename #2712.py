t= int(input())
ans = []
for i in range(t):
    a,b = map(str, input().split())
    a = float(a)
    if b == 'kg':
        ans.append(f'{a*(2.2046):.4f} lb')
    elif b == 'l':
        ans.append(f'{a*(0.2642):.4f} g')
    elif b == 'g':
        ans.append(f'{a*(3.7854):.4f} l')
    elif b == 'lb':
        ans.append(f'{a*(0.4536):.4f} kg')

for i in ans:
    print(i)
