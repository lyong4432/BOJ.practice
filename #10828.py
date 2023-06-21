import sys
input = sys.stdin.readline
n = int(input().strip())

res = []
for i in range(n):
    s = input().strip()

    if s[0:4] == 'push':
        res.append(s[5:])
    elif s == 'top':
        if len(res) == 0:
            print(-1)
        else:
            print(res[-1])
    elif s == 'pop':
        if len(res) == 0:
            print(-1)
        else:
            print(res[-1])
            res.pop()
    elif s == 'size':
        print(len(res))
    elif s == 'empty':
        if len(res) == 0:
            print(1)
        else: print(0)
