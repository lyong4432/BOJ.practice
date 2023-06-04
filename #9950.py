

import sys 
j = 1
res = []

while j == 1:
    a,b,c = map(int, sys.stdin.readline().split())
    if a == b == c == 0:
        j = 2
    else: 
        if a == 0:
            res.append(f'{c//b} {b} {c}')
        elif b == 0:
            res.append(f'{a} {c//a} {c}')
        elif c == 0:
            res.append(f'{a} {b} {a*b}')

for i in res:
    print(i)
