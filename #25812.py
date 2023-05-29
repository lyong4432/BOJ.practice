n, r = map(int, input().split())

g, s =0, 0
for i in range(n):
    k = int(input())
    if k+r > k*2:
        g += 1
    elif k + r < k * 2: s += 1

if g > s :
    print(1)
elif g == s:
    print(0)
else: print(2)
