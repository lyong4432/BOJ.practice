import math
n = int(input())
res = []
for i in range(n):
    a,b = map(int, input().split())
    res.append(math.ceil(a**2/b**2))

for i in res:
    print(i)
