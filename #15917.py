import sys
n = int(sys.stdin.readline())
res = []

for i in range(n):
    a = int(sys.stdin.readline())
    if a == 1:
        res.append(1)
    else:
        a = bin(a)
        a = a[2:]
        if a[0] == '1' and a[1:] == '0'*(len(a)-1):
            res.append(1)
        else:
            res.append(0)

for i in res:
    print(i)
