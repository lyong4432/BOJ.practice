import sys

input = sys.stdin.readline

while True:
    cnt = 0
    a,b,c,d = map(int, input().split())
    if a == b == c == d == 0: break
    elif a == b == c == d: print(0)
    else: 
        while True:
            n1 = abs(a-b)
            n2 = abs(b-c)
            n3 = abs(c-d)
            n4 = abs(d-a)

            a = n1
            b = n2
            c = n3
            d = n4

            if a == b == c == d:
                cnt += 1
                print(cnt)
                break
            else: cnt += 1
