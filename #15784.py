n, a, b =map(int, input().split())
x = []
for i in range(n):
    y = list(map(int, input().split()))
    x.append(y)

h = 0
for i in x[a-1]:
    if i > x[a-1][b-1]:
        h = 1
for i in range(n):
    if x[i][b-1] != x[a-1][b-1]:
        if x[i][b-1] > x[a-1][b-1]:
            h = 1

if h == 0:
    print('HAPPY')
else: print('ANGRY')
