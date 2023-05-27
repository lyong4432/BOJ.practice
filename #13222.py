import math
n, w, h = map(int, input().split())
res = []
num = [w,h,math.sqrt(w**2+h**2)]
for i in range(n):
    a = int(input())
    if a <= num[0] or a <= num[1] or a <= num[2]:
        res.append('YES')
    else: res.append('NO')

for i in res: print(i)
