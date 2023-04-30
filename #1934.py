import math 
n = int(input())
ans = []
for i in range(n):
    a, b = map(int, input().split())
    ans.append(math.lcm(a,b))

for i in ans:
    print(i)
