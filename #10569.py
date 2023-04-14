t = int(input())
ans = []
for i in range(t):
    v,e = map(int, input().split())
    ans.append(2-v+e)

for i in ans:
    print(i)
