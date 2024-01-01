import sys
input = sys.stdin.readline
i = 1
while True:
    l, p, v = map(int, input().split())  
    if l == p == v == 0: break
    if v%p >l:
        print(f'Case {i}: {v//p*l + l}')
    else:
        print(f'Case {i}: {v//p*l + (v%p)}')
    i += 1
