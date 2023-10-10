import sys
import math
input = sys.stdin.readline
i = 1
while True:
    a,b,c = map(int, input().split())
    result = ''
    if a==0 and b==0 and c==0:
        break 
    if i != 1: 
        print()
    print(f"Triangle #{i}")
    if a == -1:
        if b < c:
            a = math.sqrt(c**2-b**2)
            print("a = %.3f"%a)
        else: print('Impossible.')
    elif b == -1:
        if a < c:
            b = math.sqrt(c**2-a**2)
            print("b = %.3f"%b)
        else: print('Impossible.')
    elif c == -1:
        c = math.sqrt(a**2+b**2)
        print("c = %.3f"%c)

    i += 1
   
    
