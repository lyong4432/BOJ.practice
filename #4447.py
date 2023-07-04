n = int(input())
res = []
for i in range(n):
    a = input()
    g = a.count('G') + a.count('g')
    b = a.count('B') + a.count('b')
    if g > b:
        res.append(f'{a} is GOOD')
    elif g == b:
        res.append(f'{a} is NEUTRAL')
    else: res.append(f'{a} is A BADDY')

for i in res: print(i)
