n, m = map(int, input().split())
ans = []
for i in range(n):
    a = input()
    ans.append(a[::-1])

for i in ans:
    print(i)
