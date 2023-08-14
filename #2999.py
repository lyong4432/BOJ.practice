import sys
input = sys.stdin.readline
s = input().strip()
n = len(s)

max_r = 0
max_c = 0
for r in range(1,n+1):
    c = n//r
    if r <= c and r*c == n:
        max_r = r
        max_c = c

res = ['']*max_r
c = 0
for _ in range(max_c):
    for i in range(max_r):
        res[i] += s[c]
        c += 1
    

for i in res[:-1]: print(i,end='')
print(res[-1])
