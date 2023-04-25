n = int(input())
ans = []
for i in range(n):
    a = list(map(int, input().split()))
    ans.append(a)

ans.sort()

for [a,b] in ans:
    print(a,b)
