import sys
input = sys.stdin.readline


n = input().strip()
l = len(n)

def gop(k):
    result = 1
    for i in k:
        result *= int(i)
    return result

flag=0
for i in range(l-1):
    if flag == 1: break
    a = n[:i+1]
    b = n[i+1:]
    if gop(a) == gop(b):
        flag = 1

if flag: print('YES')
else: print('NO')
