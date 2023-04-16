t = int(input())
x = 0
ans = []
for _ in range(t):
    n, d = map(int, input().split())
    result = 0
    for i in range(n):
        v, f, c = map(int, input().split())
        x = v * f / c
        if x >= d:
            result += 1
    ans.append(result)

for i in ans:
    print(i)
