import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    N = []
    d = 2
    while n != 1: 
        if n % d != 0: 
            d += 1
        else: 
            n //= d
            N.append(d)
    set_N = list(set(N))
    set_N.sort()

    for i in set_N:
        print(i, N.count(i))
