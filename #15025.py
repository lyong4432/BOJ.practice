l, r = map(int, input().split())

if l == r:
    if l == 0:
        print('Not a moose')
    else:
        print(f'Even {l*2}')
else: 
    if l > r:
        print(f'Odd {l*2}')
    else:
        print(f'Odd {r*2}')
