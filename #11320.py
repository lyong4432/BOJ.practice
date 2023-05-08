import math
n = int(input())
res = []

for i in range(n):
    a, b = map(int, input().split())
    a_tri = (a**2)
    b_tri =  (b**2)
    res.append(math.ceil(a_tri/b_tri))

for i in res:
    print(i)
