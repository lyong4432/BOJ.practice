n = int(input())
ans = []

for i in range(n):
    x,y = map(int, input().split())
    if x >= y :
        ans.append('MMM BRAINS')
    else:
        ans.append('NO BRAINS')

for i in ans:
    print(i)
