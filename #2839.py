n = int(input())
ans = []
for i in range(n):
    for j in range(n):
        if 5*i + 3*j == n:
            ans.append(i+j)



if ans == []:
    print(-1)
else:
    print(min(ans))
