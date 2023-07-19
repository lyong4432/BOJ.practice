import sys
input =sys.stdin.readline
n = int(input().strip())
res = []
for i in range(n):
    a = float(input().strip())
    res.append(a)

res.sort()

for i in res[:7]:
    print('%.3f'%i)
