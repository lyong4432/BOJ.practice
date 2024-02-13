n = int(input())
for i in range(n): 
    s = list(map(int, input().split()))
    print(*s,end=' ')
    if 17 in s and 18 in s: print('\nboth')
    elif 17 in s: print('\nzack')
    elif 18 in s: print('\nmack')
    else: print('\nnone')

    if i != n-1: print()
