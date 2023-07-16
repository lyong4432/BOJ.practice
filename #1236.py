n, m = map(int, input().split())
arr = [0]*m
cnt = []
c = 0
h = 0
for i in range(n):
    s = input()
    cnt.append(s.count('X'))
    for j,k in enumerate(s):
        if k == 'X':
            arr[j] += 1

for i in arr:
    if i == 0:
        c += 1

for i in cnt:
    if i == 0:
        h += 1

if c <= h :
    print(h)
else: print(c)
