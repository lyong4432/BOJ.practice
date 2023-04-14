import math

n, w, h = map(int, input().split())
ans = []
for i in range(n):
    a = int(input())
    if a<=w or a<=h or a<= math.sqrt(w**2 + h**2):
        ans.append('DA')
    else:
        ans.append('NE')

for i in ans:
    print(i)
