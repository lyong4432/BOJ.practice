import sys
input = sys.stdin.readline

n = int(input())
res = []
for i in range(n):
    s = input().strip()
    if s == 'P=NP':
        res.append('skipped')
    else:
        a,b = s.split('+')
        res.append(int(a)+int(b))


for i in res: print(i)
