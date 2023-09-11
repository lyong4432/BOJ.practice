n = int(input())
for i in range(n):
    s = list(map(int, input().split()))
    e, o = 0, 0 
    
    for j in s[1:]:
        if j % 2 == 0:
            e += j
        else: o += j
    
    if e == o:
        print('TIE')
    elif e > o:
        print('EVEN')
    else: print('ODD')
