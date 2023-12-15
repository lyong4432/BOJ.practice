import sys
input = sys.stdin.readline

alpha = {}
for i in range(1,27):
    alpha[chr(i+64)] = str(i)



for _ in range(int(input())):
    n, cn = map(str, input().split())
    N = list(map(str, input().split()))
    for i in N: 
        if cn == 'C':
            print(alpha[i],end=' ')
        elif cn == 'N':
            for k,v in alpha.items():
                if v == i:
                    print(k, end=' ') 
    print()
