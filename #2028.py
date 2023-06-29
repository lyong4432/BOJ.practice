import sys
input = sys.stdin.readline

n = int(input())
res = []
for i in range(n):
    s = input().strip()
    ss = str(int(s)**2)
    if s == ss[-len(s):]:
        res.append('YES')
    else: res.append('NO')

for i in res: print(i)
