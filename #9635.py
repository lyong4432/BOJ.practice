t = int(input())
res = []
for i in range(t):
    n, x, y = map(int, input().split())
    colors = list(map(int, input().split()))
    if colors[0] == x and colors[-1] == y:
        res.append("BOTH")
    elif colors[0] == x:
        res.append("EASY")
    elif colors[-1] == y:
        res.append("HARD")
    else: 
        res.append("OKAY")

for i in res: print(i)
