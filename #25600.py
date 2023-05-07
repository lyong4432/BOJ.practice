n = int(input())
res = []

for i in range(n):
    a, d, g = map(int, input().split())
    if a == d+g:
        res.append(a*2*(d+g))
    else:
        res.append(a*(d+g))

res.sort(reverse=True)

print(res[0])
