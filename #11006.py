t = int(input())
x = 0
ans = []
for i in range(t):
    a,b = map(int, input().split())
    u = 2 * b - a
    v = b - u
    ans.append(f'{u} {v}')

for i in ans:
    print(i)
