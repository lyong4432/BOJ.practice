import math
t = int(input())
res = []
for i in range(t):
    h,w,n= map(int, input().split())
    if n%h == 0:
        res.append(f'{h}{math.ceil(n/h):02d}')
    else:
        res.append(f'{n%h}{math.ceil(n/h):02d}')


for i in res:
    print(i)
