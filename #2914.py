import math

a, i = map(int, input().split())
ans = []
for x in range(a*i,0,-1):
    if math.ceil(x/a) == i:
       ans.append(x)

print(min(ans))
